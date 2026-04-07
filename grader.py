def grade_task(task, action):
    correct = task["answer"]

    if isinstance(correct, list):
        return 1.0 if action == correct else 0.5

    return 1.0 if str(action).strip().lower() == str(correct).strip().lower() else 0.0