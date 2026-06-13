
## 클로저(Closure) 예제

# 함수 안에 함수를 중첩하여 m이라는 변수를 기억하게 만듬
def mul_factory(m):
    # 외부 함수인 mul_factory의 변수 m을 기억하는 클로저
    def wrapper(n):
        return m * n
    return wrapper

#상태 유지: 함수나 객체가 호출될 때마다 처음 설정된 값(m)을 기억하고 연산을 수행
mul3 = mul_factory(3) # m=3을 기억하는 클로저 객체 생성
print(mul3(10))       # 30 출력

x
##__call__을 활용한 클로저(클래스 기반)

# __call__ 메서드를 구현하여 인스턴스를 함수처럼 사용할 수 있게 하는 방법도 있다. 
# 이 방법은 클래스의 인스턴스가 특정 상태를 유지하면서 함수처럼 동작하도록 할 때 유용하다.
class Mul:
    def __init__(self, m):
        self.m = m
    
    # __call__을 구현하여 인스턴스를 함수처럼 실행 가능하게 만듦
    def __call__(self, n):
        return self.m * n

# 클래스 인스턴스 생성 (3이라는 상태를 저장)
mul4 = Mul(3)

# 함수처럼 바로 호출 가능 (클로저처럼 상태 유지)
print(mul4(10))  # 30 출력
print(mul4(20))  # 60 출력

# 5를 기억하는 다른 객체 생성
mul5 = Mul(5)
print(mul5(10))  # 50 출력