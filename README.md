# AI House Price Predictor 💎

A premium machine learning web application built with Streamlit and Scikit-Learn that predicts property valuations based on sophisticated market analysis. This application features a stunning, dynamic, and glassmorphism-inspired UI with advanced data visualizations powered by Plotly.

## ✨ Features

- **Real-Time Price Prediction**: Instant AI-driven property valuation based on Square Footage, Bedrooms, Bathrooms, and Property Age using a pre-trained regression model (`model.joblib`).
- **Premium User Interface**: Dark-mode aesthetic with deep radial gradients, glassmorphism sidebar, and glowing hover animations.
- **Advanced Visualizations**:
  - **Dynamic Gauge Chart**: A massive visual indicator representing the exact estimated property value versus the city average.
  - **10-Year Valuation Trajectory**: A smoothed line chart projecting the historical value and future forecasted trend of the property.
  - **Radar Profile Analysis**: A comprehensive radar chart comparing the exact specs of your custom property against market averages.
- **Micro-Metrics & Analytics**: View comparative market positioning, calculated value per square foot, and an estimated monthly mortgage calculation.
- **Fully Responsive**: Highly fluid layouts optimized for desktop and accessible on mobile.

## 🛠️ Tech Stack

- **Frontend / Core Framework**: `Streamlit`
- **Machine Learning**: `scikit-learn`, `pandas`, `numpy`, `joblib`
- **Data Visualization**: `plotly.graph_objects`
- **Styling**: `Vanilla CSS` with inline HTML elements

## 🚀 Getting Started

Follow these instructions to run the application on your local machine.

### Prerequisites

Ensure you have Python installed on your Windows machine.

### Installation & Setup

1. **Navigate to the Directory**
   Open your PowerShell or Command Prompt and navigate to the project folder:
   ```powershell
   cd "C:\Users\Jaswanth\OneDrive\Pictures\Desktop\AI House Price Predictor"
   ```

2. **Activate the Virtual Environment**
   Activate the included virtual environment to ensure dependency isolation:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   *(Ensure you see `(venv)` in your terminal prompt).*

3. **Install Dependencies**
   Install the required Python packages:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Launch the Streamlit server:
   ```powershell
   streamlit run app.py
   ```
   The application will automatically open in your default browser at `http://localhost:8501`.

## 🧠 Model Training (Optional)

The application comes bundled with a pre-trained `model.joblib` file. However, if you wish to retrain the model on updated data (from `housing_data.csv`), simply execute the training script before running the app.

```powershell
python generate_and_train.py
```

## 👨‍💻 Credits

Created by Jaswanth Chennu with Antigravity.
