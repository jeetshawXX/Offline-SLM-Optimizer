from services.ollama_client import OllamaClient


class InferenceEngine:

    def __init__(self):
        self.client = OllamaClient()

    def process(self, prompt):

        response = self.client.generate(prompt)

        return response