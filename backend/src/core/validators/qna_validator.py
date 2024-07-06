from sentence_transformers import CrossEncoder
 
model = CrossEncoder('cross-encoder/qnli-electra-base')
scores = model.predict([('Query1', 'Paragraph1'), ('Query2', 'Paragraph2')])

def is_qna_match(question: str,answer:str) -> bool:
    scores = model.predict([(question,answer)])
    print(scores)
    if scores>0.5:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f"Message is {is_qna_match('How many people live in Berlin?','10 people')}")
    print(f"Message is {is_qna_match('What is the size of New York?','My name is Gayuni')}")