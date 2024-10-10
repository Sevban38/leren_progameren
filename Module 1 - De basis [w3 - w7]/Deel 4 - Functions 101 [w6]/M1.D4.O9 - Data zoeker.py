def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator)
    if 0 <= position < len(splitted_strings):
        return splitted_strings[position]
    else:
        return None

# Test cases
toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
print(get_value(toets_data, ',', 8))  # Expected output: 'Bram:6'
print(get_value(toets_data, ',', 0))  # Expected output: 'Sofie:8'
print(get_value(toets_data, ',', 9))  # Expected output: 'Maria:7'
print(get_value(toets_data, ',', 10)) # Expected output: None
print(get_value('muis,kat,hond', ',', 1)) # Expected output: 'kat'