# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出“猜對了”
# 猜錯的話 要告訴他比答案大或小

import random

r = random.randint(1, 100)
count = 0

while True:
	number = input('please enter a number from 0~100: ')
	number = int(number)
	count += 1 # count = count + 1

	if number == r: 
		print('It is correct!')
		print('this is the', count, 'times')
		break
	elif number > r:
		print('your answer is larger than the answer.')
	elif number < r:
		print('your answer is smaller than the answer')

	print('this is the', count, 'times')


