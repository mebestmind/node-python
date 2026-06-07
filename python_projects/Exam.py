# 2. 조건문 포함: [표현식 for 변수 in 반복가능객체 if 조건]
# 1부터 10까지의 숫자 중 짝수만 골라 제곱하기
even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
print(f"짝수 제곱 리스트: {even_squares}")
