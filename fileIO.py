# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf-8")
# open(파일이름, 목적(w은 write), 인코딩)
# print("수학 :  0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# open(파일이름, 목적(a은 append), 인코딩)
# score_file.write("과학 :  80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# open(파일이름, 목적(r은 read), 인코딩)
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()