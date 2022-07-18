
import string


# A list containing all characters
all_alphabets= string.ascii_letters

	
"""
create a dictionary to store the substitution
for the given alphabet in the plain text
based on the key
"""

	
dict1 = {}
key = 4

for i in range(len(all_alphabets)):
	dict1[all_alphabets[i]] = all_alphabets[(i+key)%len(all_alphabets)]


plain_txt= "ilovesfbu"
cipher_txt=[]

# loop to generate ciphertext

for char in plain_txt:
	if char in all_alphabets:
		temp = dict1[char]
		cipher_txt.append(temp)
	else:
		temp =char
		cipher_txt.append(temp)
		
cipher_txt= "".join(cipher_txt)

	

# create a dictionary to store the substitution for the given alphabet in the cipher
# text based on the key


	
dict2 = {}	
for i in range(len(all_alphabets)):
	dict2[all_alphabets[i]] = all_alphabets[(i-key)%(len(all_alphabets))]
	
# loop to recover plain text
decrypt_txt = []

for char in cipher_txt:
	if char in all_alphabets:
		temp = dict2[char]
		decrypt_txt.append(temp)
	else:
		temp = char
		decrypt_txt.append(temp)
		
decrypt_txt = "".join(decrypt_txt)
print("plain text :", decrypt_txt)
print("Cipher Text|| output: ",cipher_txt)

