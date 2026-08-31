from database import supabase

def save_user(
    name,
    age,
    gender,
    height,
    weight,
    goal,
    diet_type
):

    data = {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "goal": goal,
        "diet_type": diet_type
    }

    response = (
        supabase
        .table("users")
        .insert(data)
        .execute()
    )

    return response