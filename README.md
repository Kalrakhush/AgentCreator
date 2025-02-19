# AI Agent Creator

This project creates an **AI Agent** from API documentation using a Large Language Model (LLM). It supports both **Gemini** (Google Generative AI) and **AWS Bedrock** as LLM providers. For demonstration, it uses `testdoc.txt` as a sample API documentation file.

---

## How It Works

1. **Agent Creation**  
   - Run `agent_creator.py`, which reads `testdoc.txt` (or another API doc you specify).
   - The content is sent to your chosen LLM (Gemini or AWS Bedrock).
   - The script generates Python code for a new agent and saves it as `generated_agent_<filename>.py` inside the `agents/` folder.

2. **Agent Testing**  
   - To verify the generated agent, simply run the new `.py` file from the `agents` folder (e.g., `python agents/generated_agent_testdoc.py`).

---

## Project Structure

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

---

## Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **LLM Credentials**:
  - **Gemini** requires a Google Generative AI key (`GOOGLE_API_KEY`).
  - **AWS Bedrock** requires AWS credentials and the Bedrock model ID.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/agent-creator.git
   cd agent-creator

**Create and Activate a Virtual Environment:**
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

**Install Dependencies:**

pip install -r requirements.txt


**Create a .env File**

In the project root, create a .env file to specify your LLM provider and API keys:
See the sample given in repository

**Usage**
Run agent_creator.py:

python agent_creator.py

This script reads testdoc.txt by default as the API documentation.
It sends the content to the chosen LLM (Gemini or AWS Bedrock).
It generates agent code and saves it to agents/generated_agent_testdoc.py (if the doc is named testdoc.txt).

Check the Generated Agent:

Inside the agents/ folder, you’ll find the newly created file, for example:

agents/
└── generated_agent_testdoc.py

Test the Generated Agent:

python agents/generated_agent_testdoc.py
This confirms the agent code is runnable. The agent’s functionality depends on how the LLM interprets the documentation.

**Logs**
Log Files are stored in the logs/ folder (automatically created by custom_logging.py).
You can check app.log (or any rotating logs) for debug info and errors.

**Customizing the API Documentation**
If you want to use a YAML-based API documentation, rename or place your .yml file in the project folder.
Modify agent_creator.py to point to that file. If it ends with .yml or .yaml, the api_parser.py will parse and validate it automatically.

Known Limitations
AWS Bedrock code path is present but not tested (no AWS key available).
Generated agent code quality depends on the LLM’s capabilities.


That’s it! If you have any further questions or run into issues, please open an issue or contact me.
Khushpreet Singh
khushpreets016@gmail.com








You said:
give  in way so that i can copy
Reasoned for 8 seconds
Below is a sample README.md file you can copy and paste directly into your repository. Adjust file names, URLs, and other details as needed for your specific project.

markdown
Copy
Edit
# AI Agent Creator

This project creates an **AI Agent** from API documentation using a Large Language Model (LLM). It supports both **Gemini** (Google Generative AI) and **AWS Bedrock** as LLM providers. For demonstration, it uses `testdoc.txt` as a sample API documentation file.

---

## How It Works

1. **Agent Creation**  
   - Run `agent_creator.py`, which reads `testdoc.txt` (or another API doc you specify).
   - The content is sent to your chosen LLM (Gemini or AWS Bedrock).
   - The script generates Python code for a new agent and saves it as `generated_agent_<filename>.py` inside the `agents/` folder.

2. **Agent Testing**  
   - To verify the generated agent, simply run the new `.py` file from the `agents` folder (e.g., `python agents/generated_agent_testdoc.py`).

---

## Project Structure

AGENTCREATOR/ ├── agents/ # Folder where generated agents are saved ├── logs/ # Auto-created folder for logs ├── src/ │ ├── init.py │ ├── agent.py # Contains the AgentCreator class │ ├── api_parser.py # APIDocParser for YAML-based API docs │ ├── config.py # Configuration for LLM provider, keys, etc. │ ├── custom_logging.py # Sets up logging, creates logs folder if missing │ └── llm_plugin.py # LLM plugin interface & Gemini/AWS classes ├── .env # Environment variables (not committed to Git) ├── agent_creator.py # Main script that loads doc & generates agent ├── requirements.txt # Python dependencies └── testdoc.txt # Sample API documentation (text-based)

yaml
Copy
Edit

---

## Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **LLM Credentials**:
  - **Gemini** requires a Google Generative AI key (`GOOGLE_API_KEY`).
  - **AWS Bedrock** requires AWS credentials and the Bedrock model ID.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/agent-creator.git
   cd agent-creator
Create and Activate a Virtual Environment

bash
Copy
Edit
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create a .env File

In the project root, create a .env file to specify your LLM provider and API keys:

dotenv
Copy
Edit
# .env example

# "GEMINI" or "AWS_BEDROCK"
LLM_PROVIDER=GEMINI

# If using Gemini:
GOOGLE_API_KEY=YOUR_GEMINI_KEY

# If using AWS Bedrock:
AWS_BEDROCK_MODEL_ID=your-bedrock-model-id
AWS_REGION=us-east-1
Note: Do not commit .env to source control. You must provide valid keys to run the project.

Usage
Run agent_creator.py

bash
Copy
Edit
python agent_creator.py
By default, this reads testdoc.txt as the API documentation.
It generates an agent and saves it to agents/generated_agent_testdoc.py.
Test the Generated Agent

bash
Copy
Edit
python agents/generated_agent_testdoc.py
This verifies the newly created agent can run. Its functionality depends on how the LLM interpreted the doc.
Logs
A logs/ folder is automatically created (if missing) by custom_logging.py.
Check app.log or rotating logs inside logs/ for debug messages and errors.
Known Limitations
AWS Bedrock integration is present but not tested if you don’t have AWS credentials.
Generated code’s quality depends on the LLM output.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

