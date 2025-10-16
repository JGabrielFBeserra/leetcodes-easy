candies = [4, 2, 1, 1, 2]
extraCandies = 1
maior = max(candies)

for i, c in enumerate(candies):
    candies[i] += extraCandies

    if candies[i] >= maior:
        candies[i] = True
    else:
        candies[i] = False   
print(candies)