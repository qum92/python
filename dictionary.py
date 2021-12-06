# 사전
# 키 벨류 형태

#cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# print(cabinet.get(100))

# Get으로 가져오면 리턴 값을 None을 주고
# []을 사용해서 가져오면 에러를 리턴
# print(cabinet.get(5))

# 디폴트 값 사용
# print(cabinet.get(5, "사용가능"))

# 해당 사전에 해당 키가 있는지 리턴값은 boolean
# cabinet = {3:"유재석", 5:"김태호"}
# print( 3 in cabinet) # True
# print( 5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로 키 추가
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 기존 키 지우기
del cabinet["A-3"]
print(cabinet)

# 해당 사전에 키값들만 출력
print(cabinet.keys())

# 해당 사전에 벨류값들만 출력
print(cabinet.values())

# 해당 사전에 key, value 쌍으로 출력
print(cabinet.items())

# 모든 키 벨류 지우기
cabinet.clear()
print(cabinet)