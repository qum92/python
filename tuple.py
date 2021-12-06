# 튜플
# 리스트 하고는 다르게 내용 변경이나 추가를 할 수가 없지만,
# 속도가 리스트 보다 빠르니 변경되지 않은 목록에 사용하면
# 빠르게 나타낼 수 있다.
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
