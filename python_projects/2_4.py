
# 튜플 자료형  

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# print(t1)
# print(t2) 
# print(t3)
# print(t4)
# print(t5)

# 삭제 : TypeError: 'tuple' object doesn't support item deletion
# del t3[0] 

# 값 변경 : TypeError: 'tuple' object does not support item assignment
# t3[0] = 'c'

#튜플을 더하는 예이다. 이때 t1, t2 튜플의 요솟값이 바뀌는 것은 아니다. t1, t2 튜플을 더하여 새로운 튜플 t3를 생성한 것
t6 = t2 + t3
print(t6)

t7 = t4 * 3
print(t7)