from faker import Factory

fake = Factory.create('pl_PL')

print(str(fake.date_this_decade(before_today=False, after_today=True)) +" " +  str(fake.time(pattern="%H:%M:%S", end_datetime=None)))