#  Auto Mapping Agent(Structured Agentic Framework)

An **NLP-based agentic AI system** using **Ollama's Phi-3 LLM** to perform autonomous mapping and decision-making tasks. Built with **FastAPI** and **Uvicorn**, this project provides a scalable backend for intelligent interactions, suitable for research, planning tools, or autonomous agents.

##Project Highlights

**LLM Reasoning**: Powered by Ollama’s **Phi-3** model
**Agentic Behavior**: For intelligent decision-making and task execution
**API Deployment**: Lightweight FastAPI backend with Uvicorn server
**Extensible Design**: Ideal base for custom NLP agent workflows

---

## Setup Instructions


### 1. Clone the Repository

```bash
git clone https://github.com/MandavaKashyapSai/auto-mapping-agent.git
cd auto-mapping-agent


Install Python Dependencies
pip install -r requirements.txt

If you don’t have a requirements.txt yet, create one with:
pip install fastapi uvicorn
pip freeze > requirements.txt

Setting Up Ollama with Phi-3
Step 1: Download and Install Ollama
Visit: https://ollama.com/download
Follow platform-specific instructions for Windows, macOS, or Linux.

Step 2: Start Ollama and Download Phi-3
Once Ollama is installed, open a terminal and run:

ollama run phi3
This will download and start the Phi-3 LLM locally.

ollama serve

ollama pull phi3


Running the App
Make sure Ollama is running in the background.

Then start the FastAPI server:
python main.py



# Agent-Mapping
