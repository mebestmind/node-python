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
# print("--- 2. 사용자 입력 실습 ---")
# user_input = input("이름을 입력하세요: ")
# print(f"안녕하세요, {user_input}님!")

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