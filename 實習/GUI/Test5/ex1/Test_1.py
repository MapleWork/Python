from operator import mod


file = open("Test5/ex1/text1.txt", mode="w", encoding="utf-8")
file.write("測試1")
file.close()

# -----------------------------------------------------------------------

with open("Test5/ex1/text2.txt", mode="w", encoding="utf-8") as file:
    file.write("3\n5\n6")

with open("Test5/ex1/text2.txt", mode="r", encoding="utf-8") as file:
    data = file.read()

print(data)
print("-----------------------------------------------------------------------")

# -----------------------------------------------------------------------

with open("Test5/ex1/readline.txt", mode="w+", encoding="utf-8") as file:
    file.write("第一行\n第二行\n第三行")

with open("Test5/ex1/readline.txt", mode="r", encoding="utf-8") as file:
    data2 = file.readline()
    data2 += file.readline()
    data2 += file.readline()

print(data2)
print("-----------------------------------------------------------------------")

# -----------------------------------------------------------------------

with open("Test5/ex1/readlines.txt", mode="w+", encoding="utf-8") as file:
    file.write("第一行\n第二行\n第三行")

with open("Test5/ex1/readlines.txt", mode="r", encoding="utf-8") as file:
    data3 = file.readlines()

print(data3)
print(data3[0])
print(data3[1])
print("-----------------------------------------------------------------------")

# -----------------------------------------------------------------------

data4 = ["第一行\n","第二行\n","第三行\n"]

with open("Test5/ex1/writelines.txt", mode="w+", encoding="utf-8") as file:
    file.writelines(data4)

with open("Test5/ex1/writelines.txt", mode="r", encoding="utf-8") as file:
    data4=file.read()

print(data4)
print("-----------------------------------------------------------------------")

# -----------------------------------------------------------------------

sum1 = 0
a=0

with open("Test5/ex1/text2.txt", mode="r", encoding="utf-8") as file:
    for data5 in file:
        print(data5)
        sum1+=int(data5)
        a+=1

print("共", a, "行")
print("內容數字總和", sum1)