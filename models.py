from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False) # Constraint
    category = db.Column(db.String)
    
    # Relationship to join table
    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', cascade="all, delete-orphan")

class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    
    workout_exercises = db.relationship('WorkoutExercise', backref='workout', cascade="all, delete-orphan")

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)

    @validates('reps', 'sets') # Model Validation
    def validate_metrics(self, key, value):
        if value < 0: raise ValueError("Must be positive")
        return value