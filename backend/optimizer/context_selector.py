class ContextSelector:
    """
    Selects the most relevant conversation history.
    Version 1: Keep only the last N messages.
    """

    def __init__(self, max_messages=4):
        self.max_messages = max_messages

    def select(self, history):

        if len(history) <= self.max_messages:
            return history

        return history[-self.max_messages:]