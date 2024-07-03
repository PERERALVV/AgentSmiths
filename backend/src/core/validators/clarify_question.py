import importlib
import re

# Import the Ggemini class
gemini_module = importlib.import_module('routes.llm')
gemini = getattr(gemini_module, 'Ggemini')()

def remove_formatting(text: str) -> str:
    # Remove ** and * used for bold or italic formatting
    clean_text = re.sub(r'\*\*|[*]', '', text)
    return clean_text

# Define the get_clarification function
def get_clarification(message: str) -> str:
    clarification_prompt = f"Provide a brief clarification for this question: {message}"
    response = gemini.chatGemini(clarification_prompt)
    clean_response = remove_formatting(response)
    return clean_response


if __name__ == "__main__":
    pass
