# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 1-1. 대소문자 바꾸기

N = int(input())
S = input()

word = []
for spell in S:
	if spell.islower() == True:
		spell = spell.upper()
	elif spell.isupper() == True:
		spell = spell.lower()
	word.append(spell)
		
result = ''.join(word)
print(result)


# 정답
'''
import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()

# 결과 저장을 위한 변수
result = ''

# 반복문을 이용해서 현재의 철자가 소문자라면 대문자로, 대문자라면 소문자로 치환하기
for i in S:
	if i.islower():
		result += i.upper()
	elif i.isupper():
		result += i.lower()

print(result)
'''