"""
Configuration for the AI Agent Generator project.
"""

import os
from dotenv import load_dotenv
load_dotenv()


# Define the LLM provider: "GEMINI" or "AWS_BEDROCK"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "GEMINI")

# Gemini API configuration.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# AWS Bedrock configuration.
AWS_BEDROCK_MODEL_ID = os.getenv("AWS_BEDROCK_MODEL_ID", "your-bedrock-model-id")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
