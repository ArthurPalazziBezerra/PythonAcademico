name = input("Digite o seu nome:\n")
"""
-Arquivos:S
1- opçao w -write
2- opçao a -append
3- opçao r - read
"""
#Alternativa 1
#file = open ("name.txt", "a")
#file.write(f"{name}\n")
#file.close()

#Alternativa 2
with open ("name.txt", "a") as file:
    file.write(f"{name}\n")