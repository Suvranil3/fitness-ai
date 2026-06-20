def get_fitness_profile():

    print("\nFitness Level")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    fitness_level = int(input("Choose: "))

    print("\nWorkout Location")
    print("1. Home")
    print("2. Gym")

    location = int(input("Choose: "))

    days = int(input("\nWorkout days per week: "))

    time_available = int(input("Minutes per workout: "))

    return {
        "fitness_level": fitness_level,
        "location": location,
        "days": days,
        "time_available": time_available
    }