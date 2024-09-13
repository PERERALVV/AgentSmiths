def count_words(message: str) -> int:
    return len(message.split())

if __name__ == "__main__":
    text = 'Hello we are AgentSmiths and we build websites'
    print(f"Word Count: {count_words(text)}")