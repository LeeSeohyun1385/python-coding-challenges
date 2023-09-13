# 반복문 부터 작성 추천
a = [i for i in range(10)]
print(a)

# 조건문 추가 가능
array = [i for i in range(20) if i%2 ==1]
print(array)

# 연산 가능
array = [i*i for i in range(1,10)]
print(array)

# 2차원 리스트 초기화
# n * m 크기 2차원 리스트 초기화 
n = 4
m = 3
array = [[0]*m for _ in range(n)]
print(array)

# 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)사용
for _ in range(5):
    print('hello')

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5} # 집합자료형 

result = [i for i in a if i not in remove_set] 
print(result)

'''
# 리스트 관련 메서드
append()
sort()
reverse() # 순서 뒤집기
insert() # 특정 인덱스 위치에 원소 삽입
count() # 특정 값 개수
remove() # 특정 값 원소 제거 , 여러개일 경우 하나만 제거
'''