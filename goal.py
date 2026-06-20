def calculate_goal_calories(tdee, goal):

    if goal == 1:      # Fat Loss
        return round(tdee - 500, 2)

    elif goal == 2:    # Maintain
        return round(tdee, 2)

    elif goal == 3:    # Muscle Gain
        return round(tdee + 300, 2)

    else:
        return None