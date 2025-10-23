from faker import Faker
fake = Faker('es_AR')

for i in range(1, 221):
    nombre=f"{fake.first_name_male()} {fake.last_name()}"
    print (nombre)