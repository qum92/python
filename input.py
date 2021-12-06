# 입력
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재미있을까요?")


# import sys
# sys.stderr은 에러처리로 나올 수 있음
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# score = {"수학": 0, "영어":50, "코딩":100}
# for subject, score in score.items():
#      #print(subject, score)
#      print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 :" + str(num).zfill(3))

# 표준 입출력
# 사용자 입력으로 받으면 무조건 타입은 str 주의
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.") 
# print(type(answer))