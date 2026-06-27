from services.ollama_client import OllamaClient
from optimizer.prompt_optimizer import PromptOptimizer
from optimizer.context_selector import ContextSelector
from memory.conversation_memory import ConversationMemory


class InferenceEngine:

    def __init__(self):

        self.client = OllamaClient()

        self.optimizer = PromptOptimizer()

        self.memory = ConversationMemory()

        self.selector = ContextSelector()

    def build_context(self, selected_messages):

        context = ""

        for message in selected_messages:

            context += f"{message['role']}: {message['content']}\n"

        return context

    def process(self, prompt):

        history = self.memory.get_history()

        selected = self.selector.select(history)

        context = self.build_context(selected)

        full_prompt = f"""
Previous Conversation:

{context}

Current Question:

{prompt}
"""

        optimized_prompt = self.optimizer.optimize(full_prompt)

        response = self.client.generate(optimized_prompt)

        self.memory.add_message("User", prompt)

        self.memory.add_message("Assistant", response)

        return response

    def process_stream(self, prompt):

        history = self.memory.get_history()

        selected = self.selector.select(history)

        context = self.build_context(selected)

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