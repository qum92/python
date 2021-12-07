# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_out = thailand.ThailandPackage()
# trip_out.detail()

# import inspect
# import travel
# print(inspect.getfile(travel))

# import random
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Oscar"
# print(dir(name))

# 구글 검색
# list of python builitins
# list of python modules

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# import time 시간 관련 함수
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후

