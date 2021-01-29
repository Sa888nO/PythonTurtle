import turtle, math

turtle.shape('turtle')
turtle.color('green')
stepRange = 20
for x in range(10):
	stepRange += 10 * math.sqrt(2)
	for y in range(4):
		turtle.forward(stepRange)
		turtle.right(90)
	turtle.left(135)
	turtle.penup()
	turtle.forward(10)
	turtle.right(135)
	turtle.pendown()		
turtle.done()