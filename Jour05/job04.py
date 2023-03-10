import string
text = "Salut, et merci pour le poisson"
alphabet = string.ascii_lowercase + string.ascii_uppercase
shift = 3

shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
cesar = text.translate(table)

print(cesar)
