from sentence_transformers import CrossEncoder
# from backend.app import get_message

# Initialize the CrossEncoder model with the desired model name
model = CrossEncoder('cross-encoder/qnli-electra-base')

# Define the queries and paragraphs for which you want to predict scores
query_paragraph_pairs = [
    ('How many people live in Berlin?', 'Berlin is beautiful.'),
    ('What is your name?', 'Hi I am Nimal.'),
]

# Predict scores for each query-paragraph pair
scores = model.predict(query_paragraph_pairs)

# Print the scores
for i, score in enumerate(scores):
    print(f"Score for pair {i+1}: {score:.4f}")

