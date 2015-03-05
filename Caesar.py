var = 'abcdefghijklmnopqrstuvwxyz'*2

word = raw_input("Enter a word to encode. \n\n")

key = int(raw_input("\nChoose a key between 1 and 25 \n\n"))


def encrypt(word,key):
	
	encryptedCode = ""
	
	for letter in word.lower():
		if letter in var:
			new = var.find(letter)
			encryptedCode += var[new+key]	
		else: 
				encryptedCode += letter
	print encryptedCode
	return
	
def decrypt(word, key):
	
	encryptedCode = ""
	
	for letter in word.lower():
		if letter in var:
			new = var.find(letter)
			encryptedCode += var[new-key]
		else: 
				encryptedCode += letter	
	print encryptedCode
	return
		

encrypt(word, key)
decrypt(word, key)

