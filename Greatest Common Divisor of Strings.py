# str1 = "ABCDEF"
str1 = "ABABABAB"
str2 = "ABAB"

x = ""
m = ""

for i in range(min(len(str1), len(str2))):
    x += str1[i]
    if "".join(str2.split(x)) == "" and "".join(str1.split(x)) == "":
        m = x
         
print(m)
      
    