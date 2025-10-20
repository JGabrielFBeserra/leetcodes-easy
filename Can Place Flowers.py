flowerbed = [0,0,0,0,0, 0, 0, 0, 0]
n = 5

for i in range(len(flowerbed)): 
        esquerda = 0
        direita = 0
        if i == 0:
            esquerda = 0
        else:
            esquerda = flowerbed[i-1]
        if i == len(flowerbed)-1:
            direita = 0
        else:
            direita = flowerbed[i+1]
        if flowerbed[i] == 0 and esquerda == 0 and direita == 0:
            flowerbed[i] = 1
            n -= 1
        print(flowerbed)

if n <= 0:
    print(True) 
else:
    print(False)  
    