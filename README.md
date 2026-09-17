# 🏠A House Price Predictor

An interactive **Machine Learning web application** that predicts house prices based on property characteristics such as **square footage, bedrooms, bathrooms, and property age**.

The application combines a trained regression model with a modern **Streamlit dashboard** and interactive **Plotly visualizations** to provide property valuation insights.

---

## 🎯 Project Overview

Estimating the value of a property depends on multiple factors.

This project demonstrates how **Machine Learning Regression** can be used to analyze housing information and generate an estimated property value.

Users enter property details through an interactive interface, and the trained ML model instantly generates a predicted price along with useful market analytics.

---

## ✨ Features

### 🤖 AI-Powered Price Prediction

Predict the estimated value of a property using inputs such as:

* 📐 Square Footage
* 🛏️ Number of Bedrooms
* 🚿 Number of Bathrooms
* 🏗️ Property Age

The prediction is generated using a pre-trained **Scikit-learn regression model**.

---

### 📊 Dynamic Valuation Gauge

Displays the predicted property value through an interactive gauge chart.

It helps visualize how the estimated value compares with the average market value.

---

### 📈 10-Year Valuation Trajectory

Provides a visual representation of:

* Historical property value
* Current estimated value
* Projected future valuation

This helps users understand potential property value trends.

---

### 🕸️ Property Radar Analysis

An interactive radar chart compares the selected property specifications with typical market characteristics.

Comparison factors include:

* Square Footage
* Bedrooms
* Bathrooms
* Property Age

---

### 💰 Property Analytics

The dashboard also calculates useful property metrics such as:

**Value per Square Foot**

```text
Predicted Property Value
────────────────────────
Total Square Footage
```

**Estimated Monthly Mortgage**

Provides an approximate monthly payment based on the predicted property value.

---

## 🧠 Machine Learning Workflow

```text
Housing Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Selection
      │
      ▼
Regression Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model using Joblib
      │
      ▼
Streamlit Application
      │
      ▼
User Property Details
      │
      ▼
House Price Prediction
```

---

## 🛠️ Tech Stack

### Programming Language

* 🐍 Python

### Machine Learning

* 🤖 Scikit-learn
* 🐼 Pandas
* 🔢 NumPy
* 📦 Joblib

### Web Application

* 🎈 Streamlit

### Data Visualization

* 📊 Plotly
* `plotly.graph_objects`

### Styling

* 🎨 Custom CSS
* HTML elements
* Glassmorphism-inspired UI

---

## 📂 Project Structure

```text
PROJECT-03-AI-HOUSE-PRICE-PREDICTOR/
│
├── app.py
│
├── generate_and_train.py
│
├── housing_data.csv
│
├── model.joblib
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

### File Description

| File                    | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| `app.py`                | Main Streamlit web application           |
| `generate_and_train.py` | Generates/trains the ML regression model |
| `housing_data.csv`      | Housing dataset used for model training  |
| `model.joblib`          | Pre-trained Machine Learning model       |
| `requirements.txt`      | Required Python libraries                |
| `.gitignore`            | Files excluded from Git                  |
| `README.md`             | Project documentation                    |

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/JASH2026AD/PROJECT-03-AI-HOUSE-PRICE-PREDICTOR.git
```

Move into the project directory:

```bash
cd PROJECT-03-AI-HOUSE-PRICE-PREDICTOR
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

Start the Streamlit development server:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

in your browser.

---

# 🧠 Model Training

The repository already contains a trained model:

```text
model.joblib
```

Therefore, you can run the application directly without retraining the model.

If you want to retrain the model using the housing dataset, run:

```bash
python generate_and_train.py
```

The script trains the Machine Learning model and generates an updated:

```text
model.joblib
```

file.

---

# 🔄 Prediction Process

When a user enters property information:

```text
User Input
   │
   ├── Square Footage
   ├── Bedrooms
   ├── Bathrooms
   └── Property Age
          │
          ▼
    Streamlit App
          │
          ▼
   Pre-trained Model
          │
          ▼
    Price Prediction
          │
          ▼
   Analytics Dashboard
          │
   ┌──────┼───────────┐
   ▼      ▼           ▼
 Gauge  Trajectory   Radar
 Chart    Chart       Chart
```

---

# 💡 What This Project Demonstrates

This project demonstrates practical knowledge of:

* Machine Learning Regression
* Data preprocessing
* Feature-based prediction
* Model training
* Model serialization with Joblib
* Python application development
* Streamlit dashboards
* Interactive data visualization
* Machine Learning model deployment into a web interface

---

# 🔮 Future Improvements

Future versions could include:

* 🏙️ Location-based house pricing
* 🗺️ Google Maps integration
* 📍 City and neighborhood selection
* 📊 Larger real-world housing datasets
* 🧠 Multiple ML model comparison
* 🌲 Random Forest / XGBoost models
* 📉 Model accuracy dashboard
* 🔐 User authentication
* 💾 Prediction history
* ☁️ Cloud deployment
* 📱 Improved mobile interface
* 🏘️ Real-estate market API integration

---

# 📸 Screenshots

Add screenshots of your application here.

```text
assets/
├── dashboard.png
├── prediction.png
├── valuation-chart.png
└── radar-analysis.png
```

Example:

```markdown
![AI House Price Predictor Dashboard](assets/dashboard.png)
```

---

# 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# ⭐ Support

If you find this project useful, consider giving the repository a **⭐ Star**.

It helps support the project and future improvements.

---

## 👨‍💻 Author

**Jaswanth Chennu**

GitHub: `@JASH2026AD`

---

## 📄 License

This project is intended for **educational and Machine Learning development purposes**.

---

<div align="center">

# 🏠 AI House Price Predictor

### Machine Learning • Data Analytics • Property Valuation

**Turning property data into intelligent price predictions. 🚀**

</div>
