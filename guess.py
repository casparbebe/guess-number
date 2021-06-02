# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
start = input('請決定隨機數的開始值(請打阿拉伯數字): ')
end = input('請決定隨機數的結束值(請打阿拉伯數字): ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	number = input('請猜一個數字: ')
	number = int(number)
	if number == r:
		print('終於猜對了!')
		print('總共猜了', count, '次')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('這是你猜的第', count, '次')