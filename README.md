# ❤️ Heart Disease Prediction using Machine Learning

## Overview
This project predicts whether a person has heart disease based on medical attributes using Machine Learning.  
It was developed as part of the **YBI Foundation Internship Program**.

## Objective
To train a classification model that can identify heart disease risk using patient health data.

## Dataset
Dataset used: [Heart Disease UCI Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Flask (Web Deployment)
- HTML/CSS

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the model notebook to generate `model.pkl`:
   ```bash
   jupyter notebook heart_disease.ipynb
   ```

4. Start the Flask app:
   ```bash
   python app.py
   ```

5. Open browser and visit: `http://127.0.0.1:5000/`

## Model Performance
| Metric | Score |
|--------|-------|
| Accuracy | ~88% |
| Precision | 0.87 |
| Recall | 0.86 |

## Created by:
**Rahul Yadav**  
YBI Foundation Internship Project
