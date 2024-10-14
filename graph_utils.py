import networkx as nx
import re
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Initialize the QA model and tokenizer
model_name = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

def create_knowledge_graph(entities):
    G = nx.Graph()
    for entity in entities:
        G.add_node(entity['word'], type=entity['entity'])
    # Example edges (you may want to implement a more sophisticated method)
    edges = [
        ("World War II", "Germany", "involved"),
        ("World War II", "Allied Powers", "opposed"),
        ("Germany", "Adolf Hitler", "led by"),
        ("Allied Powers", "United States", "included"),
        ("Allied Powers", "Soviet Union", "included"),
        ("Allied Powers", "United Kingdom", "included"),
        ("World War II", "1939", "started in"),
        ("World War II", "1945", "ended in"),
        ("World War II", "Holocaust", "included"),
        ("World War II", "Atomic Bomb", "ended with")
    ]
    G.add_edges_from((s, t, {"relation": r}) for s, t, r in edges)
    return G

def strip_tags(text):
    return re.sub('<[^<]+?>', '', text)

def qa_pipeline(question, context):
    inputs = tokenizer(question, context, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    answer_start = outputs.start_logits.argmax()
    answer_end = outputs.end_logits.argmax() + 1
    answer = tokenizer.decode(inputs["input_ids"][0][answer_start:answer_end])
    return {"answer": answer}

def extract_answer(query, context, full_response):
    keywords = {
        "who": ["led", "commanded"],
        "what": ["involved", "included", "started", "ended"],
        "where": ["occurred", "took place"],
        "when": ["started", "ended", "occurred"]
    }
    question_type = next((word for word in keywords if word in query.lower()), None)

    if question_type:
        sentences = re.split(r'(?<=[.!?])\s+', context)
        relevant_sentences = [s for s in sentences if any(keyword in s.lower() for keyword in keywords[question_type])]
        if not relevant_sentences:
            return full_response
        new_context = " ".join(relevant_sentences)
        try:
            new_response = qa_pipeline(query, new_context)
            return new_response['answer']
        except Exception as e:
            print(f"Error in QA pipeline: {e}")
            return full_response
    return full_response

def generate_response(query, graph):
    try:
        context = " ".join([f"{node} {graph[node][neighbor]['relation']} {neighbor}."
                            for node in graph.nodes()
                            for neighbor in graph[node]])

        initial_response = qa_pipeline(query, context)
        detailed_answer = extract_answer(query, context, initial_response['answer'])

        # Ensure the answer is at least one complete sentence
        sentences = re.split(r'(?<=[.!?])\s+', context)
        for sentence in sentences:
            if detailed_answer.lower() in sentence.lower():
                return strip_tags(sentence.strip())

        # If no matching sentence is found, return the original answer
        return strip_tags(detailed_answer)

    except Exception as e:
        return f"An error occurred while generating the response: {str(e)}"
