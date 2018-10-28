from faker import Factory
import random
fake = Factory.create('pl_PL')

pesel_one = random.randint(0, 100)
for i in range(2501, 2600):
    print(i-2501)