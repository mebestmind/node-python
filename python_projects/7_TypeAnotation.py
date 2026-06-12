
## 타입 어노테이션(Type Annotation)은 Python에서 변수, 함수 매개변수, 반환값 등에 데이터 타입을 명시하는 방법입니다.

## mypy 설치 
# pip install mypy

# 디버깅 도움: 영상처럼 mypy를 사용하면 실행 전에 잘못된 타입이 들어오는 것을 
# 미리 찾아낼 수 있어, 런타임 오류를 줄여준다.
# 타입 어노테이션은 코드의 가독성을 높이고, 협업 시 
# 다른 개발자들이 함수나 변수의 의도를 쉽게 이해할 수 있도록 도와준다.


# 매개변수 a, b는 int형이어야 하며, 반환값도 int형임을 명시
def add(a: int, b: int) -> int:
    return a + b

# 올바른 사용
result = add(3, 4)
print(result)  # 출력: 7


## 변수 타입 어노테이션

name: str = "조코딩"
age: int = 25
is_student: bool = True
scores: list[int] = [90, 80, 85]



from typing import List, Dict, Optional

# 리스트 내부에 문자열만 들어갈 수 있음을 명시
names: List[str] = ["Alice", "Bob"]

# 딕셔너리 키는 문자열, 값은 정수임을 명시
student_scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# None이 될 수도 있는 변수 (Optional)
nickname: Optional[str] = None