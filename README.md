# GraphRAG QA Agent - Detailed Submission Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
7. [GraphAgent_Setup.ipynb](#graphagent_setupipynb)
8. [Customization](#customization)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction

The **GraphRAG QA Agent** is a sophisticated question-answering system that integrates knowledge graph techniques with cutting-edge natural language processing (NLP) models. This system is designed to extract data from Wikipedia, construct a knowledge graph, and provide accurate answers to user queries by referencing the constructed graph.

## Features

- **Wikipedia data extraction**: Retrieves relevant content directly from Wikipedia.
- **Named Entity Recognition (NER)**: Extracts key entities from text.
- **Knowledge graph construction**: Builds a graph of extracted information, linking related entities.
- **Question-answering functionality**: Processes and answers user questions based on the knowledge graph.
- **Semantic similarity evaluation**: Assesses and improves the relevance of generated responses.

## Requirements

To run this project, you will need the following dependencies:

- Python 3.8+
- PyTorch 1.13.1
- Transformers 4.30.2
- NetworkX 3.3
- Scikit-learn 1.0.2
- Wikipedia-API 0.7.1

For a complete list of all required packages, please refer to the `requirements.txt` file in the repository.

## Installation

Follow these steps to install and set up the GraphRAG QA Agent on your system:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/graphrag-qaagent.git
   cd graphrag-qaagent
   ```

2. **Create a virtual environment** (optional, but recommended for isolating dependencies):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project is organized as follows:

```
graphrag-qaagent/
│
├── main.py                 # Main script to execute the QA system
├── wikipedia_utils.py      # Functions for extracting data from Wikipedia
├── graph_utils.py          # Functions for building and querying the knowledge graph
├── nlp_utils.py            # Functions for NLP tasks like NER and semantic similarity
├── requirements.txt        # File listing the required Python packages
├── README.md               # Project documentation
└── GraphAgent_Setup.ipynb  # Jupyter notebook for setup and demonstration
```

## Usage

To use the GraphRAG QA Agent, follow the instructions below:

1. **Install dependencies** as outlined in the [Installation](#installation) section.

2. **Run the main script**:
   ```bash
   python main.py
   ```

Upon execution, the script will:

- Extract information related to *World War II* from Wikipedia.
- Construct a knowledge graph using the extracted data.
- Process a set of predefined queries.
- Generate responses to each query and evaluate them for accuracy.

3. **Modify the predefined queries**: 
   You can customize the list of questions by modifying the `queries` variable in `main.py` to ask your own questions, particularly on topics related to *World War II* or any other subject of interest.

## GraphAgent_Setup.ipynb

The **GraphAgent_Setup.ipynb** Jupyter notebook provides a guided, interactive demonstration of the GraphRAG QA Agent. It includes the following key sections:

1. **Environment Setup**: Guides through setting up dependencies.
2. **Component Overview**: Detailed explanation of the system's components.
3. **Knowledge Graph Creation**: Step-by-step instructions to create and visualize the knowledge graph.
4. **Question-Answering Demonstration**: Interactive examples that show the QA process.
5. **Graph Visualization**: Visual representation of the knowledge graph.

### Running the Notebook

1. **Install Jupyter** (if not already installed):
   ```bash
   pip install jupyter
   ```

2. **Launch the notebook**:
   ```bash
   jupyter notebook
   ```

3. **Open** the `GraphAgent_Setup.ipynb` file in your browser and follow the instructions.

## Customization

The GraphRAG QA Agent is highly customizable. Here are some suggestions for how to extend or modify the system:

1. **Change the topic**: Adjust the `title` variable in `main.py` to extract information on a different topic from Wikipedia.
   
2. **Extend the knowledge graph**: Modify the `create_knowledge_graph` function in `graph_utils.py` to implement more advanced logic for creating relationships between entities.

3. **Improve NER**: You can fine-tune the NER model or replace the current pre-trained model by changing the `ner_model_name` in `nlp_utils.py`.

4. **Enhance question-answering performance**: Try different QA models by modifying the `model_name` in `graph_utils.py` to suit your needs.

## Troubleshooting

If you encounter issues while using the GraphRAG QA Agent, consider the following troubleshooting steps:

1. **Dependency issues**: Ensure all dependencies are installed and match the versions specified in `requirements.txt`.
   
2. **Error messages**: Review the console output for detailed error messages and resolve any issues indicated.

3. **Internet connection**: Ensure you have a stable internet connection when extracting data from Wikipedia.

4. **GPU problems**: If you're facing GPU compatibility issues, try switching to CPU by adjusting the device settings in the code.

## Contributing

We welcome contributions to improve the GraphRAG QA Agent. To contribute:

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push the changes** to your branch:
   ```bash
   git push origin feature-branch
   ```
5. **Open a pull request**: Submit your changes by opening a Pull Request on GitHub.

## License

This project is licensed under the **MIT License**. For more details, refer to the [LICENSE](LICENSE) file included in the repository.

---

For further information, assistance, or to report any issues, please open an issue on the GitHub repository.
