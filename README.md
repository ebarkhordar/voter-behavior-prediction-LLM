# Voter Behavior Prediction Using Large Language Models

## About

This repository explores the application of large language models (LLMs) to predict voter behavior based on social media data. By integrating demographic data with tweets, this study assesses how different LLMs perform in predicting voter preferences, focusing on the importance of data diversity for enhancing accuracy and minimizing biases. The repository includes all necessary resources to replicate our findings and further explore LLMs' potential in social science.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Using Google Colab](#using-google-colab)
- [Dataset](#dataset)
- [Notebooks](#notebooks)
- [Results](#results)
- [Utils](#utils)
- [License](#license)

## Installation

### Prerequisites

- Python 3.10 or higher
- A virtual environment tool (e.g., venv, virtualenv, conda)

### Setup

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/voter-behavior-prediction-LLM.git
   cd voter-behavior-prediction-LLM
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   # Using conda as an example
   conda create --name myenv python=3.10
   conda activate myenv
   pip install -r requirements.txt
   ```

3. Open the notebooks in Jupyter or run them in Google Colab for optimal performance:
   ```bash
   jupyter notebook notebooks/<notebook_name>.ipynb
   ```

## Using Google Colab

To use Google Colab, simply upload the notebooks and dataset files (both `tweets_data.json` and `survey.xlsx`) to your Google Drive. Modify the path in the notebooks to reflect the dataset's location:

```python
%cd /path/to/voter-behavior-prediction-LLM
```

Run the notebooks directly in Colab without any installation required. Ensure you place your OpenAI API token in the `.env` file located in the same directory as `tweets_data.json` to access the models.

## Dataset

This project utilizes survey data and tweets for analysis. Access the survey data in `dataset/survey.xlsx`. For tweet data, please request access through [this Google Drive link](https://drive.google.com/file/d/1tnUMC6_q0f6ZB9kQJsNBUbpV1j_Q7I9c/view?usp=sharing). The dataset also uses auxiliary files like `utils/city_codes.txt` for data transformation.

## Notebooks

- `notebooks/survey.ipynb`: Main notebook for data preprocessing, prompt creation, results retrieval, and storage.
- `notebooks/analysis.ipynb`: Analyzes collected data and model predictions.
- `notebooks/evaluate.ipynb`: Evaluates model performance.

## Results

Detailed results from various LLMs are stored in the `results` directory:
- Davinci-002 results: `results/results_davinci-002_20240519162857.json`
- GPT-3.5 Turbo results: `results/results_gpt-3.5-turbo-0125_20240519153306.json`
- GPT-4 results: `results/results_gpt-4o-2024-05-13_20240519155949.json`

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.

