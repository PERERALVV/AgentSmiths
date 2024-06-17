from sentence_transformers import SentenceTransformer, util
import numpy as np

# Initialize the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Define domain-related sentences for comparison
domain_sentences = [
    "I need a website for my new business.",
    "How do I create a backend using Django?",
    "Can you help me with CSS styling?",
    "What are the best practices for SEO?",
    "How do I develop a responsive web design?"
]

# Generate embeddings for the domain-related sentences
domain_embeddings = model.encode(domain_sentences)

# Define a function to check if a sentence is within the domain
def is_within_domain(sentence, domain_embeddings, model, threshold=0.6):
    """
    Check if a sentence is within the specified domain based on semantic similarity.
    
    Args:
    - sentence (str): The input sentence to classify.
    - domain_embeddings (np.array): Array of embeddings for domain sentences.
    - model (SentenceTransformer): The sentence transformer model for encoding sentences.
    - threshold (float): Similarity threshold to consider the sentence as within the domain.
    
    Returns:
    - bool: True if the sentence is classified within the domain, False otherwise.
    """
    # Generate embedding for the input sentence
    sentence_embedding = model.encode(sentence)

    # Compute cosine similarity between the input sentence and the domain sentences
    cosine_scores = util.cos_sim(sentence_embedding, domain_embeddings)
    
    # Check if any similarity score exceeds the threshold
    max_score = np.max(cosine_scores.numpy())
    return max_score >= threshold

# Example usage
sentences = [
    "I need a website for my new business.",
    "How do I create a backend using Django?",
    "What's the weather like today?",
    "Can you help me with CSS styling?",
    "What are the best practices for SEO?"
]

for sentence in sentences:
    in_domain = is_within_domain(sentence, domain_embeddings, model)
    if in_domain:
        print(f"Sentence: '{sentence}'\nIs within domain: {in_domain}\n")
    else:
        print("Your response is not applicable to our domain. Please assist us to get a clear understanding about your web requirements")
        print("__message__")
