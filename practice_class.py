class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# 2개 이상의 부모 클래스의 상속 받을 때는
# super는 Unit Class만 초기화를 한다
# 2개이상이면 클랙시.이닛 클래스로 초기화
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    def show_deatail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

a = House("강남", "아파트", "매매", "10억", "2010년")
b = House("마포", "오피스텔", "전세", "5억", "2007년")
c = House("송파", "빌라", "월세", "500/50", "2000년")

print("총 3대의 매물이 있습니다.")
a.show_deatail()
b.show_deatail()
c.show_deatail()
