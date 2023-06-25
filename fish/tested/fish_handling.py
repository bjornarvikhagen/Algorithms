import numpy as np
import warnings
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Define handling method names
handling_method_names = {
    0: "Manual Handling",
    1: "Gentle Handling",
    2: "Controlled Environment",
    3: "Automated Processing"
}

# Define fish size names
fish_size_names = {
    0: "Small Fish (<10 cm)",
    1: "Medium Fish (10-20 cm)",
    2: "Large Fish (>20 cm)"
}

# Define stress level descriptions
stress_level_descriptions = {
    1: "Low Stress: Fish experience minimal stress, indicating a calm and favorable environment for their well-being.",
    2: "Moderate Stress: Fish may experience some mild stress due to external factors, but it does not significantly impact their health or behavior.",
    3: "Medium Stress: Fish experience moderate levels of stress, which might result from certain handling or environmental conditions.",
    4: "High Stress: Fish encounter significant stress levels, indicating a challenging or unfavorable environment that could impact their health and overall condition.",
    5: "Very High Stress: Fish are subjected to extremely high stress levels, indicating severe or critical conditions that pose a significant risk to their well-being."
}

# Load the data from a CSV file
# file_path = 'fish_handling_data.csv'
# df = pd.read_csv(file_path)
# the csv file should be in this format:
# fish_size | handling_method | stress_level | biomass_utilization | growth_rate
# -------------------------------------------------------------------------------
#  10.5    |       2         |      3       |        0.85         |    0.12
#  8.2    |       4         |      2       |        0.92         |    0.09
#  12.7    |       1         |      1       |        0.78         |    0.11
#  9.1    |       3         |      2       |        0.88         |    0.1


# Sample data
data = {
    'fish_size': [10.5, 8.2, 12.7, 9.1],
    'handling_method': [2, 4, 1, 3],
    'stress_level': [3, 2, 1, 2],
    'biomass_utilization': [0.85, 0.92, 0.78, 0.88],
    'growth_rate': [0.12, 0.09, 0.11, 0.1]
}

# Create DataFrame from sample data
df = pd.DataFrame(data)

# Train a regression model to predict biomass utilization based on fish size, handling method, and stress level
model_biomass = RandomForestRegressor(n_estimators=100, random_state=42)
model_biomass.fit(df[['fish_size', 'handling_method', 'stress_level']], df['biomass_utilization'])

# Train a regression model to predict growth rate based on fish size, handling method, and stress level
model_growth = RandomForestRegressor(n_estimators=100, random_state=42)
model_growth.fit(df[['fish_size', 'handling_method', 'stress_level']], df['growth_rate'])


# Now we can predict the impact of different handling methods on fish of different sizes and stress levels
def predict_impact(fish_size, handling_method, stress_level):
    predicted_biomass = model_biomass.predict([[fish_size, handling_method, stress_level]])
    predicted_growth = model_growth.predict([[fish_size, handling_method, stress_level]])
    return predicted_biomass, predicted_growth


warnings.filterwarnings("ignore", message="X does not have valid feature names")


# Let's find the best handling method for a fish of a given size and stress level
def find_best_method(fish_size, stress_level):
    if fish_size == 0:  # Small fish
        if stress_level >= 4:
            return 0  # Manual Handling
        else:
            return 1  # Gentle Handling
    elif fish_size == 1:  # Medium fish
        if stress_level >= 4:
            return 1  # Gentle Handling
        else:
            return 2  # Controlled Environment
    else:  # Large fish
        if stress_level >= 4:
            return 2  # Controlled Environment
        else:
            return 3  # Automated Processing


# Instructions for the user
print("Welcome to the Fish Handling Method Recommender!")
print("Please provide the following information:")

# Get user input for fish size and stress level
fish_size_category = int(input("Enter the fish size category (0 for small, 1 for medium, 2 for large): "))
stress_level = int(input("Enter the stress level (1-5, where 1 is low and 5 is very high): "))

# Validate the stress level input
if stress_level < 1 or stress_level > 5:
    print("Invalid stress level input. Please enter a value between 1 and 5.")
    exit()

# Find the best handling method for a fish of the given size and stress level
best_method = find_best_method(fish_size_category, stress_level)

# Output the result
fish_size_category_name = fish_size_names[fish_size_category]
best_method_name = handling_method_names[best_method]
stress_level_description = stress_level_descriptions[stress_level]
print(f"\nFish Size Category: {fish_size_category_name}")
print(f"Stress Level: {stress_level_description}")
print(
    f"\nThe recommended handling method for a {fish_size_category_name} fish with a stress level of {stress_level} is: {best_method_name}.")

# Loop over the sample data
for i in range(len(data['fish_size'])):
    fish_size = data['fish_size'][i]
    handling_method = data['handling_method'][i]
    stress_level = data['stress_level'][i]

    # Use predict_impact function to get predictions
    predicted_biomass, predicted_growth = predict_impact(fish_size, handling_method, stress_level)

    # Print the predictions
    print("Sample", i + 1)
    print("Fish Size:", fish_size)
    print("Handling Method:", handling_method)
    print("Stress Level:", stress_level)
    print("Predicted Biomass Utilization:", predicted_biomass)
    print("Predicted Growth Rate:", predicted_growth)
    print()
