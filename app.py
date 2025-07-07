# app.py
from agent import ask_agent

def main():
    print("🧠 System Agent (Groq-powered)")
    print("Ask about CPU, files, memory, IP, screenshots, clipboard, etc.")
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
