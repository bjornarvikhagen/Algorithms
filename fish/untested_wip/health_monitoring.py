import numpy as np
import pandas as pd

# Define thresholds for different environmental parameters
temperature_threshold = 28  # Maximum temperature threshold in Celsius
oxygen_threshold = 5  # Minimum oxygen threshold in mg/L
ph_threshold = 7.5  # Maximum pH threshold
ammonia_threshold = 0.2  # Maximum ammonia threshold in mg/L

# Simulated environmental data
data = {
    'temperature': [26, 28, 27, 25],
    'oxygen': [6, 5.2, 5.8, 6.5],
    'ph': [7.2, 7.6, 7.4, 7.3],
    'ammonia': [0.1, 0.15, 0.18, 0.2]
}

# Create DataFrame from environmental data
df = pd.DataFrame(data)

# Check if any parameter exceeds the threshold
if (df['temperature'] > temperature_threshold).any() or \
        (df['oxygen'] < oxygen_threshold).any() or \
        (df['ph'] > ph_threshold).any() or \
        (df['ammonia'] > ammonia_threshold).any():
    print("Fish health is at risk. Take necessary actions.")

    # Generate alerts and recommendations based on specific environmental conditions
    if (df['temperature'] > temperature_threshold).any():
        print("Temperature is above the recommended limit.")
        # Generate specific recommendations for temperature-related issues

    if (df['oxygen'] < oxygen_threshold).any():
        print("Oxygen levels are below the recommended threshold.")
        # Generate specific recommendations for low oxygen levels

    if (df['ph'] > ph_threshold).any():
        print("pH levels are above the recommended range.")
        # Generate specific recommendations for high pH levels

    if (df['ammonia'] > ammonia_threshold).any():
        print("Ammonia levels are above the recommended limit.")
        # Generate specific recommendations for high ammonia levels

else:
    print("Fish health is stable. No immediate action required.")

