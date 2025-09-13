import random
print(random.randint(-10,10))
print(random.randrange(0,50,5))
print(random.choice([45,78,89]))
print(random.choice(["rock","paper","sccissor"]))
print(random.choices(["rock","paper","sccissor",89,56,23],k=2))
print(random.sample(["rock","paper","sccissor",89,56,23],k=3))
print(random.random())