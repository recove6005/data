# 클래스

# Chapter 45. 클래스
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# Chapter 47. 멤버변수

# 레이스: 공중 유닛, 비행기. 클로킹
wraith1 = Unit("레이스", 80, 5)
print("Name: {0}, Damage: {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}은 현재 클로킹 상태입니다. - clocking: {1}".format(wraith2.name, wraith2.clocking))


wraith2.clocking = False
print("{0} 클로킹이 해제되었습니다. - clocking: {1}".format(wraith2.name, wraith2.clocking))


# Chapter 49. 상속
# 일반 유닛
class GeneralUnit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격
class AttackUnit(GeneralUnit):
    def __init__(self, name, hp, damage):
        GeneralUnit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        self.hp -= damage
        print("{0} 데미지 손상, {1} 유닛의 현재 체력은 {2} 입니다.".format(damage, self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} 유닛이 {1} 방향으로 이동합니다.".format(self.name, location))

# 파이어뱃
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(10)


# Chapter 50. 다중 상속
# 비행 유닛
class FlyableUnit():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} 유닛이 {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 공격형 비행 유닛
class FlyableAttackUnit(AttackUnit, FlyableUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        FlyableUnit.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200 , 6, 5)
valkyrie.fly(valkyrie.name, "3시")


# Chapter 51. 메소드 오버라이딩
# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10)

# 배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# move,fly 메서드 때문에 매번 공중 유닛, 지상유닛인지 확인해야 함
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "3시")


# Chapter 52. pass
def game_start():
    print("[Alert] New game started")

def game_over():
    pass # 함수가 완성된 것처럼 보여지게 함

game_start()
game_over()


# Chpater 53. super
# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 부모 클래스 지칭
        self.location = location

# 서플라이 디폿
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# 다중 상속의 경우, super()는 마지막에 상속받는 클래스(FlyableUnit)에 대해서만 init함수가 호출됨
# 필요할 경우 super()가 아닛 직접 부모클래스 명시
class FlyableBuildngUnit(Unit, FlyableUnit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        # Unit.__init__()
