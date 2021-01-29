import turtle, math

turtle.shape('turtle')
turtle.color('green')
stepRange = 0
n = int(input('сколько закручиваний:  '))
for x in range(n):
	stepRange += 10
	turtle.left(90)
	turtle.forward(stepRange)
turtle.done()