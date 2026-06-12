# Forest Fire Prediction Using Machine Learning

## Project Overview

This project predicts the Fire Weather Index (FWI) using a Ridge Regression Machine Learning model. The model is trained on the Algerian Forest Fires dataset and deployed using Flask.

The application allows users to enter weather and environmental conditions through a web interface and obtain a predicted Fire Weather Index value.

---

## Features

The model uses the following input features:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC (Fine Fuel Moisture Code)
* DMC (Duff Moisture Code)
* ISI (Initial Spread Index)
* Classes
* Region

### Target Variable

* FWI (Fire Weather Index)

---

## Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-Learn
* HTML
* CSS
* Pickle

---

## Project Structure

```text
Forest_Fire_Prediction/

├── Notes_And_Datasets/
│   ├── 1.Cleaning.ipynb
│   ├── 2.Exploratory_Data_Analysis.ipynb
│   ├── 3.Feature_selection_&_Model_Training.ipynb
│   ├── Algerian_forest_fires_Cleaned_dataset.csv
│   ├── Algerian_forest_fires_dataset_UPDATE.csv
│   ├── ridge_mode.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── index.html
│   └── predictdata.html
│
├── application.py
└── README.md
```

---

## Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Selection
4. Data Standardization
5. Ridge Regression Model Training
6. Model Serialization using Pickle
7. Flask Web Application Deployment

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
python application.py
```

---

## Access the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Sample Input

| Feature     | Value |
| ----------- | ----- |
| Temperature | 29    |
| RH          | 74    |
| Ws          | 19    |
| Rain        | 0.1   |
| FFMC        | 75.8  |
| DMC         | 3.6   |
| ISI         | 2.1   |
| Classes     | 0     |
| Region      | 0     |

---

## Output

Predicted Fire Weather Index (FWI)

---

## Future Enhancements

* Deploy on Render or Heroku
* Add data visualization dashboard
* Support multiple machine learning models
* Improve UI/UX design

---

## Author

T N Perarasan

Machine Learning Project using Flask and Scikit-Learn.
