from faker import Factory

fake = Factory.create('pl_PL')

pesel_one = fake.credit_card_security_code(card_type=None)
print(pesel_one)