def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "a", encoding="utf-8")
    string = 1

    for i in range(len(strings)):
        strings_positions[(string, file.tell())] = strings[i]
        file.write(f"{strings[i]}\n")
        string += 1

    file.close()

    return strings_positions



info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)