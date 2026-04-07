from tasks import get_task
from grader import grade_task

class OfficeEnv:
    def __init__(self):
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = get_task()
        self.done = False
        return {"task": self.current_task}

    def step(self, action):
        score = grade_task(self.current_task, action)
        self.done = True

        reward = score  # simple reward

        return {"result": score}, reward, self.done, {}

    def state(self):
        return self.current_task