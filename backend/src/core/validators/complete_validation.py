from core.validators.prompt_validator import is_message_legitimate
from core.validators.qna_validator import is_qna_match
from core.validators.summarize import message_summary
from core.validators.word_count import count_words

def complete_response_validation(user_message: str):
    if count_words(user_message)>20:
        user_message = message_summary(user_message)
        user_message = user_message.strip('"\'')
        print(f"summarized message : {user_message}")
    legitimacy = is_message_legitimate(user_message)
    return legitimacy, user_message

if __name__ == "__main__":
    pass
