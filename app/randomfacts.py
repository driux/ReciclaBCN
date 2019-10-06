import random

def randomfact():
    with open("app/curiosidades.txt") as f:
        content = f.readlines()
        x = random.randint(0, len(content))
        return content[x]
