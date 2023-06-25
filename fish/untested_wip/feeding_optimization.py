import numpy as np

# Define nutritional requirements and feed availability for different fish species
fish_species = ['Salmon', 'Tilapia', 'Trout']
nutritional_requirements = {
    'Salmon': {'protein': 40, 'fat': 20, 'carbohydrates': 30},
    'Tilapia': {'protein': 35, 'fat': 10, 'carbohydrates': 35},
    'Trout': {'protein': 45, 'fat': 15, 'carbohydrates': 25}
}
feed_availability = {'protein': 1000, 'fat': 500, 'carbohydrates': 800}

# Calculate feed ratios based on nutritional requirements and availability
feed_ratios = {}
for species in fish_species:
    species_requirements = nutritional_requirements[species]
    feed_ratios[species] = {
        'protein': species_requirements['protein'] / feed_availability['protein'],
        'fat': species_requirements['fat'] / feed_availability['fat'],
        'carbohydrates': species_requirements['carbohydrates'] / feed_availability['carbohydrates']
    }

# Print the feed ratios for each fish species
for species, ratios in feed_ratios.items():
    print(f"Feed Ratios for {species}:")
    print(f"Protein: {ratios['protein']}")
    print(f"Fat: {ratios['fat']}")
    print(f"Carbohydrates: {ratios['carbohydrates']}")
    print()

