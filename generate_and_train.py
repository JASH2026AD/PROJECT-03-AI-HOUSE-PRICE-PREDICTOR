import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def generate_synthetic_data(num_samples=1000):
    """
    Generates synthetic, realistic housing data.
    Features: sqft, bedrooms, bathrooms, age
    """
    np.random.seed(42)
    
    # Generate random features
    sqft = np.random.randint(500, 5000, size=num_samples)
    bedrooms = np.random.randint(1, 6, size=num_samples)
    bathrooms = np.random.randint(1, 5, size=num_samples)
    age = np.random.randint(0, 50, size=num_samples)
    
    # Calculate a synthetic price using a linear combination + noise, to make sure the model 
    # can learn it reasonably well, but adding variance.
    # Base price: ₹ 1,000,000
    # Add value for sqft: ₹ 4,000 per sqft
    # Add value for bedrooms: ₹ 500,000 per bedroom
    # Add value for bathrooms: ₹ 300,000 per bathroom
    # Subtract value for age: ₹ 20,000 per year of age
    
    base_price = 1000000
    price = (base_price + 
             sqft * 4000 + 
             bedrooms * 500000 + 
             bathrooms * 300000 - 
             age * 20000)
    
    # Add some random noise
    noise = np.random.normal(0, 500000, size=num_samples)
    price = price + noise
    
    # Ensure no negative prices
    price = np.maximum(price, 500000)
    
    df = pd.DataFrame({
        'sqft': sqft,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'age': age,
        'price': price
    })
    
    return df

def main():
    print("Generating synthetic dataset...")
    df = generate_synthetic_data()
    
    # Save a sample of the dataset for reference if needed
    df.to_csv('housing_data.csv', index=False)
    print("Saved dataset to 'housing_data.csv'")
    
    # Prepare features and target
    X = df[['sqft', 'bedrooms', 'bathrooms', 'age']]
    y = df['price']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Random Forest model
    print("Training Random Forest Regressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Evaluation:")
    print(f"  RMSE: Rs. {np.sqrt(mse):,.2f}")
    print(f"  R2 Score: {r2:.4f}")
    
    # Export the trained model
    model_filename = 'model.joblib'
    joblib.dump(model, model_filename)
    print(f"Successfully saved trained model to '{model_filename}'")

if __name__ == "__main__":
    main()
