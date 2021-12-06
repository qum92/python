# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("채희주", 30, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# profile("유재석")
# profile("김태호")

# 키워드로 순서 상관없이 함수에 인자를 보낼 수 있음
# profile(name="유재석", main_lang="자바", age=30)
# profile(main_lang="자바", name="김태호", age=30)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# 가변인자
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 30, "Kotlin", "Swift")