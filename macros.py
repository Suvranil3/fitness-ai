def calculate_macros(weight, goal, target_calories):

    # Protein (grams per kg)
    if goal == 1:  # Fat Loss
        protein = weight * 2.2

    elif goal == 2:  # Maintain
        protein = weight * 1.8

    elif goal == 3:  # Muscle Gain
        protein = weight * 2.0

    else:
        return None

    # Fat (25% of calories)
    fat_calories = target_calories * 0.25
    fat = fat_calories / 9

    # Remaining calories go to carbs
    protein_calories = protein * 4

    carb_calories = (
        target_calories
        - protein_calories
        - fat_calories
    )

    carbs = carb_calories / 4

    return {
        "protein": round(protein),
        "fat": round(fat),
        "carbs": round(carbs)
    }
def calculate_water(weight):
    water = weight * 0.035
    return round(water, 2)