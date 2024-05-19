# Voter Behavior Prediction Using Large Language Models

## Abstract

This article explores how large language models (LLMs) can reflect human preferences and exhibit biases based on the diversity and type of input data. Utilizing survey data linked with tweets, we compare the predictive performance and bias manifestations of LLMs under three different data inclusion strategies: (1) using only demographic information, (2) combining demographic information with tweets, and (3) exclusively using tweets. The study finds that prompts enriched with tweets notably improve the predictive accuracy of models compared to those relying solely on demographic data. More importantly, the inclusion of dynamic, user-generated content like tweets not only reduces the oversimplification of individual identities but also lessens inherent biases, leading to more accurate and representative simulations of voter behavior. These findings underscore the critical role of data variety in LLM-based simulations, suggesting that integrating richer, real-time data sources can effectively diminish biases and enhance the models' ability to simulate complex human characteristics.

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
## Citing This Work

If you find the content of this repository useful in your research, please cite the following paper:

```
@inproceedings{barkhordar2024assessing,
  title={Assessing the Predictive Power of Social Media Data-Fed Large Language Models on Voter Behavior},
  author={Barkhordar, Ehsan and Atsizelti, Şükrü},
  booktitle={Proceedings of the ACM Conference},
  year={2024},
  doi={10.1145/3630744.3659831}
}
```

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.
