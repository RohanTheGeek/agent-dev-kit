# agent.py
import requests
import os_tools

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

FUNCTIONS = [
    "get_cpu_usage()",
    "get_memory_usage()",
    "get_disk_usage()",
    "get_uptime()",
    "get_os_info()",
    "list_files(path='.')",
    "create_file(filename, content='')",
    "read_file(filename)",
    "delete_file(filename)",
    "rename_file(old_name, new_name)",
    "move_file(src, dst)",
    "copy_file(src, dst)",
    "zip_folder(folder_path)",
    "create_directory(dirname)",
    "delete_directory(dirname)",
    "check_connectivity()",
    "get_ip_address()",
    "get_clipboard()",
    "set_clipboard(text)",
    "take_screenshot()"
]

def ask_agent(user_input):
    prompt = (
        "You are a system assistant. Based on the user’s request, return a valid Python function call "
        "from this list only:\n" +
        "\n".join(FUNCTIONS) +
        "\n\nExample:\nUser: What is the CPU usage?\nAssistant: get_cpu_usage()\n\n"
        f"User: {user_input}\nAssistant:"
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=body)
        result = response.json()["choices"][0]["message"]["content"].strip()

        print(f"\n🔧 Calling: {result}")
        exec_result = eval(f"os_tools.{result}")
        return exec_result

    except Exception as e:
        return f"[ERROR] Failed to execute command: {e}"


# app.py
from agent import ask_agent

def main():
    print("🧠 System Agent (Groq-powered)")
    print("Ask about CPU, files, memory, IP, screenshots, clipboard, folders, etc.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("💬 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            result = ask_agent(user_input)
            print("\n📋 Result:")
            print(result)
        except Exception as e:
            print(f"[ERROR] {e}")

        print("-" * 50)

if __name__ == "__main__":
    main()
