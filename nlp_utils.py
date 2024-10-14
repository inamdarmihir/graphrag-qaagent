import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the NER model and tokenizer
ner_model_name = "dslim/bert-base-NER"
ner_tokenizer = AutoTokenizer.from_pretrained(ner_model_name)
ner_model = AutoModelForTokenClassification.from_pretrained(ner_model_name)

def extract_entities_and_relationships(text):
    try:
        inputs = ner_tokenizer(text[:10000], return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = ner_model(**inputs)
        
        predictions = torch.argmax(outputs.logits, dim=2)
        tokens = ner_tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
        
        entities = []
        for token, prediction in zip(tokens, predictions[0]):
            if prediction != 0:  # 0 is usually the 'O' (Outside) tag
                entity_type = ner_model.config.id2label[prediction.item()]
                entities.append({"word": token, "entity": entity_type})
        
        return entities
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
