from bmi import calculate_bmi, bmi_category
from bmr import calculate_bmr
from tdee import calculate_tdee
from goal import calculate_goal_calories
from macros import calculate_macros, calculate_water
from workout_generator import generate_workout
from meal_planner import generate_meal_plan
from save_user import save_user

print("=" * 40)
print("       FITNESS AI ASSISTANT")
print("=" * 40)

# USER INFO
name = input("\nEnter your name: ")

# Weight
weight = float(input("Enter your weight (kg): "))

# Height
print("\nChoose height unit:")
print("1. Meters")
print("2. Feet & Inches")

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    height_m = float(input("Enter height in meters: "))
    height_cm = height_m * 100

elif choice == "2":
    feet = int(input("Enter feet: "))
    inches = int(input("Enter inches: "))

    total_inches = (feet * 12) + inches

    height_m = total_inches * 0.0254
    height_cm = height_m * 100

else:
    print("Invalid choice!")
    exit()

# Age & Gender
age = int(input("\nEnter age: "))
gender = input("Enter gender (male/female): ")

# BMI
bmi = calculate_bmi(weight, height_m)
category = bmi_category(bmi)

# BMR
bmr = calculate_bmr(weight, height_cm, age, gender)

# TDEE
print("\nActivity Level")
print("1. Sedentary")
print("2. Lightly Active")
print("3. Moderately Active")
print("4. Very Active")
print("5. Athlete")

activity_level = int(input("Choose activity level (1-5): "))

tdee = calculate_tdee(bmr, activity_level)

# GOAL
print("\nGoal")
print("1. Fat Loss")
print("2. Maintain Weight")
print("3. Muscle Gain")

goal_names = {
    1: "Fat Loss",
    2: "Maintain Weight",
    3: "Muscle Gain"
}

goal = int(input("Choose goal (1-3): "))

goal_calories = calculate_goal_calories(tdee, goal)

selected_goal = goal_names.get(goal, "Unknown Goal")

# MACROS
macros = calculate_macros(
    weight,
    goal,
    goal_calories
)

if macros is None:
    print("Error calculating macros.")
    exit()

water = calculate_water(weight)

# FITNESS QUESTIONNAIRE
print("\n===== FITNESS PROFILE =====")

print("Fitness Level")
print("1. Beginner")
print("2. Intermediate")
print("3. Advanced")
fitness_level = int(input("Choose fitness level (1-3): "))

print("\nWorkout Location")
print("1. Home")
print("2. Gym")
location = int(input("Choose location (1-2): "))

days = int(input("\nWorkout days per week (3-6): "))
time_available = int(input("Workout duration in minutes: "))

# DIET TYPE
print("\nDiet Type")
print("1. Vegetarian")
print("2. Non-Vegetarian")

diet_choice = int(input("Choose diet type (1-2): "))

if diet_choice == 1:
    diet_type = "vegetarian"
else:
    diet_type = "nonveg"

# MEAL PLAN
meal_plan = generate_meal_plan(
    goal,
    diet_type
)

# WORKOUT PLAN
workout_plan = generate_workout(
    goal,
    fitness_level,
    location,
    days,
    time_available
)

# SAVE USER TO SUPABASE
save_user(
    name,
    age,
    gender,
    height_cm,
    weight,
    selected_goal,
    diet_type
)

# PROFILE NAMES
level_names = {
    1: "Beginner",
    2: "Intermediate",
    3: "Advanced"
}

location_names = {
    1: "Home",
    2: "Gym"
}

fitness_level_name = level_names.get(fitness_level, "Unknown")
location_name = location_names.get(location, "Unknown")

# RESULTS
print("\n===== RESULTS =====")

print(f"Name: {name}")
print(f"BMI: {bmi}")
print(f"Category: {category}")

print(f"\nBMR: {bmr} calories/day")
print(f"TDEE: {tdee} calories/day")

print(f"\nGoal: {selected_goal}")
print(f"Target Calories: {goal_calories} calories/day")

print(f"\nProtein: {macros['protein']} g/day")
print(f"Fat: {macros['fat']} g/day")
print(f"Carbs: {macros['carbs']} g/day")

print(f"\nWater: {water} L/day")

print("\n===== FITNESS PROFILE =====")
print(f"Fitness Level: {fitness_level_name}")
print(f"Workout Location: {location_name}")
print(f"Workout Days: {days}")
print(f"Workout Duration: {time_available} minutes")

print("\n===== WORKOUT PLAN =====")

for day, exercises in workout_plan.items():
    print(f"\n{day}")

    for exercise in exercises:
        print(f" - {exercise}")

print("\n===== MEAL PLAN =====")

for meal, foods in meal_plan.items():

    print(f"\n{meal}")

    for food in foods:
        print(f" - {food}")

print("\nUser successfully saved to Supabase!")