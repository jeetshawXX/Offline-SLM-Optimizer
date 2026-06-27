from services.ollama_client import OllamaClient
from optimizer.prompt_optimizer import PromptOptimizer
from memory.conversation_memory import ConversationMemory


class InferenceEngine:

    def __init__(self):

        self.client = OllamaClient()

        self.optimizer = PromptOptimizer()

        self.memory = ConversationMemory()

    def process(self, prompt):

        # Get previous conversation
        context = self.memory.get_context()

        # Build the complete prompt
        full_prompt = f"""
Previous Conversation:

{context}

Current Question:

{prompt}
"""

        # Optimize prompt
        optimized_prompt = self.optimizer.optimize(full_prompt)

        # Generate answer
        response = self.client.generate(optimized_prompt)

        # Save conversation
        self.memory.add_message("User", prompt)
        self.memory.add_message("Assistant", response)

        return response

    def process_stream(self, prompt):

        context = self.memory.get_context()

        full_prompt = f"""
Previous Conversation:

{context}

Current Question:

{prompt}
"""

        optimized_prompt = self.optimizer.optimize(full_prompt)

        return self.client.generate_stream(
            optimized_prompt
        )