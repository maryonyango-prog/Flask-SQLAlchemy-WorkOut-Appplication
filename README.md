# Flask SQLAlchemy Workout Application

A classic Flask-based RESTful API for tracking workouts and exercises. This application uses Flask-SQLAlchemy for database interactions, Flask-Migrate for database migrations, and Marshmallow for object serialization and deserialization.

## Features
- Create, view, and delete workout sessions.
- Seeded list of base exercises (e.g., Push-up, Squat, Jumping Jack, Plank).
- Add specific exercises to workouts with tracked metrics (reps, sets).
- Model-level input validation (e.g., preventing negative reps/sets).

## Prerequisites
- Python 3.12
- `pipenv` for dependency management

## Installation

1. **Navigate to the project directory**:
   ```bash
   cd Flask-SQLAlchemy-WorkOut-Appplication
   ```

2. **Install dependencies** using Pipenv:
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

## Database Setup

1. **Apply migrations** to create the database schema:
   ```bash
   flask db upgrade
   ```

2. **Seed the database** with initial exercises:
   ```bash
   python seed.py
   ```

## Running the Application

Start the Flask development server:
```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5555`.

## API Endpoints

### Workouts

- **GET `/workouts`**
  - Retrieves a list of all workouts.

- **POST `/workouts`**
  - Creates a new workout.
  - **Request Body:** 
    ```json
    {
      "date": "YYYY-MM-DD"
    }
    ```

- **GET `/workouts/<id>`**
  - Retrieves a specific workout by its ID, including its associated exercises.

- **DELETE `/workouts/<id>`**
  - Deletes a specific workout by its ID.

### Workout Exercises

- **POST `/workouts/<w_id>/exercises/<e_id>/workout_exercises`**
  - Adds a specific exercise (`e_id`) to a workout (`w_id`).
  - **Request Body:** 
    ```json
    {
      "reps": 10,
      "sets": 3
    }
    ```

## Database Models

- **`Exercise`:** Stores standard exercises (`id`, `name`, `category`).
- **`Workout`:** Stores workout sessions (`id`, `date`).
- **`WorkoutExercise`:** A join table associating a `Workout` and an `Exercise`, keeping track of metrics (`reps` and `sets`).

## License
This project is licensed under the terms provided in the `LICENSE` file.