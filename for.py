# 반복문

# 1. For

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# randrange()
# for waiting_no in range(1, 6): # 0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

# 2. While

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#          print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#          index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# 3. Continue & Break

# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book :
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 4. For문 활용

# 출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron Man", "Thor", "I am groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron Man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# Quiz
from random import *
count = 0
for guests in range(1, 51) :
    isRide = ""
    time = randrange(5, 51)
    if 5 <= time < 16 :
        isRide = "O"
        count += 1
    print("[{0}] {1}번째 손님 (소요시간 : {2}분".format(isRide, guests, time))
print("총 탑승 승객 : {0} 분".format(count))