# Mastering the AI Toolkit 🛠️🧠

[![CI](https://github.com/<nicanornicolas>/ai-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/<nicanornicolas>/ai-toolkit/actions/workflows/ci.yml)

This repository contains the work for the "Mastering the AI Toolkit" assignment. Our team collaborated to explore theoretical concepts, implement practical machine learning models, and analyze the ethical implications of AI.

## Repository Structure
ai-toolkit/
├─ part1_theory/
│  ├─ outline.md
│  └─ references.bib
├─ part2_practical/
│  ├─ task1_iris_sklearn/
│  │  ├─ iris_classifier.ipynb
│  │  └─ iris_utils.py
│  ├─ task2_mnist_cnn/
│  │  ├─ mnist_cnn.ipynb
│  │  ├─ train.py
│  │  └─ models/
│  └─ task3_spacy_reviews/
│     ├─ spacy_ner_sentiment.ipynb
│     └─ rules.py
├─ bonus_app/
│  ├─ app.py
│  └─ requirements.txt
├─ report/
│  ├─ report_outline.md
│  └─ ethics_and_optimization.md
├─ deliverables/
│  ├─ .gitkeep
│  ├─ final_report.pdf
│  └─ presentation_video_link.txt
├─ data/               # .gitignore large/raw files; include small samples
│  └─ .gitkeep
├─ tests/
│  ├─ test_iris.py
│  ├─ test_mnist.py
│  └─ test_spacy.py
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  └─ task.yml
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/
│     └─ ci.yml
├─ .gitignore
├─ Makefile
├─ requirements.txt
└─ README.md
## Overview
Brief summary of project goals and components.

## Quickstart

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<YOUR_USERNAME>/ai-toolkit.git
    cd ai-toolkit
    ```

2.  **Set up the environment and install dependencies:**
    This project uses a `Makefile` for convenience.
    ```bash
    make setup
    ```
    This will create a virtual environment `./.venv` and install all required packages.

3.  **Activate the environment:**
    ```bash
    source .venv/bin/activate
    ```

## How to Run Our Work

-   **Part 1 (Theory):** The analysis is in the [Final Report](deliverables/final_report.pdf).
-   **Part 2.1 (Iris Classifier):** Open and run the notebook: `part2_practical/task1_iris_sklearn/iris_classifier.ipynb`
-   **Part 2.2 (MNIST CNN):** Open and run the notebook: `part2_practical/task2_mnist_cnn/mnist_cnn.ipynb`
-   **Part 2.3 (spaCy NLP):** Open and run the notebook: `part2_practical/task3_spacy_reviews/spacy_ner_sentiment.ipynb`
-   **Bonus App:**
    ```bash
    streamlit run bonus_app/app.py
    ```

## Deliverables

-   **[Final Report](deliverables/final_report.pdf):** Our comprehensive report including theoretical answers, practical results, and ethical analysis.
-   **[Presentation Video](deliverables/presentation_video_link.txt):** A link to our 3-minute video presentation.
-   **Bonus Web App Live Demo:** [Link will be here]

## Team Members & Roles

-   **Team Leader / Project Manager:** Nicanor Nicolas
-   **Theory & Documentation Lead:** Team Member A
-   **Classical ML Lead (Scikit-learn):** Team Member B
-   **Deep Learning Lead (TensorFlow/PyTorch):** Team Member C
-   **NLP Lead (spaCy):** Team Member D
-   **Deployment Engineer (Bonus Task):** Nicanor Nicolas
