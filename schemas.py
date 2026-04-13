from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from models import Exercise, Workout, WorkoutExercise

class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta: model = Exercise
    name = fields.String(required=True, validate=validate.Length(min=2))

class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = WorkoutExercise
        include_fk = True
    exercise = fields.Nested(ExerciseSchema, only=("name",)) # Nested data

class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta: model = Workout
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema))

