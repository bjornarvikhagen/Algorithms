import random

# Define water quality thresholds for different parameters
water_quality_thresholds = {
    'ammonia': 0.5,  # mg/L
    'nitrite': 0.1,  # mg/L
    'nitrate': 20    # mg/L
}

# Simulate water quality measurements
def measure_water_quality():
    ammonia_level = random.uniform(0, 1)  # Random value between 0 and 1 mg/L
    nitrite_level = random.uniform(0, 0.5)  # Random value between 0 and 0.5 mg/L
    nitrate_level = random.uniform(0, 50)  # Random value between 0 and 50 mg/L
    return ammonia_level, nitrite_level, nitrate_level

# Check water quality and provide recommendations
def check_water_quality():
    ammonia, nitrite, nitrate = measure_water_quality()
    recommendations = []

    # Check ammonia level
    if ammonia > water_quality_thresholds['ammonia']:
        recommendations.append("Ammonia level is high. Take necessary steps to reduce it.")

    # Check nitrite level
    if nitrite > water_quality_thresholds['nitrite']:
        recommendations.append("Nitrite level is high. Take necessary steps to reduce it.")

    # Check nitrate level
    if nitrate > water_quality_thresholds['nitrate']:
        recommendations.append("Nitrate level is high. Take necessary steps to reduce it.")

    # Print water quality measurements and recommendations
    print("Water Quality Measurements:")
    print(f"Ammonia: {ammonia} mg/L")
    print(f"Nitrite: {nitrite} mg/L")
    print(f"Nitrate: {nitrate} mg/L")
    print()
    print("Recommendations:")
    if recommendations:
        for recommendation in recommendations:
            print(recommendation)
    else:
        print("Water quality is within acceptable limits.")

# Run the water quality control algorithm
check_water_quality()
