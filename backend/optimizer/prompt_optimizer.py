class PromptOptimizer:
    """
    Optimizes user prompts before sending them to the language model.
    """

    def optimize(self, prompt: str) -> str:
        """
        Convert a simple prompt into a structured prompt.
        """

        optimized_prompt = f"""
You are a helpful AI assistant.

Answer the following question clearly.

Question:
{prompt}

Instructions:
- Give a simple explanation.
- Use headings if necessary.
- Give examples whenever possible.
- Keep the answer accurate.
- End with a short summary.
"""

        return optimized_prompt.strip()