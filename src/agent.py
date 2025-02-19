import re
from typing import Optional
from src.llm_plugin import LLMPlugin
from src.custom_logging import setup_logger

logger = setup_logger(__name__)

class AgentCreator:
    """
    AgentCreator generates production-level Python agent code using an LLM plugin.
    """
    PROMPT_TEMPLATE = (
        "You are an AI developer. Generate production-level Python code for an agent that interacts with an API.\n\n"
        "API Documentation:\n{api_doc}\n\n"
        "Agent Description:\n{agent_desc}\n\n"
        "The generated agent should:\n"
        "- Utilize the API as documented.\n"
        "- Include proper error handling.\n"
        "- Use classes and methods with clean, maintainable code.\n"
        "- Don't give any examples like '(example@example.com) # Replace with your app's info', if its mentioned in document, please give as it is."
        "- Always givr proper and full code that can be run with if __main__."
        "- Be ready for testing.\n\n"
        "Generate the complete Python code."
        "Remember give only python code which can be run directly, no explanations, nothing."
    )

    def __init__(self, llm_plugin: LLMPlugin):
        self.llm_plugin = llm_plugin

    def build_prompt(self, api_doc: str, agent_desc: Optional[str] = None) -> str:
        agent_desc = agent_desc or "N/A"
        prompt = self.PROMPT_TEMPLATE.format(api_doc=api_doc, agent_desc=agent_desc)
        logger.debug("Built prompt: %s", prompt)
        return prompt

    def create_agent(self, api_doc: str, agent_description: Optional[str] = None) -> str:
        prompt = self.build_prompt(api_doc, agent_description)
        try:
            generated_code = self.llm_plugin.generate_code(prompt)
            logger.info("Generated agent code successfully.")
            
            python_matches = re.findall(r"```python(.*?)```", generated_code, re.DOTALL)
            code = python_matches[0].strip() if python_matches else generated_code
            
            return code
        except Exception as e:
            logger.error("Error generating agent code: %s", e)
            raise

    def save_agent_code(self, code: str, output_path: str = "generated_agent.py"):
        try:
            if not code.strip():
                logger.error("No code to save. The code content is empty.")
                return
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(code)
            logger.info("Agent code saved to %s", output_path)
        except Exception as error:
            logger.error("Failed to save agent code: %s", error)
            raise
