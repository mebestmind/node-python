# 클래스 설계도 정의
class Calculator:
    def __init__(self, first, second): # 생성자: 객체 생성 시 필수 값 초기화
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

# 객체 생성 (인스턴스)
cal1 = Calculator(4, 2)
print(f"더하기 결과: {cal1.add()}") # 출력: 6

'''
# 곱하기, 빼기, 나누기 기능 만들기
class FourCal:
    # 객체에 숫자(first, second)를 저장하는 메서드
    def setdata(self, first, second):
        self.first = first      # 객체의 변수 first에 값 저장
        self.second = second    # 객체의 변수 second에 값 저장

    # 저장된 두 숫자를 더한 결과를 반환하는 메서드
    def add(self):
        result = self.first + self.second
        return result

    # 저장된 두 숫자를 곱한 결과를 반환하는 메서드
    def mul(self):
        result = self.first * self.second
        return result

    # 저장된 두 숫자를 뺀 결과를 반환하는 메서드
    def sub(self):
        result = self.first - self.second
        return result

    # 저장된 두 숫자를 나눈 결과를 반환하는 메서드
    def div(self):
        result = self.first / self.second
        return result
      
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())


# a에 setdata 메서드를 수행하지 않고 add 메서드를 먼저 수행하면 오류가 발생한다. 왜냐하면 add 메서드에서 self.first와 self.second를 참조하는데, setdata 메서드를 통해 이 값들이 초기화되지 않았기 때문이다. 따라서 a.add()를 호출하기 전에 a.setdata(4, 2)와 같이 setdata 메서드를 먼저 호출하여 값을 설정해야 한다.
a = FourCal()
print(a.add())
'''

#파이썬 메서드명으로 __init__를 사용하면 이 메서드는 생성자가 된다.
class FourCal2:
     # 생성자: 객체가 생성될 때 자동으로 호출되는 메서드
    def __init__(self, first, second):
         self.first = first
         self.second = second
         
    # 객체에 숫자(first, second)를 저장하는 메서드
    def setdata(self, first, second):
        self.first = first      # 객체의 변수 first에 값 저장
        self.second = second    # 객체의 변수 second에 값 저장

    # 저장된 두 숫자를 더한 결과를 반환하는 메서드
    def add(self):
        result = self.first + self.second
        return result

    # 저장된 두 숫자를 곱한 결과를 반환하는 메서드
    def mul(self):
        result = self.first * self.second
        return result

    # 저장된 두 숫자를 뺀 결과를 반환하는 메서드
    def sub(self):
        result = self.first - self.second
        return result

    # 저장된 두 숫자를 나눈 결과를 반환하는 메서드
    def div(self):
        result = self.first / self.second
        return result
      
#a = FourCa2l()  # error : IndentationError: unindent does not match any outer indentation level
aa = FourCal2(4, 2)  # 객체 생성 시 __init__ 메서드가 자동으로 호출되어 first와 second가 초기화된다.

print(aa.add())



# 클래스의 상속
class MoreFourCal(FourCal2):
  
  #pass  # 상속받은 클래스에서 추가로 기능을 구현하지 않고, 부모 클래스의 기능을 그대로 사용할 때는 pass 키워드를 사용하여 빈 클래스를 정의할 수 있다.

  def pow(self):
    result = self.first ** self.second
    return result
  
  def div(self):
    result = self.first / self.second
    return result
  
bb = MoreFourCal(4, 2)
print(bb.add())  # 부모 클래스의 add 메서드 사용
print(bb.pow())  # 자식 클래스에서 새로 정의한 pow 메서드 사용

cc = FourCal2(4, 0)
#print(cc.div())  # ZeroDivis  ionError: division by zero


# 메소드 오버라이딩
# FourCal 클래스를 상속받아 SafeFourCal 클래스 정의
# 부모 클래스인 FourCal의 모든 기능(add, sub, mul, div 등)을 물려받습니다.
class SafeFourCal(FourCal2):
    
    # 부모 클래스인 FourCal의 div 메서드를 자식 클래스에서 재정의(오버라이딩)합니다.
    # 0으로 나누는 상황에서 프로그램이 에러로 종료되지 않게 처리합니다.
    def div(self):
        # 나누는 값(self.second)이 0인지 확인합니다.
        if self.second == 0:  
            # 0으로 나누면 수학적으로 정의되지 않아 에러가 발생하므로,
            # 에러 대신 0을 반환하도록 설정하여 안전하게 처리합니다.
            return 0
        else:
            # 나누는 값이 0이 아닐 경우에만 정상적으로 나눗셈을 수행합니다.
            return self.first / self.second
          
dd = SafeFourCal(4, 0)

print(dd.div())  # 0으로 나누는 경우에도 에러 없이 0을 반환하여 안전하게 처리됩니다.



# ==========================================
# 클래스 변수와 생성자 실습 예제
# ==========================================

class Family:
    # 클래스 변수: 모든 객체가 공통으로 공유하는 변수
    lastname = "김" 

    # 생성자 (__init__): 객체가 생성될 때 자동으로 호출
    # 객체를 만들 때 'name'을 필수로 입력받도록 강제함
    def __init__(self, name):
        self.name = name  # 객체 변수: 각 객체마다 다른 값을 가짐

# 1. 클래스 변수 사용 (공통 속성)
a = Family("철수")
b = Family("영희")

print(f"공통 성씨: {a.lastname}, {b.lastname}") # 둘 다 '김'

# 2. 객체 변수 사용 (개별 속성)
print(f"이름:  {a.lastname} {a.name},  {b.lastname} {b.name}")             # '철수', '영희'

# 3. 클래스 변수 값 수정 (개별 객체만 변경)
a.lastname = "박" # 'a' 객체만 성씨를 '박'으로 개명
print(f"개명 후 a: {a.lastname}, {a.name}")   # '박', '철수'
print(f"그대로 b: {b.lastname}, {b.name}")   # '김', '영희' (b는 그대로)

# 4. 클래스 변수 자체를 변경 (전체 변경)
Family.lastname = "최" # 클래스 수준에서 변경
print(f"전체 변경 후 b: {b.lastname}")        # 이제 'b'도 '최'로 변경됨