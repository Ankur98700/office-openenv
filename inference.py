import os
from openai import OpenAI
from env import OfficeEnv

client = OpenAI(api_key=os.getenv("HF_TOKEN"))

env = OfficeEnv()
obs = env.reset()

print("Task:", obs["task"]["question"])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": obs["task"]["question"]}
    ]
)

answer = response.choices[0].message.content
print("Model Answer:", answer)

obs, reward, done, _ = env.step(answer)

print("Score:", reward)