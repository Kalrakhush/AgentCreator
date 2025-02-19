"""
LLM Plugin interface and implementations for Gemini and AWS Bedrock.
"""

import json
import logging
import requests
import boto3
import google.generativeai as genai
from abc import ABC, abstractmethod
from src.config import (
    GOOGLE_API_KEY,
    AWS_BEDROCK_MODEL_ID,
    AWS_REGION,
    LLM_PROVIDER,
)

logger = logging.getLogger(__name__)


class LLMPlugin(ABC):
    @abstractmethod
    def generate_code(self, prompt: str) -> str:
        """
        Generate code based on the provided prompt.
        :param prompt: The prompt string to send to the LLM.
        :return: Generated code as a string.
        """
        pass


class GeminiLLMPlugin(LLMPlugin):
    """
    Gemini LLM Plugin using Google's `google.generativeai` SDK.
    """

    def __init__(self, api_key: str = GOOGLE_API_KEY):
        self.api_key = api_key
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-2.0-flash")  # Use the appropriate model version.
            logger.info("Initialized Gemini LLM plugin.")
        except Exception as e:
            logger.error("Failed to initialize Gemini API: %s", e)
            raise

    def generate_code(self, prompt: str) -> str:
        logger.debug("Sending prompt to Gemini API: %s", prompt)
        try:
            response = self.model.generate_content(prompt)
            generated_text = response.text.strip() if response.text else ""
            if not generated_text:
                logger.error("No generated text found in Gemini response.")
                raise ValueError("Gemini API did not return generated text.")
            logger.info("Successfully generated code using Gemini.")
            return generated_text
        except Exception as e:
            logger.error("Error during Gemini API call: %s", e)
            raise


class AWSBedrockLLMPlugin(LLMPlugin):
    """
    AWS Bedrock LLM Plugin.
    Uses boto3 to call the AWS Bedrock runtime for code generation.
    """

    def __init__(self, model_id: str = AWS_BEDROCK_MODEL_ID, region: str = AWS_REGION):
        self.model_id = model_id
        self.region = region
        try:
            self.client = boto3.client("bedrock-runtime", region_name=self.region)
            logger.info("Initialized AWS Bedrock client in region %s.", self.region)
        except Exception as e:
            logger.error("Failed to initialize AWS Bedrock client: %s", e)
            raise

    def generate_code(self, prompt: str) -> str:
        logger.debug("Sending prompt to AWS Bedrock: %s", prompt)
        try:
            payload = {
                "prompt": prompt,
                "maxTokens": 1024,  # Adjust as needed.
            }
            response = self.client.invoke_model(
                ModelId=self.model_id,
                ContentType="application/json",
                Accept="application/json",
                Body=json.dumps(payload),
            )
            response_body = response["Body"].read().decode("utf-8")
            logger.debug("Raw response from AWS Bedrock: %s", response_body)
            result = json.loads(response_body)
            generated_text = result.get("generated_text", "")
            if not generated_text:
                logger.error("No generated text found in AWS Bedrock response.")
                raise ValueError("AWS Bedrock did not return generated text.")
            logger.info("Successfully generated code using AWS Bedrock.")
            return generated_text
        except Exception as e:
            logger.error("Error during AWS Bedrock API call: %s", e)
            raise


def get_llm_plugin() -> LLMPlugin:
    """
    Factory function to return the appropriate LLM plugin based on configuration.
    """
    if LLM_PROVIDER.upper() == "GEMINI":
        logger.info("Using GeminiLLMPlugin as the LLM provider.")
        return GeminiLLMPlugin()
    elif LLM_PROVIDER.upper() == "AWS_BEDROCK":
        logger.info("Using AWSBedrockLLMPlugin as the LLM provider.")
        return AWSBedrockLLMPlugin()
    else:
        logger.error("LLM provider '%s' not implemented.", LLM_PROVIDER)
        raise NotImplementedError(f"LLM provider {LLM_PROVIDER} not implemented.")