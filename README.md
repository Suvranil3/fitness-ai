# 🏋️ Fitness AI

An AI-powered fitness and nutrition coaching application that generates **personalized workout plans**, **meal plans**, **calorie targets**, **macro recommendations**, and **health insights** based on your goals and fitness profile.

---

## ✨ Features

| Feature | Description |
|---|---|
| **BMI Calculator** | Calculate Body Mass Index and get your health category |
| **BMR Calculator** | Estimate Basal Metabolic Rate using the Mifflin-St Jeor equation |
| **TDEE Calculator** | Total Daily Energy Expenditure based on your activity level |
| **Goal-based Calorie Planning** | Personalized calorie targets for fat loss, maintenance, or muscle gain |
| **Macro Calculator** | Protein, fat, and carb breakdown tailored to your goal |
| **Water Intake** | Daily water recommendation based on body weight |
| **Workout Generator** | Custom workout plans based on fitness level, location (home/gym), and available time |
| **Meal Planner** | Goal-specific meal plans with vegetarian and non-vegetarian options |
| **User Profiles** | Save user data to Supabase for persistence and tracking |

---

## 🖥️ Tech Stack

**Backend**
- Python
- FastAPI
- Supabase (Database & Auth)

**Frontend**
- HTML / CSS / JavaScript
- Responsive web UI with multiple pages:
  - Landing Page
  - Onboarding Flow
  - Dashboard
  - Workout Planner
  - Meal Planner
  - Analytics
  - Profile
  - Ranks / Leaderboard

---

## 📁 Project Structure

```
fitness-ai/
├── app.py                 # FastAPI server & route definitions
├── main.py                # CLI-based fitness assistant
├── bmi.py                 # BMI calculation logic
├── bmr.py                 # BMR calculation logic
├── tdee.py                # TDEE calculation logic
├── goal.py                # Goal-based calorie planning
├── macros.py              # Macronutrient & water intake calculations
├── workout_generator.py   # Workout plan generator
├── meal_planner.py        # Meal plan generator
├── database.py            # Supabase client setup
├── save_user.py           # Save user data to Supabase
├── questionnaire.py       # Fitness questionnaire logic
├── frontend/
│   ├── landing.html       # Landing page
│   ├── onboarding.html    # User onboarding flow
│   ├── dashboard.html     # Main dashboard
│   ├── workout.html       # Workout planner UI
│   ├── meal_planner.html  # Meal planner UI
│   ├── analytics.html     # Analytics & insights
│   ├── profile.html       # User profile page
│   └── ranks.html         # Ranks / leaderboard
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Suvranil3/fitness-ai.git
cd fitness-ai

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn supabase
```

### Run the Web App

```bash
uvicorn app:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

### Run the CLI Version

```bash
python main.py
```

---

## 🗺️ Future Roadmap

- [ ] User Authentication (Sign up / Login)
- [ ] Progress Tracking & History
- [ ] Adaptive AI Coach
- [ ] Machine Learning Recommendation System
- [ ] Mobile Application (React Native / Flutter)
- [ ] AI-powered exercise form analysis
- [ ] Social features & community challenges

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/Suvranil3">Suvranil</a>
</p>