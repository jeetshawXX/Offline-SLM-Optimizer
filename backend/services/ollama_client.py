import json
import requests

from config import MODEL_NAME


class OllamaClient:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"
        self.model = MODEL_NAME

    def generate(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        response.raise_for_status()

        return response.json()["response"]

    def generate_stream(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }

        response = requests.post(
            self.url,
            json=payload,
            stream=True
        )

        response.raise_for_status()

        for line in response.iter_lines():

            if not line:
                continue

            data = json.loads(line)

            if "response" in data:
                yield data["response"]

            if data.get("done", False):
                break