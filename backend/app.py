from services.ollama_client import OllamaClient

client = OllamaClient()

print("Offline AI Assistant")
print("Type exit to quit")

while True:

    prompt = input("\nYou : ")

    if prompt.lower() == "exit":
        break

    answer = client.generate(prompt)

    print("\nAI :", answer)