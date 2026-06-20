def generate_meal_plan(goal, diet_type):

    meals = {

        "vegetarian": {

            1: {  # Fat Loss
                "Breakfast": [
                    "Oats",
                    "Low-fat Milk",
                    "Apple"
                ],

                "Lunch": [
                    "Rice",
                    "Dal",
                    "Mixed Vegetables"
                ],

                "Dinner": [
                    "Paneer",
                    "Salad"
                ]
            },

            2: {  # Maintain
                "Breakfast": [
                    "Oats",
                    "Milk",
                    "Banana"
                ],

                "Lunch": [
                    "Rice",
                    "Dal",
                    "Paneer"
                ],

                "Dinner": [
                    "Roti",
                    "Vegetables",
                    "Curd"
                ]
            },

            3: {  # Muscle Gain
                "Breakfast": [
                    "Oats",
                    "Milk",
                    "Banana",
                    "Peanut Butter"
                ],

                "Lunch": [
                    "Rice",
                    "Dal",
                    "Paneer",
                    "Soya Chunks"
                ],

                "Dinner": [
                    "Paneer",
                    "Roti",
                    "Curd"
                ]
            }
        },

        "nonveg": {

            1: {  # Fat Loss
                "Breakfast": [
                    "Boiled Eggs",
                    "Oats"
                ],

                "Lunch": [
                    "Rice",
                    "Chicken Breast",
                    "Salad"
                ],

                "Dinner": [
                    "Fish",
                    "Vegetables"
                ]
            },

            2: {  # Maintain
                "Breakfast": [
                    "Eggs",
                    "Oats",
                    "Milk"
                ],

                "Lunch": [
                    "Rice",
                    "Chicken",
                    "Vegetables"
                ],

                "Dinner": [
                    "Fish",
                    "Roti"
                ]
            },

            3: {  # Muscle Gain
                "Breakfast": [
                    "4 Eggs",
                    "Oats",
                    "Milk",
                    "Banana"
                ],

                "Lunch": [
                    "Rice",
                    "Chicken",
                    "Eggs"
                ],

                "Dinner": [
                    "Fish",
                    "Roti",
                    "Curd"
                ]
            }
        }
    }

    return meals[diet_type][goal]