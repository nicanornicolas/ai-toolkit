<!-- This file contains the written answers for Part 1 of the assignment. -->

# Mastering the AI Toolkit: Part 1 - Theoretical Understanding

## Short Answer Questions

### Q1: Primary difference between TensorFlow and PyTorch

*   **TensorFlow** uses a **static computation graph**, which requires you to define the entire model before running it. This makes it better for deployment and production environments.
    *(Choose it for large-scale, production-ready systems)*

*   **PyTorch** uses a **dynamic computation graph**, which builds the graph as code executes. This makes it easier to debug and experiment with.
    *(Choose it for research, rapid prototyping, and flexible model design)*

### Q2: Two uses of Jupyter Notebooks in AI development

*   **Interactive Experimentation:** Data scientists can write, test, and visualize AI code in real time, making it easier to debug and analyze results.

*   **Documentation and Reporting:** Jupyter Notebooks combine code, outputs, and explanations in one document, which is useful for creating tutorials, research reports, or presentations.

### Q3: How does spaCy enhance NLP tasks compared to basic Python string operations?

*   spaCy provides pre-trained language models that understand grammar, entities, and dependencies, enabling advanced NLP tasks like tokenization, POS tagging, and named entity recognition.

*   Basic Python string operations (like `.split()` or `.replace()`) only handle plain text and lack linguistic understanding.

*   Thus, spaCy offers faster, more accurate, and scalable text processing for NLP applications.

---

## Comparative Analysis

### Scikit-Learn vs. TensorFlow

| Aspect | Scikit-Learn | TensorFlow |
| :--- | :--- | :--- |
| **Target Applications** | Classical machine learning (e.g., regression, classification, clustering). | Deep learning and neural networks. |
| **Ease of use for Beginners** | Very easy to learn with simple APIs. | Steeper learning curve, more complex setup. |
| **Community Support** | Large and active for traditional ML. | Large and growing, especially in AI/deep learning fields. |