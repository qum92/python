# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "920630-1567910"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 부터 2 직전 까지(0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일" + "19"+jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7자리부터 맨 뒤까지
# print("뒤 7 자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자로 바꿔주기
# print(python.upper()) # 대문자로 바꿔주기
# print(python[0].isupper()) # 대문자인지 확인시켜주는 애
# print(len(python)) # 길이를 알려주는 함수
# print(python.replace("Python", "Java")) # 문자열 바꿔주는 함수

# index = python.index("n")
# print(index) # 해당 문자열 위치를 알려주는 함수
# index = python.index("n", index + 1)
# print(index) # 처음시작 된 뒤로 또 찾는 법

# print(python.find("n")) # 똑같이 찾아주는 함수
# print(python.find("Java")) # Find 함수는 그 결과를 찾지 못하면 -1 반환
# # index = python.index("Java") # Index 함수는 에러를 리턴
# # print(index)

# print(python.count("n")) # 해당 문자열에 n이 몇번 포함되는지 알려주는 함수

# 문자열 포맷
# print("a" + "b")
# print("a" , "b")

# 방법 1
# print("나는 %d살 입니다." % 20) # 정수
# print("나는 %s을 좋아해요." % "파이썬") # 문자열
# print("Apple은 %c로 시작해요" % "A") # 문자

# %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# 방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '나도코딩' 입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.")

# \\ : 문장 내에서 \
# print("D:\\Study\\PythonWorkplace")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

domain = "http://naver.com"
domain = domain.replace("http://", "")
domain = domain[:domain.index(".")]
password = domain[:3] + str(len(domain)) + str(domain.count('e')) + "!"
print(password)
