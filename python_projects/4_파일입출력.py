# ==========================================
# 파이썬 4장 실습 예제: 입출력과 함수
# ==========================================

# 1. 함수 (Function) 정의 및 활용
def add_many(*args): # 여러 개의 입력값을 받는 함수
    result = 0
    for i in args:
        result += i
    return result

print("--- 1. 함수 실습 ---")
print(f"합계: {add_many(1, 2, 3, 4, 5)}")

# 2. 사용자 입력 (input)
print("--- 2. 사용자 입력 실습 ---")
user_input = input("이름을 입력하세요햐 ")
print(f"안녕하세요, {user_input}님!")

# 3. 파일 읽고 쓰기
print("\n--- 3. 파일 입출력 실습 ---")

# 파일 쓰기 (w 모드)
with open("test.txt", "w", encoding="utf8") as f:
    for i in range(1, 4):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)

# 파일 읽기 (r 모드)
print("파일 내용 읽기:")
with open("test.txt", "r", encoding="utf8") as f:
    lines = f.readlines() # 파일 전체를 리스트로 읽기
    for line in lines:
        print(line.strip()) # strip()으로 줄바꿈 문자 제거

# 4. 람다(lambda) - 패션 코딩 예제
print("\n--- 4. 람다 실습 ---")
add = lambda a, b: a + b
print(f"람다 합계: {add(3, 4)}")

# 람다를 이용한 패션코딩 예제 : 리스트 컴프리헨션과 함께 사용하여 짝수만 3을 곱한 리스트 만들기 
#def asdf(a,b)
#   return a + b 
#def asdd(a,b)
#   return a * b 

a = [lambda a, b: a + b, lambda a, b: a * b]
print(f" 람다 리스트 합계: {a[0](1, 2)}") # 7]
print(f" 람다 리스트 곱셈: {a[1](3, 4)}") # 12]



# 리스트 안의 데이터를 람다를 이용해 정렬하기
# 람다는 단독으로 쓰기보다, 리스트를 정렬하거나 필터링할 때 유용하게 사용됨
# (이름, 나이) 순서의 리스트를 나이순으로 정렬
people = [("철수", 25), ("영희", 20), ("민수", 30)]

# key 부분에 람다를 사용하여 정렬 기준을 설정
people.sort(key=lambda x: x[1])

print(f"나이순 정렬 결과: {people}")



# ========================================================
# Immutable vs Mutable 차이점 실습
# ========================================================
print("\n--- 5. Immutable vs Mutable 차이점 실습 ---")

# 1. Immutable (변경 불가능한 자료형: 정수, 실수, 문자열, 튜플)
# 함수 내부에서 값을 바꿔도 원래 변수에는 아무런 영향이 없습니다.
def change_immutable(a):
    a = a + 1  # 새로운 객체를 생성하여 대입할 뿐, 원본이 변하지 않음
    print(f"함수 내부의 a: {a}")

num = 1
change_immutable(num)
print(f"함수 외부의 num: {num}")  # 여전히 1 (원본 유지)


# 2. Mutable (변경 가능한 자료형: 리스트, 딕셔너리, 집합)
# 함수 내부에서 .append(), .pop() 등으로 객체를 수정하면 원본도 함께 변합니다.
def change_mutable(b):
    b.append(4)  # 원본 리스트 객체 자체를 수정함
    print(f"함수 내부의 b: {b}")

lst = [1, 2, 3]
change_mutable(lst)
print(f"함수 외부의 lst: {lst}")  # [1, 2, 3, 4]로 원본이 변함!

# ========================================================
# 핵심 포인트 요약
# ========================================================
# Immutable: 함수 안에서 값을 바꾸려 하면 새로운 상자가 생김 (원본 보호)
# Mutable: 함수 안에서 값을 수정하면 원본 상자 내용물이 직접 바뀜 (영향 받음)


print("\n--- 6. 정리 ---")