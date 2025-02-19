# AI Agent Creator

This project creates an AI Agent from API documentation using a Large Language Model (LLM). It supports both **Gemini (Google Generative AI)** and **AWS Bedrock** as LLM providers. For demonstration, it uses `testdoc.txt` as a sample API documentation file.

## How It Works

### Agent Creation

- **Run `agent_creator.py`:**  
  This script reads `testdoc.txt` (or another API documentation file you specify).

- **LLM Interaction:**  
  The content is sent to your chosen LLM (Gemini or AWS Bedrock).

- **Agent Generation:**  
  The script generates Python code for a new agent and saves it as `generated_agent_<filename>.py` inside the `agents/` folder.

### Agent Testing

To verify the generated agent, simply run the new Python file from the `agents` folder (e.g., `python agents/generated_agent_testdoc.py`).

## Project Structure

```plaintext
AGENTCREATOR/
├── agents/                 # Folder where generated agents are saved
├── logs/                   # Auto-created folder for logs
├── src/
│   ├── __init__.py
│   ├── agent.py            # AgentCreator class
│   ├── api_parser.py       # APIDocParser class (for YAML docs)
│   ├── config.py           # Configuration for LLM provider, keys, etc.
│   ├── custom_logging.py   # Sets up logging and creates logs folder
│   └── llm_plugin.py       # LLM plugin interface & Gemini/AWS Bedrock classes
├── .env                    # Environment variables (not committed to Git)
├── agent_creator.py        # Main script to create agent from API docs
├── requirements.txt        # Python dependencies
└── testdoc.txt             # Example API documentation (text-based)
```
### Prerequisites
-Python 3.8+
-pip (Python package manager)

**LLM Credentials:**

Gemini: Requires a Google Generative AI key (GOOGLE_API_KEY).
AWS Bedrock: Requires AWS credentials and the Bedrock model ID.

### Installation
**1. Clone the Repository**

```bash
Copy
Edit
git clone https://github.com/your_username/agent-creator.git
cd agent-creator
```

**2. Create and Activate a Virtual Environment**
```bash
Copy
Edit
python -m venv venv
```

**3. Install Dependencies**
```bash
Copy
Edit
pip install -r requirements.txt
```

**4. Create a .env File**

In the project root, create a .env file to specify your LLM provider and API keys. Refer to the sample provided in the repository.

**Usage**

Run agent_creator.py
```bash
Copy
Edit
python agent_creator.py
```

This script reads testdoc.txt by default as the API documentation. It sends the content to the chosen LLM (Gemini or AWS Bedrock) and generates agent code. The code is saved to agents/generated_agent_testdoc.py (if the doc is named testdoc.txt).

### Check the Generated Agent
Inside the agents/ folder, you’ll find the newly created file, for example:

```plaintext
Copy
Edit
agents/
└── generated_agent_testdoc.py
```

**Test the Generated Agent**
```bash
Copy
Edit
python agents/generated_agent_testdoc.py
```

This confirms that the agent code is runnable. The agent’s functionality depends on how the LLM interprets the documentation.

**Logs**

Log files are stored in the logs/ folder (automatically created by custom_logging.py). You can check app.log (or any rotating logs) for debug information and errors.

**Customizing the API Documentation**

If you want to use a YAML-based API documentation:

-Rename or place your .yml/.yaml file in the project folder.

-Modify agent_creator.py to point to that file.

-If the file ends with .yml or .yaml, api_parser.py will automatically parse and validate it.

**Known Limitations**
-The AWS Bedrock code path is present but not tested (no AWS key available).
-The quality of the generated agent code depends on the LLM’s capabilities.
-That’s it! If you have any further questions or run into issues, please open an issue or contact me.

Khushpreet Singh
Email: khushpreets016@gmail.com
