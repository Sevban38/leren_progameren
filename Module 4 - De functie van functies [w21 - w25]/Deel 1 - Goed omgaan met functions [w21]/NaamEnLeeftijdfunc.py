def get_name_and_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))  
    city = input("Enter your city: ")
    return {'name': name, 'age': age, 'city': city}

def collect_data():
    data_list = []
    while True:
        choice = input("Press 'enter' to continue or type 'stop' to print: ")
        if choice == 'stop':
            break
        data = get_name_and_age()
        data_list.append(data)
    return data_list

data = collect_data()