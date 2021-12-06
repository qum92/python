# 지역변수 & 전역변수

# gun = 10
# def checkPoint(soldiers):
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkPoint_ret(gun, soliders):
#     gun = gun - soliders
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkPoint(2)
# gun = checkPoint_ret(gun, 3)
# print("남은 총 : {0}".format(gun))

height = input("당신의 키는 몇 cm입니까? ")
gender = input("당신의 성별은 어떻게 됩니까? ")

def std_weight(gender, height):
    sumHeight = (height/100) * (height/100)
    if gender == "남자":
        return sumHeight * 22
    else:
        return sumHeight * 21

result = std_weight(gender, int(height))
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(result, 2)))


