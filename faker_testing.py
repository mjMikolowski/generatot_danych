from faker import Factory
import random
fake = Factory.create('pl_PL')

pesel_one = random.randint(0, 100)
print(pesel_one)