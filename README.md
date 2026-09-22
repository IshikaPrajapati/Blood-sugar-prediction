# Blood Sugar Level Prediction using Machine Learning

A **Machine Learning web application** that predicts blood sugar levels using **Linear Regression** based on health and lifestyle-related input features.

> **Disclaimer:** This project is created for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used for medical decisions.

---

## 📌 Project Overview

The **Blood Sugar Level Prediction** project uses a Linear Regression model to estimate blood sugar levels in **mg/dL**.

The model takes 8 input features:

* Age
* BMI
* Physical Activity
* Sleep Hours
* Stress Level
* Daily Carbohydrate Intake
* Family History
* Previous Glucose Level

The trained model is connected to a **Flask backend** and a modern HTML/CSS/JavaScript frontend.

The user enters the required information through the web interface, and the Flask backend sends the data to the trained ML model. The predicted blood sugar level is then displayed on the frontend.

---

## ✨ Features

* 🤖 Machine Learning prediction using Linear Regression
* 🩸 Blood sugar level prediction in mg/dL
* 🌐 Flask backend
* 🎨 Modern responsive frontend
* 📊 8 health and lifestyle input features
* ⚡ Real-time prediction through API
* 📱 Responsive design for different screen sizes
* 🔄 Actual vs Predicted visualization during model evaluation
* 📈 Model performance metrics
* 🧪 Educational synthetic dataset

---

## 🧠 Machine Learning Model

### Algorithm

**Linear Regression**

Linear Regression is used to predict a continuous numerical value based on multiple input features.

### Target Variable

```text
Blood_Sugar_mg_dL
```

### Input Features

| Feature               | Description                        |
| --------------------- | ---------------------------------- |
| Age                   | Age of the person                  |
| BMI                   | Body Mass Index                    |
| Physical_Activity_Min | Physical activity in minutes/day   |
| Sleep_Hours           | Average sleep duration             |
| Stress_Level          | Stress level from 1–10             |
| Daily_Carb_Intake_g   | Daily carbohydrate intake in grams |
| Family_History        | 0 = No, 1 = Yes                    |
| Previous_Glucose      | Previous glucose level in mg/dL    |

---

## 📊 Model Performance

The model was evaluated using a test dataset.

| Metric   |           Result |
| -------- | ---------------: |
| MAE      | **4.0194 mg/dL** |
| MSE      |      **26.1369** |
| RMSE     | **5.1124 mg/dL** |
| R² Score |       **0.8751** |

### What these metrics mean

* **MAE:** Average absolute difference between actual and predicted values.
* **MSE:** Average squared prediction error.
* **RMSE:** Measures prediction error in the same unit as blood sugar.
* **R² Score:** Shows how well the model explains the variation in the target variable.

---

## 🗂️ Project Structure

All project files are kept in the same folder:

```text
BloodSugarPrediction/
│
├── app.py
├── index.html
├── blood_sugar_model.pkl
└── README.md
```

### File Description

**`app.py`**

Flask backend that:

* Loads the trained model
* Receives input from the frontend
* Performs prediction
* Returns the prediction as JSON

**`index.html`**

Frontend containing:

* Input form
* CSS styling
* JavaScript
* Prediction result section

**`blood_sugar_model.pkl`**

Saved Linear Regression model.

**`README.md`**

Project documentation.

---

## 🔄 Project Workflow

```text
User Input
    ↓
HTML Form
    ↓
JavaScript
    ↓
POST /predict
    ↓
Flask Backend
    ↓
Load ML Model
    ↓
Linear Regression Prediction
    ↓
Predicted Blood Sugar
    ↓
JSON Response
    ↓
Frontend Result
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Model Saving

* Joblib

---

## 📦 Installation

Make sure Python is installed on your system.

### 1. Open the project folder

Open PowerShell or Command Prompt inside the project folder.

### 2. Install required libraries

```bash
pip install flask pandas scikit-learn joblib
```

If `pip` doesn't work, use:

```bash
python -m pip install flask pandas scikit-learn joblib
```

---

## ▶️ Run the Application

Run:

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

> Do not open `index.html` directly. The frontend should be accessed through the Flask server.

---

## 🔌 API Endpoint

### Prediction API

```text
POST /predict
```

The frontend sends JSON data containing the 8 model features.

Example:

```json
{
    "Age": 25,
    "BMI": 22.5,
    "Physical_Activity_Min": 45,
    "Sleep_Hours": 7,
    "Stress_Level": 4,
    "Daily_Carb_Intake_g": 200,
    "Family_History": 0,
    "Previous_Glucose": 95
}
```

The backend returns:

```json
{
    "success": true,
    "prediction": 98.42
}
```

---

## 🧪 Dataset

The project uses a **synthetic dataset** containing 500 records.

The dataset includes lifestyle and health-related features such as:

* Age
* BMI
* Physical activity
* Sleep
* Stress
* Carbohydrate intake
* Family history
* Previous glucose

The dataset is intended for **machine learning practice and demonstration**, not for clinical research.

---

## 📈 Model Development

The machine learning workflow followed these steps:

```text
1. Dataset Creation
       ↓
2. Data Exploration
       ↓
3. Data Visualization
       ↓
4. Correlation Analysis
       ↓
5. Feature Selection
       ↓
6. Train-Test Split
       ↓
7. Linear Regression Training
       ↓
8. Prediction
       ↓
9. Model Evaluation
       ↓
10. Model Saving
       ↓
11. Flask Integration
```

---

## 📊 Evaluation Visualization

The project also uses an **Actual vs Predicted Blood Sugar** plot to visually compare the model's predictions with the actual test values.

The closer the points are to the diagonal reference line, the closer the predictions are to the actual values.

---

## 🌐 Web Application

The frontend provides fields for all eight model inputs.

After submitting the form:

```text
Input Data
     ↓
JavaScript Fetch Request
     ↓
Flask /predict API
     ↓
ML Model
     ↓
Prediction
     ↓
Result displayed on webpage
```

---

## ⚠️ Disclaimer

This application is an **educational machine learning project**.

The predictions are generated from a synthetic dataset and a Linear Regression model. The application:

* Is not a medical device.
* Does not diagnose diabetes or other medical conditions.
* Should not be used to make medical decisions.
* Should not replace professional medical advice.

---

## 🚀 Future Improvements

Possible improvements include:

* Use a larger real-world dataset
* Compare Linear Regression with other ML algorithms
* Add data preprocessing pipelines
* Add feature scaling where appropriate
* Add model comparison
* Add prediction history
* Add database integration
* Add user authentication
* Deploy the application online
* Add model monitoring
* Improve UI/UX
* Add more detailed model analysis

---

## 👩‍💻 Author

**Ishika Prajapati**

Computer Science & Engineering
Machine Learning | Data Science | Data Analytics

---

## ⭐ Project Purpose

This project demonstrates the complete process of building and deploying a basic machine learning application:

**Dataset → EDA → Model Training → Evaluation → Model Saving → Flask API → Web Frontend → Prediction**

