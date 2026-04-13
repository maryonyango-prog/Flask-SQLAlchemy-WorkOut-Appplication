from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Exercise, Workout, WorkoutExercise
from schemas import ExerciseSchema, WorkoutSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
Migrate(app, db)

ex_schema = ExerciseSchema(); exs_schema = ExerciseSchema(many=True)
wk_schema = WorkoutSchema(); wks_schema = WorkoutSchema(many=True)

@app.route('/workouts', methods=['GET', 'POST'])
def handle_workouts():
    if request.method == 'GET':
        return jsonify(wks_schema.dump(Workout.query.all()))
    new_w = Workout(date=request.json['date'])
    db.session.add(new_w); db.session.commit()
    return wk_schema.dump(new_w), 201

@app.route('/workouts/<int:id>', methods=['GET', 'DELETE'])
def workout_id(id):
    w = Workout.query.get_or_404(id)
    if request.method == 'DELETE':
        db.session.delete(w); db.session.commit()
        return '', 204
    return wk_schema.dump(w)

@app.route('/workouts/<int:w_id>/exercises/<int:e_id>/workout_exercises', methods=['POST'])
def add_to_workout(w_id, e_id):
    data = request.json
    new_we = WorkoutExercise(workout_id=w_id, exercise_id=e_id, reps=data['reps'], sets=data['sets'])
    db.session.add(new_we); db.session.commit()
    return WorkoutExerciseSchema().dump(new_we), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)