# 주석 : Ctrl + ?  
# 여러줄 주석 : 큰 따옴표, 작은 따옴표 3개씩 앞뒤로 감싸기 
# print("Hello world!")
# print(1 +1)


# a = 10
# print(a)


# 문자열 : "" 또는 ''로 감싸기
multiline = '''
... Life is too short
... You need python
... '''
# print(multiline)


head = "life"
tail = " is fun"
# print(head + tail)
# 문자열의 반복 *2
# print(head *2) 

'''
# 문자열 반복 응용
print("=" * 50)
print("My Program")
print("=" * 50)
'''
'''
# 문자열 인덱싱과 슬라이싱
a = "Pithon"
# a[:1] = 'P'
# a[2:] = 'thon'
print(a[:1] + 'y' + a[2:])
'''
'''
# 문자열 포맷팅
number = 10s
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
# 'I ate 10 apples. so I was sick for three days.'
'''

# f-string
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
a = f'나의 이름은 {name}입니다. 나이는 {age*2}입니다.'
a = f'{'hi':>10}'  # 오른쪽 정렬 10자리 스트링
print(a)

