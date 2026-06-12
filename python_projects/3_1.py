# ==========================================
# 파이썬 제어문 종합 실습 예제
# ==========================================

# 1. 조건문 (if문)
print("--- 1. 조건문 실습 ---")
money = 3000
card = True

if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 2. 반복문 (while문) - 커피 자판기 예제
print("\n--- 2. while문 실습 (커피 자판기) ---")
coffee = 3
while coffee > 0:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print(f"거스름돈 {money - 300}원을 주고 커피를 줍니다.")
        coffee -= 1
    else:
        print("돈이 부족합니다. 커피를 주지 않습니다.")
        
    print(f"남은 커피의 양: {coffee}")
    
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # while문 탈출

# 3. 반복문 (for문) - 합격자 판별
print("\n--- 3. for문 실습 (시험 점수) ---")
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number += 1
    if mark < 60:
        continue # 60점 미만이면 아래 출력문 건너뛰고 다음 학생으로
    print(f"{number}번 학생은 합격입니다.")

# 4. 패션 코딩 (리스트 컴프리헨션)
print("\n--- 4. 리스트 컴프리헨션 실습 ---")
a = [1, 2, 3, 4]
# 각 요소에 3을 곱해 새로운 리스트 생성 (짝수만)
result = [num * 3 for num in a if num % 2 == 0]
print(f"결과 리스트: {result}")



# ==========================================
# range() 함수 실습 예제
# [시작, 끝) : 항상 시작값은 포함되지만, 끝값은 포함되지 않음. (예: range(1, 11)은 10에서 멈춤)
# ==========================================

# 1. 기본 사용법: range(시작, 끝)
# 1부터 10까지 출력 (11은 포함되지 않음)
print("--- 1. 1부터 10까지 출력 ---")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. 시작 생략하기: range(끝)
# 0부터 4까지 출력 (range(5)는 0부터 4까지)
print("--- 2. 0부터 4까지 출력 ---")
for i in range(5):
    print(i, end=" ")
print("\n")

# 3. 간격(Step) 사용하기: range(시작, 끝, 간격)
# 1부터 10까지 2씩 증가 (홀수만 출력)
print("--- 3. 1부터 10까지 홀수만 출력 ---")
for i in range(1, 11, 2):
    print(i, end=" ")
print("\n")

# 4. 실전 예제: 1부터 10까지의 합 구하기
print("--- 4. 1부터 10까지의 합 구하기 ---")
add = 0
for i in range(1, 11):
    add = add + i
print(f"1부터 10까지의 합: {add}")

# 5. 역순으로 출력하기
print("\n--- 5. 10부터 1까지 역순 출력 ---")
for i in range(10, 0, -1):
    print(i, end=" ")
    
    


# ==========================================
# 리스트 컴프리헨션(List Comprehension) 실습
# ==========================================

# 1. 기본 구조: [표현식 for 변수 in 반복가능객체]
# 1부터 5까지 숫자의 제곱 리스트 만들기
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(f"제곱 리스트: {squares}")


# 2. 조건문 포함: [표현식 for 변수 in 반복가능객체 if 조건]
# 1부터 10까지의 숫자 중 짝수만 골라 제곱하기
even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
print(f"짝수 제곱 리스트: {even_squares}")


# 3. 실전 응용: 문자열 처리
# 리스트에 있는 단어들의 첫 글자만 대문자로 바꾸기
fruits = ["apple", "banana", "cherry"]
capital_fruits = [f.capitalize() for f in fruits]
print(f"대문자 변환: {capital_fruits}")


# 4. 복합적인 구조: [표현식 for 변수1 in 객체1 for 변수2 in 객체2]
# 두 리스트의 요소들을 곱한 결과 리스트 (구구단처럼)
a = [1, 2]
b = [10, 20]
multiplied = [x * y for x in a for y in b]
print(f"복합 곱셈 결과: {multiplied}")