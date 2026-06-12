import time

# 데코레이터 정의: 함수 실행 시간을 측정하는 기능
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 실행 전 시간
        result = func(*args, **kwargs) # 기존 함수 실행
        end_time = time.time()    # 실행 후 시간
        print(f"함수 {func.__name__} 실행 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

# @데코레이터 이름 으로 사용
@timer_decorator
def my_function(n):
    time.sleep(1) # 1초 대기
    return n * n

# 호출
print(my_function(10))