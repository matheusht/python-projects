nome = str(input('NOME'))
letter = "a"

count = nome.lower().count(letter.lower())
print("The letter '{}' appears {} times in the string.".format(letter, count))