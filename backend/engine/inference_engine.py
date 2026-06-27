from services.ollama_client import OllamaClient
from optimizer.prompt_optimizer import PromptOptimizer


class InferenceEngine:

    def __init__(self):

        self.client = OllamaClient()

        self.optimizer = PromptOptimizer()

    def process(self, prompt):

        optimized_prompt = self.optimizer.optimize(prompt)

        return self.client.generate(optimized_prompt)

    def process_stream(self, prompt):

        optimized_prompt = self.optimizer.optimize(prompt)

        return self.client.generate_stream(
            optimized_prompt
        )