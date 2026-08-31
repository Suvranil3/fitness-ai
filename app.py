from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def home():
    return FileResponse("frontend/landing.html")


@app.get("/dashboard")
def dashboard():
    return FileResponse("frontend/dashboard.html")


@app.get("/onboarding")
def onboarding():
    return FileResponse("frontend/onboarding.html")


@app.get("/workout")
def workout():
    return FileResponse("frontend/workout.html")


@app.get("/meal-planner")
def meal_planner():
    return FileResponse("frontend/meal_planner.html")


@app.get("/analytics")
def analytics():
    return FileResponse("frontend/analytics.html")


@app.get("/profile")
def profile():
    return FileResponse("frontend/profile.html")


@app.get("/ranks")
def ranks():
    return FileResponse("frontend/ranks.html")