from env import OfficeEnv

env = OfficeEnv()

obs = env.reset()
print("Task:", obs)

# Dummy action (for testing)
action = "spam"

obs, reward, done, info = env.step(action)

print("Reward:", reward)
