# 🧠 Agent Development Kit (ADK)

> An AI-powered system monitoring and control agent that streams real-time system metrics, executes natural language commands, and manages system resources — powered by Groq's LLaMA-4.

---

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![LLM](https://img.shields.io/badge/LLM-Groq%20LLaMA--4-orange)

---

## 🚀 Overview

**ADK (Agent Development Kit)** is a modular Python-based framework designed to:

- Monitor system performance (CPU, Memory, Disk, Uptime)
- Receive and execute natural language commands via Groq's LLM
- Perform file system operations, clipboard access, screenshots, and cleanup
- Stream metrics to a remote server every few seconds
- Act as a base framework for building AI-enabled system agents

---

## 📁 Project Structure

```
agent-dev-kit/
├── agent.py           # Converts natural language to function calls using Groq LLM
├── app.py             # CLI interface to interact with the agent
├── agent side.py      # Background process that sends system metrics
├── os_tools.py        # Implements system utility functions
├── requirements.txt   # Python dependencies
├── .gitignore         # Files to ignore in version control
└── README.md          # Project documentation
```

---

## ⚙️ Features

- 📊 **Real-Time Metrics**: CPU, Memory, Disk usage, and Uptime
- 🧠 **Groq LLM Integration**: Understands commands like _"Show me memory usage"_ or _"Take a screenshot"_
- 🔁 **Continuous Agent**: Background loop to send system health to server
- 🧹 **Auto Cleanup**: Cleans temp/cache files if disk usage exceeds 80%
- 💻 **Cross-Platform**: Designed to work on most Unix-like systems

---

## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agent-dev-kit.git
cd agent-dev-kit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the CLI Agent

```bash
python app.py
```

### 4. Run the Background Monitoring Agent

```bash
python "agent side.py"
```

> ⚠️ Replace your Groq API key in `agent.py` before running.

---

## 🧠 Supported Natural Language Commands

The agent can understand and execute requests like:

- "What’s the CPU usage?"
- "List files in the current directory"
- "Take a screenshot"
- "Copy text to clipboard"
- "Show me the uptime"
- "Create a new folder called testdir"

---

## 🔐 Security Note

This tool executes real system commands. Use responsibly and avoid deploying on shared or critical machines without restrictions.

---

## 📦 Dependencies

- `psutil` – System metrics
- `requests` – Groq API interaction
- `pyperclip` – Clipboard access
- `Pillow` – Screenshot support

Install them with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to fork, improve, and share.

---

## 👨‍💻 Author

Built with ❤️ by **[Your Name]**  
Let's connect: [LinkedIn](https://linkedin.com/in/yourprofile)
