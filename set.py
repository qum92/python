# 세트 (집합)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석", "박명수"])

# 교집합 (Jave 와 Python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (Java 도 할 수 있거나 Python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (Java 할 줄 알지만 Python을 할 수 없는 개발자)
print(java - python)
print(java.difference(python))

# Python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# Java 를 잊어버렸어요
java.remove("김태호")
print(java)