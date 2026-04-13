from app import app
from models import db, Exercise

EXERCISES = [
    {"name": "Push-up", "category": "Strength"},
    {"name": "Squat", "category": "Strength"},
    {"name": "Jumping Jack", "category": "Cardio"},
    {"name": "Plank", "category": "Core"}
]

if __name__ == '__main__':
    with app.app_context():
        for exercise_data in EXERCISES:
            existing = Exercise.query.filter_by(name=exercise_data['name']).first()
            if not existing:
                db.session.add(Exercise(**exercise_data))
        db.session.commit()
        print(f"Seeded {len(EXERCISES)} exercises into app.db")
