class OfficeEnv:
    def reset(self):
        return {"task": "Classify email"}

    def step(self, action):
        return {"result": action}, 1.0, True, {}

    def state(self):
        return {"status": "running"}
