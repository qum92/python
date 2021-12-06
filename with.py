# With
# 위드는 파일 읽고 쓰기가 두문장으로 사용 가능
# 장점은 해당 파일을 읽고 쓰고 하는데 close를 안해줘도 된다.

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

for weeks in range(1,51):
    fileName = "{0}주차.txt".format(weeks)
    with open(fileName, "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n 부서 : \n 이름 : \n 업무 요약 :".format(weeks))