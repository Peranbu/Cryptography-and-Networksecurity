P="ceaser cipher example"
alphabet= []
plaintext= []
for i in range(97,123):
    alphabet.append(chr(i))
print(alpahbet)
k=[]
for j in alphabet:
    k.append(alphabet.index(j))
print(k)
for i in P:
    if i in alphabet:
        print(alphabet.index(i))
        plaintext.append(alphabet.index(i))
print(plaintext)
cipher=[x+1 for x in plaintext]
print(cipher)
for m in cipher:
    if m in k:
        print(alphabet[m],end="")
