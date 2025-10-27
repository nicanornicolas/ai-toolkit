# Mastering the AI Toolkit 🛠️🧠

[![CI](https://github.com/<YOUR_GITHUB_USERNAME>/ai-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR_GITHUB_USERNAME>/ai-toolkit/actions/workflows/ci.yml)

This repository is the final submission for the "Mastering the AI Toolkit" assignment. It showcases a comprehensive understanding and practical application of key AI frameworks including **Scikit-learn**, **TensorFlow**, and **spaCy**.

The project is structured into three main parts: theoretical analysis, practical implementation of machine learning models, and an examination of AI ethics. Additionally, a bonus web application was developed using **Streamlit** to demonstrate model deployment. Our team followed agile development practices, including version control with Git, feature branching, and automated testing with `pytest`.

## 📂 Repository Structure

The repository is organized to separate concerns, making it easy to navigate the theoretical, practical, and deliverable components of the project.

```bash
ai-toolkit/
├── .github/                # CI/CD and GitHub templates
├── bonus_app/              # Source code for the Streamlit web application
├── deliverables/           # Final PDF report and video presentation link
├── part1_theory/           # Markdown files with theoretical answers
├── part2_practical/        # Notebooks and refactored Python pipelines for ML tasks
│   ├── task1_iris_sklearn/
│   ├── task2_mnist_cnn/
│   └── task3_spacy_reviews/
├── tests/                  # Pytest scripts for our refactored ML pipelines
├── .gitignore
├── environment.yml         # Recommended: Conda environment definition
├── pyproject.toml          # Project configuration for package discovery
├── README.md               # You are here!
└── requirements.txt        # Alternative: pip requirements file

🛠️ Setup and Installation
Prerequisites
Git
Python 3.10+
Miniconda (Recommended)
Method 1 (Recommended): Using Conda
This is the most reliable method as it manages complex dependencies like CUDA for you.

1. Clone the repository:
git clone https://github.com/<YOUR_GITHUB_USERNAME>/ai-toolkit.git
cd ai-toolkit

2. Create and activate the Conda environment:
conda env create -f environment.yml
conda activate ai-toolkit-env

3. Install the project in editable mode:
This makes your project's modules (like part2_practical) importable for testing.
pip install -e .


Method 2 (Alternative): Using venv
If you prefer not to use Conda, you can use Python's built-in venv.
1. Clone the repository and navigate into it. (See step 1 above)
2. Create and activate the virtual environment:
- On macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

- On Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

3. Install dependencies and the project:
pip install -r requirements.txt
pip install -e .


🚀 Usage and Execution
1. Running the Tests
To verify that all the refactored machine learning pipelines are working correctly, run the test suite from the root directory:
pytest

2. Running the Practical Notebooks
The notebooks in part2_practical/ demonstrate our model development process.
Important: When opening a notebook, ensure you select the correct kernel (ai-toolkit-env if using Conda, or .venv if using venv).
Iris Classifier: part2_practical/task1_iris_sklearn/iris_classifier.ipynb
MNIST CNN: part2_practical/task2_mnist_cnn/mnist_cnn.ipynb
spaCy NLP: part2_practical/task3_spacy_reviews/spacy_ner_sentiment.ipynb

3. Running the Bonus Web App
To launch the interactive MNIST digit classifier demo, run the following command from the root directory:
streamlit run bonus_app/app.py

streamlit run bonus_app/app.py
📄 Deliverables
All final submission materials are located in the deliverables/ folder.
Final Report: Read our Comprehensive Report, which includes all theoretical answers, practical results, and our ethical analysis.
Presentation Video: Watch our 3-Minute Presentation for a quick overview of our project and approach.
Bonus Web App (Live Demo): Try the App Live! (Link to be added upon deployment)

👥 Team Members and Roles
Team Leader / Project Manager: Nicanor Nicolas
Theory & Documentation Lead: Amy Marshall
Classical ML Lead (Scikit-learn): Khadeeja Mohammed
Deep Learning Lead (TensorFlow): KingLee
NLP Lead (spaCy): LeonMwangi
Deployment Engineer (Bonus App): Nicanor Nicolas