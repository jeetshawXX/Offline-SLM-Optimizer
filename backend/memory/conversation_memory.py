from collections import deque


class ConversationMemory:
    """
    Stores the conversation history between the user and the AI.
    """

    def __init__(self, max_messages=10):
        self.history = deque(maxlen=max_messages)

    def add_message(self, role: str, content: str):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_context(self) -> str:
        """
        Returns the complete conversation as text.
        """

        if not self.history:
            return ""

        context = ""

        for message in self.history:
            context += f"{message['role']}: {message['content']}\n"

        return context

    def clear(self):
        self.history.clear()