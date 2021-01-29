import turtle

turtle.shape('turtle')
turtle.color('green')
n = int(input('введите кол-во лапок, их должно быть чётное кол-во!!!:  '))
if n % 2 == 0:
	step = 360 / n
	for x in range(n):
		turtle.right(step)
		turtle.forward(50)
		turtle.stamp()
		turtle.right(180)
		turtle.forward(50)
		turtle.right(180)
else:
	print('Вы ввели неверное кол-во лапок')
turtle.done()