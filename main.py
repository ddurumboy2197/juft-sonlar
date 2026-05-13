# Faylga 10 ta son yozish va ularni qayta o'qish
fayl = open("sonlar.txt", "w")

for i in range(1, 11):
    fayl.write(str(i) + "\n")

fayl.close()

fayl = open("sonlar.txt", "r")
print(fayl.read())
fayl.close()
