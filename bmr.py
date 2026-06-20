def calculate_bmr(weight, height_cm, age, gender):

    if gender.lower() == "male":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5

    elif gender.lower() == "female":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    else:
        return None

    return round(bmr, 2)