message = input("Enter a message to encode or decode: ")
message = message.upper()
key = eval(input("Enter a key value from 1-26: "))
output = " "
for letter in message:
    if letter.isupper():
        value = ord(letter)+ key
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("Output message: ", output)