import json
from operator import mod

print("讀取 JSON 檔，存入變數")

with open("Test5/ex2/config1.json", mode="r", encoding="utf-8") as file:
    data1 = json.load(file)

print(data1)
print("name：", data1["name"])
print("ver：", data1["ver"])
print("剛剛新增的資料：", data1["text"])
print("-----------------------------------------------------------------------")

# -----------------------------------------------------------------------

data2 = {"男生":"15人", "女生":"20人"}

with open("Test5/ex2/config2.json", mode="w", encoding="utf-8") as file:
    json.dump(data2, file, ensure_ascii=False)

with open("Test5/ex2/config2.json", mode="r", encoding="utf-8") as file:
    data3 = json.load(file)

print(data3)
print("男生人數：", data3["男生"])
print("女生人數：", data3["女生"])
print("-----------------------------------------------------------------------")

# -----------------------------------------------------------------------

data4 = {"姓名":"小明", "性別":"男", "年齡":"27"}

with open("Test5/ex2/原始資料.json", mode="w", encoding="utf-8") as file:
    json.dump(data4, file, ensure_ascii=False)

with open("Test5/ex2/原始資料.json", mode="r", encoding="utf-8") as file:
    data5 = json.load(file)

print("原始資料：", data5)


data5["姓名"] = "阿銘"
data5["年齡"] = "30"

with open("Test5/ex2/修改後.json", mode="w", encoding="utf-8") as file:
    json.dump(data5, file, ensure_ascii=False)

with open("Test5/ex2/修改後.json", mode="r", encoding="utf-8") as file:
    data6 = json.load(file)

print("修改後：", data6)
print("姓名：", data6["姓名"])
print("性別：", data6["性別"])
print("年齡：", data6["年齡"])