def generate_workout(goal, fitness_level, location, days, time_available):

    plan = {}

    # Goal Type
    if goal == 1:
        goal_type = "fat_loss"

    elif goal == 2:
        goal_type = "maintain"

    else:
        goal_type = "muscle_gain"

    # HOME WORKOUTS
    if location == 1:

        if fitness_level == 1:  # Beginner

            exercises = [
                "Pushups",
                "Bodyweight Squats",
                "Plank",
                "Lunges",
                "Jumping Jacks"
            ]

        elif fitness_level == 2:  # Intermediate

            exercises = [
                "Decline Pushups",
                "Bulgarian Split Squats",
                "Mountain Climbers",
                "Plank",
                "Burpees"
            ]

        else:  # Advanced

            exercises = [
                "Pike Pushups",
                "Pistol Squats",
                "Burpees",
                "Pullups",
                "Hanging Leg Raises"
            ]

    # GYM WORKOUTS
    else:

        if fitness_level == 1:

            exercises = [
                "Bench Press",
                "Lat Pulldown",
                "Leg Press",
                "Plank",
                "Walking"
            ]

        elif fitness_level == 2:

            exercises = [
                "Bench Press",
                "Barbell Row",
                "Squat",
                "Shoulder Press",
                "Cable Crunch"
            ]

        else:

            exercises = [
                "Bench Press",
                "Deadlift",
                "Squat",
                "Pullups",
                "Overhead Press"
            ]

    # Goal-specific additions
    if goal_type == "fat_loss":
        exercises.append("Burpees")

    elif goal_type == "muscle_gain":
        exercises.append("Pullups")

    # Determine workout split
    if days == 3:

        workout_days = [
            "Monday",
            "Wednesday",
            "Friday"
        ]

    elif days == 4:

        workout_days = [
            "Monday",
            "Tuesday",
            "Thursday",
            "Friday"
        ]

    elif days == 5:

        workout_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Friday",
            "Saturday"
        ]

    else:

        workout_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ]

    # Workout volume based on available time
    if time_available <= 30:
        exercises_per_day = 3

    elif time_available <= 60:
        exercises_per_day = 4

    else:
        exercises_per_day = 5

    # Build plan
    for day in workout_days:

        plan[day] = exercises[:exercises_per_day]

    return plan