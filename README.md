{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# GraphRAG QA Agent Setup Guide\n",
    "\n",
    "This notebook will guide you through the setup and usage of the GraphRAG QA Agent."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Environment Setup\n",
    "\n",
    "First, let's install the required packages:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -r requirements.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Importing Required Modules"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from wikipedia_utils import get_wikipedia_page\n",
    "from graph_utils import create_knowledge_graph, generate_response\n",
    "from nlp_utils import extract_entities_and_relationships, evaluate_response\n",
    "import networkx as nx\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Extracting Wikipedia Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "title = \"World War II\"\n",
    "text = get_wikipedia_page(title)\n",
    "print(f\"Extracted {len(text)} characters from Wikipedia\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Entity Extraction and Knowledge Graph Creation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "entities = extract_entities_and_relationships(text)\n",
    "G = create_knowledge_graph(entities)\n",
    "print(f\"Created a graph with {len(G.nodes)} nodes and {len(G.edges)} edges\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Visualizing the Knowledge Graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(12, 8))\n",
    "pos = nx.spring_layout(G)\n",
    "nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_weight='bold')\n",
    "edge_labels = nx.get_edge_attributes(G, 'relation')\n",
    "nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)\n",
    "plt.title(\"Knowledge Graph for World War II\")\n",
    "plt.axis('off')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Question Answering"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "queries = [\n",
    "    \"Who was the primary leader of Nazi Germany during World War II?\",\n",
    "    \"Which major powers were involved in World War II?\",\n",
    "    \"In what year did World War II begin in Europe?\",\n",
    "    \"When did World War II officially come to an end?\",\n",
    "    \"What was the systematic genocide of European Jews during World War II called?\"\n",
    "]\n",
    "\n",
    "for query in queries:\n",
    "    response = generate_response(query, G)\n",
    "    print(f\"Query: {query}\")\n",
    "    print(f\"Response: {response}\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Customization\n",
    "\n",
    "You can customize the GraphRAG QA Agent by modifying the following:\n",
    "\n",
    "1. Change the `title` variable to extract information about a different topic.\n",
    "2. Add more sophisticated edge creation logic in the `create_knowledge_graph` function.\n",
    "3. Experiment with different NER or QA models by modifying the respective model names in `nlp_utils.py` and `graph_utils.py`."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
