import torch
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the NER pipeline
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")

def extract_entities_and_relationships(text):
    try:
        return ner_pipeline(text[:10000])  # Limit text to avoid memory issues
    except Exception as e:
        print(f"Error in NER: {e}")
        return []

def get_sentence_embedding(sentence, model, tokenizer):
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def evaluate_response(query, response, model, tokenizer):
    query_embedding = get_sentence_embedding(query, model, tokenizer)
    response_embedding = get_sentence_embedding(response, model, tokenizer)

    relevance_score = cosine_similarity([query_embedding], [response_embedding])[0][0]

    return relevance_score
