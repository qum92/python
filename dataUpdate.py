# 자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

from random import *
# Quiz 답
users = range(1, 21)
print(type(users))
users = list(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨담청자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")