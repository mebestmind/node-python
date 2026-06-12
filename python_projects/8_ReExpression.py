'''
1. 반복 표현식 :  {m,n}: 문자가 최소 m번에서 최대 n번까지 반복되는 패턴을 찾습니다.

예: ca{2}t

"cat": 'a'가 1번이므로 매치되지 않음

"caat": 'a'가 2번이므로 매치됨

?: 문자가 0번 또는 1번 반복될 때 매치됩니다. ({0,1}과 동일)

예: ab?c

"abc": 'b'가 1번 매치됨

"ac": 'b'가 0번 매치됨

2. 기타 주요 반복 표현식 (참고)

*: 문자가 0번 이상 반복될 때 매치됩니다. ({0,}과 동일)

+: 문자가 1번 이상 반복될 때 매치됩니다. ({1,}과 동일)


search()와 match()의 핵심 차이
re.match(): 문자열의 시작(처음)부터 패턴이 일치해야 매치됩니다.
re.search(): 문자열 전체를 검색하여 패턴이 일치하는 첫 번째 부분을 찾습니다.
re.finditer(): 문자열에서 정규식과 매치되는 모든 패턴(반복 가능한 객체)을 찾아줍니다.
re.findall(): 단순히 매치된 문자열('life', 'is', ...)만 리스트로 반환합니다.

정규표현식 프롬프트
파이썬 정규표현식을 활용해서 이문제를 해결해줘



'''

# 파이썬에서 정규 표현식을 사용하려면 re 모듈을 import 해야 합니다.
import re 

# 패턴 정의
p = re.compile('ca{2}t') 
# 'a'가 2번 반복되는 패턴을 정의합니다. 'cat'은 매치되지 않고, 'caat'은 매치됩니다.

# 매치 여부 확인
m = p.match("caat")
if m:
    print("매치되었습니다.")


    
# 1. '{m,n}' 예제: 'a'가 2번 또는 3번 반복되는 패턴
p = re.compile('ca{2,3}t')
print(p.match('caat'))   # <re.Match object>
print(p.match('caaaat')) # None (4번 반복이라 안 됨)

# 2. '?' 예제: 'b'가 있어도 되고 없어도 됨
p = re.compile('ab?c')
print(p.match('ac'))     # <re.Match object>
print(p.match('abc'))    # <re.Match object>

# 3. 매치된 문자열 확인
m = p.match('abc')
if m:
    print(f"찾은 문자열: {m.group()}") # 찾은 문자열: abc
    
    
# search() 메서드로 문자열 전체에서 패턴 검색
# 1. search()는 문자열 전체에서 처음 발견되는 것을 찾음
m = p.search("3 life is too short")
if m:
    print(f"찾은 문자열: {m.group()}") # 찾은 문자열: abc
    
    
## finditer 예제

# 패턴 정의: 알파벳이 1번 이상 반복되는 모든 경우를 찾음
p = re.compile('[a-z]+')

# 문자열에서 모든 매치 객체를 찾아 반복자(iterator)로 반환
result = p.finditer("life is too short")

print(f"finditer : {result}") 
# 출력: <callable_iterator object at ...> (반복 가능한 객체임을 확인)

# 반복문을 통해 각 Match 객체의 정보를 출력
for r in result:
    print(f"매치된 문자열: {r.group()}, 위치: {r.span()}")

# 출력 결과:
# 매치된 문자열: life, 위치: (0, 4)
# 매치된 문자열: is, 위치: (5, 7)
# 매치된 문자열: too, 위치: (8, 11)
# 매치된 문자열: short, 위치: (12, 17)


# findall()과 finditer() 차이  예제

text = "life is too short"
p = re.compile('[a-z]+')

# 1. findall(): 매치된 문자열을 '리스트'로 반환
result_all = p.findall(text)
print(f"findall 결과: {result_all}")
# 출력: ['life', 'is', 'too', 'short']

# 2. finditer(): 매치된 객체를 '반복자(iterator)'로 반환
result_iter = p.finditer(text)
print(f"finditer 결과: {result_iter}")
# 출력: <callable_iterator object at ...>

for r in result_iter:
    # 각 요소가 'Match 객체'이므로 그룹, 위치 정보 등을 더 상세히 추출 가능
    print(f"매치된 문자열: {r.group()}, 위치: {r.span()}")