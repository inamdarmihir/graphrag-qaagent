import torch
from transformers import AutoTokenizer, AutoModel
from wikipedia_utils import get_wikipedia_page
from graph_utils import create_knowledge_graph, generate_response
from nlp_utils import extract_entities_and_relationships, evaluate_response

def main():
    title = "World War II"
    text = get_wikipedia_page(title)

    if text:
        entities = extract_entities_and_relationships(text)
        G = create_knowledge_graph(entities)

        # Load BERT model for semantic similarity
        model_name = "bert-base-uncased"
        model = AutoModel.from_pretrained(model_name)
        bert_tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Define your queries
        queries = [
            "Who was the primary leader of Nazi Germany during World War II?",
            "Which major powers were involved in World War II?",
            "In what year did World War II begin in Europe?",
            "When did World War II officially come to an end?",
            "What was the systematic genocide of European Jews during World War II called?"
        ]

        total_score = 0

        # Process each query
        for query in queries:
            print(f"Query: {query}")
            response = generate_response(query, G)
            print(f"Response: {response}")

            score = evaluate_response(query, response, model, bert_tokenizer)
            print(f"Score: {score:.2f}\n")

            total_score += score

        average_score = total_score / len(queries)
        print(f"Average Score: {average_score:.2f}")

    else:
        print(f"Failed to retrieve Wikipedia page for {title}")

if __name__ == "__main__":
    main()
