* Flesh out db prepopulate and repl
* Add following models:
    * Routine: id, name
    * Exercise: id, name
    * routine_exercise (many-to-many)
    * Perscription: id, exercise, sets, weight, reps, complete_count
    * Entry: data, exercise, sets, weight, reps
