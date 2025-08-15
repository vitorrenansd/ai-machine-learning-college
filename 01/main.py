from person import Person

people = []
value = 0

while value <= 0:
    value = int(input('Please specify the quantity of people to calculate BMI: '))

for i in range(value):
    print(f'\n------ Registration Nº{i+1} ------')
    name = str(input('Name: '))
    height = float(input('Height: '))
    age = int(input('Age: '))
    weight = float(input('Weight: '))
    person = Person(name, height, age, weight)
    people.append(person)

print('\n------ BMI Report ------')
for p in people:
    print(f'Name: {p.name} | Is legal age: {p.is_legal_age()} | BMI: {p.get_bmi():.1f}')
