import os
from agent import AgentCreator
from llm_plugin import get_llm_plugin
from custom_logging import setup_logger
from api_parser import APIDocParser

logger = setup_logger(__name__)

def load_api_doc(file_path: str) -> str:
    if not os.path.exists(file_path):
        logger.error("%s not found.", file_path)
        raise FileNotFoundError(f"{file_path} not found.")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()
    logger.info("Loaded API documentation.")
    return content

def create_agents_folder() -> str:
    agents_dir = os.path.join(os.getcwd(), "agents")
    if not os.path.exists(agents_dir):
        os.makedirs(agents_dir)
        logger.info("Created 'agents' folder for saving generated agents.")
    return agents_dir

def get_file_name_from_doc(api_doc_filename: str) -> str:
    base_name = os.path.splitext(api_doc_filename)[0]
    return f"generated_agent_{base_name}.py"

def main():
    try:
        # Specify the API documentation file name in main only.
        api_doc_filename = "text.txt"  # change to "api_documentation.yml" if using YAML
        
        # If the file is YAML, parse it with APIDocParser; otherwise, load it as plain text.
        if api_doc_filename.endswith((".yml", ".yaml")):
            parser = APIDocParser(api_doc_filename)
            api_doc = parser.get_parsed_doc()
        else:
            api_doc = load_api_doc(api_doc_filename)
        
        # Get the appropriate LLM plugin and initialize AgentCreator.
        llm = get_llm_plugin()
        agent_creator = AgentCreator(llm)
        
        # Generate the agent code using the (possibly parsed) API documentation.
        agent_code = agent_creator.create_agent(
            api_doc,
            agent_description="Agent for managing users"
        )
        
        # Create the agents folder and determine the output file name based on the API doc filename.
        agents_dir = create_agents_folder()
        file_name = get_file_name_from_doc(api_doc_filename)
        file_path = os.path.join(agents_dir, file_name)
        
        # Save the generated agent code in the agents folder.
        agent_creator.save_agent_code(agent_code, file_path)
        
        logger.info(f"Agent saved as: {file_path}")
        return "Agent generation workflow completed successfully."
    
    except Exception as e:
        logger.error("Workflow failed: %s", e)

if __name__ == "__main__":
    main()
