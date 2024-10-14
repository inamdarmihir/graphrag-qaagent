# GraphRAG QA Agent

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

GraphRAG QA Agent is an advanced question-answering system that combines knowledge graph technologies with state-of-the-art natural language processing models. This system is designed to extract information from Wikipedia, create a knowledge graph, and answer user queries based on the constructed graph.

## Features

- Wikipedia data extraction
- Named Entity Recognition (NER) for entity extraction
- Knowledge graph construction
- Question-answering capabilities
- Semantic similarity evaluation of responses

## Requirements

- Python 3.8+
- PyTorch 1.13.1
- Transformers 4.30.2
- NetworkX 3.3
- Scikit-learn 1.0.2
- Wikipedia-API 0.7.1

For a complete list of requirements, please refer to the `requirements.txt` file.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/graphrag-qaagent.git
   cd graphrag-qaagent
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Project Structure

```
graphrag-qaagent/
│
├── main.py                 # Main script to run the QA system
├── wikipedia_utils.py      # Utilities for Wikipedia data extraction
├── graph_utils.py          # Functions for knowledge graph creation and querying
├── nlp_utils.py            # NLP-related functions (NER, semantic similarity)
├── requirements.txt        # List of required Python packages
├── README.md               # This file
└── GraphAgent_Setup.ipynb  # Jupyter notebook for setup and demonstration
```

## Usage

To use the GraphRAG QA Agent, follow these steps:

1. Ensure you have installed all required dependencies (see [Installation](#installation)).

2. Run the main script:
   ```
   python main.py
   ```

3. The script will:
   - Extract information about World War II from Wikipedia
   - Create a knowledge graph based on the extracted information
   - Process a set of predefined queries
   - Generate and evaluate responses for each query

4. You can modify the `queries` list in `main.py` to ask your own questions about World War II.

## GraphAgent_Setup.ipynb

We provide a Jupyter notebook `GraphAgent_Setup.ipynb` as a setup guide and interactive demonstration of the GraphRAG QA Agent. This notebook covers:

1. Environment setup and package installation
2. Step-by-step explanation of each component
3. Interactive examples of knowledge graph creation
4. Demonstration of the question-answering process
5. Visualization of the knowledge graph

To use the notebook:

1. Ensure you have Jupyter installed:
   ```
   pip install jupyter
   ```

2. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```

3. Open `GraphAgent_Setup.ipynb` in your browser and follow the instructions within the notebook.

## Customization

You can customize the GraphRAG QA Agent in several ways:

1. **Change the topic**: Modify the `title` variable in `main.py` to extract information about a different Wikipedia topic.

2. **Extend the knowledge graph**: Add more sophisticated edge creation logic in the `create_knowledge_graph` function in `graph_utils.py`.

3. **Improve NER**: Fine-tune the NER model or use a different pre-trained model by modifying the `ner_model_name` in `nlp_utils.py`.

4. **Enhance question-answering**: Experiment with different QA models by changing the `model_name` in `graph_utils.py`.

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed and versions match those in `requirements.txt`.
2. Check for any error messages in the console output.
3. Verify that you have a stable internet connection for Wikipedia data extraction.
4. If you're having GPU-related issues, try running the system on CPU by modifying the device settings in the code.

## Contributing

We welcome contributions to the GraphRAG QA Agent! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information or support, please open an issue in the GitHub repository.
