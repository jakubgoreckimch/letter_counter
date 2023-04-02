# Program is able to count every letter in your text.txt

file = open("test_text.txt", "r")

if file.readable():
    text = file.read()
    print("file loaded")
file.close()


def counter(txt, letter):
    quantity = 0
    for i in txt:
        if i == letter:
            quantity += 1
    return quantity


print("total number of letters:", len(list(text)))
alphabet = "abcdefghijklmnouprstuwxyz"

for letter in alphabet:
    finallyQuantity = counter(text.lower(), letter)
    percent = finallyQuantity / len(text) * 100
    print("letter {0} - {1} - {2}%".format(letter.upper(), finallyQuantity, round(percent, 2)))