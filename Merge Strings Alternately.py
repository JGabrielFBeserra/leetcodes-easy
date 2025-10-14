word1 ="abcde"
word2="pqr"

word3 = []

a = max(len(word1), len(word2))
for i in range(a):
    word3.append(word1[i:i+1])
    word3.append(word2[i:i+1])
print("".join(word3))





#2
# def embaralhar(w1, w2):
#     word3 = []
#     for i, c in enumerate(w1):
#         word3.append(w1[i]) 
#         word3.append(w2[i])
#     word3 = "".join(word3)
#     return word3


# if len(word1) - len(word2) == 0:
#     print(embaralhar(word1, word2))


# if len(word1) - len(word2) > 0:
#     init = word1[:len(word2)]
#     resto = word1[len(word2):]
#     word3 = embaralhar(init, word2)
#     word3 += resto
#     print(word3) 
# elif len(word1) - len(word2) < 0:
#     init = word1[:len(word1)]
#     resto = word2[len(word1):]
#     word3 = embaralhar(init, word2)
#     word3 += resto
#     print(word3)



#1
# word1 = ""
# word2 = ""

# word3 = []

# w1 = len(word1)
# w2 = len(word2)


# if w1 - w2 == 0:
#     for i, c in enumerate(word1):
#         word3.append(word1[i]) 
#         word3.append(word2[i])
#     word3 = "".join(word3)
#     return word3

# if w1 - w2 > 0:
#     init = word1[:w2]
#     resto = word1[w2:]
#     for i, c in enumerate(init):
#         word3.append(word1[i]) 
#         word3.append(word2[i])
#     word3 = "".join(word3)
#     word3 += resto
#     return word3
# elif w1-w2 <0:
#     init = word2[:w1]
#     resto = word2[w1:]
#     for i, c in enumerate(init):
#         word3.append(word1[i]) 
#         word3.append(word2[i])
#     word3 = "".join(word3)
#     word3 += resto
#     return word3


            
