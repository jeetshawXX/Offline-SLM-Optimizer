from collections import deque


class ConversationMemory:

    def __init__(self, max_messages=20):
        self.history = deque(maxlen=max_messages)

    def add_message(self, role, content):

        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self):

        return list(self.history)

    def clear(self):

        self.history.clear()