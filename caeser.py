data = input("What is the cipher?")

for char in data:
    if ord(char) == 32:
        print(" ")
    elif ord(char) < 120:
        print(chr((ord(char)+3)))
    
    else:
        print(chr((ord(char)-23)))
