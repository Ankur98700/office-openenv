import random

tasks = [
    {
        "type": "easy",
        "question": "Classify: 'Win money now!!!'",
        "answer": "spam"
    },
    {
        "type": "medium",
        "question": "Clean this list: ['Ankur', '', None, 'Rahul']",
        "answer": ["Ankur", "Rahul"]
    },
    {
        "type": "hard",
        "question": "Fix code: for i in range(5 print(i)",
        "answer": "for i in range(5): print(i)"
    }
]

def get_task():
    return random.choice(tasks)