from database import supabase

data = {
    "name": "Suvranil",
    "age": 22,
    "gender": "male",
    "height": 183,
    "weight": 73,
    "goal": "Muscle Gain",
    "diet_type": "nonveg"
}

response = (
    supabase
    .table("users")
    .insert(data)
    .execute()
)

print(response)