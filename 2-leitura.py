"""
-Arquivos:S
1- opçao w -write
2- opçao a -append
3- opçao r - read
"""
with open ("name.txt", "r") as file:
    for line in file:
        print(line)