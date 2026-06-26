from engine.inference_engine import InferenceEngine

engine = InferenceEngine()

print("Offline SLM Optimizer")
print("Type exit to quit")

while True:

    prompt = input("\nYou : ")

    if prompt.lower() == "exit":
        break

    answer = engine.process(prompt)

    print("\nAI :", answer)