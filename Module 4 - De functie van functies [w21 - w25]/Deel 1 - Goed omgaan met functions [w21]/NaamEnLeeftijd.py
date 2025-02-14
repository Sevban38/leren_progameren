def get_name_and_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return {'name': name, 'age': age}

data = get_name_and_age()
print(f"Name: {data['name']}, Age: {data['age']}")
print(f"{data['name']} is {data['age']} jaar")