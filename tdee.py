def calculate_tdee(bmr, activity_level):

    activity_multipliers = {
        1: 1.2,      # Sedentary
        2: 1.375,    # Lightly Active
        3: 1.55,     # Moderately Active
        4: 1.725,    # Very Active
        5: 1.9       # Athlete
    }

    multiplier = activity_multipliers.get(activity_level)

    if multiplier is None:
        return None

    return round(bmr * multiplier, 2)