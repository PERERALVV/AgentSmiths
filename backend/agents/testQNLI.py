from sentence_transformers import CrossEncoder
# from backend.app import get_message

# Initialize the CrossEncoder model with the desired model name
model = CrossEncoder('cross-encoder/qnli-electra-base')

#Get the message sent through the frontend
# message = get_message()  # Call the function to retrieve the message value
# print(message)

# Define the queries and paragraphs for which you want to predict scores
query_paragraph_pairs = [
    ('How many people live in Berlin?', 'Berlin is beautiful.'),
    ('What is your name?', 'Hi I am Nimal.'),
    # ('What is your name?', message),  # Append the received message here
    # ('How old are you?', message),  # Append the received message here
    # ('Where do you live?', message),  # Append the received message here
]

# Predict scores for each query-paragraph pair
scores = model.predict(query_paragraph_pairs)

# Print the scores
for i, score in enumerate(scores):
    print(f"Score for pair {i+1}: {score:.4f}")

