import random

def randomfact():
    with open("app/curiosidades.txt") as f:
        content = f.readlines()
        x1 = random.randint(0, len(content)-1)
        return content[x1]
