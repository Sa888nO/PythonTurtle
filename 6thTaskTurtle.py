import turtle, math

turtle.shape('turtle')
turtle.color('green')
k=0.1
rad=0.1
turnAround = 360
for x in range(3600):
	x = k * math.degrees(rad) * math.cos(rad)
	y = k * math.degrees(rad) * math.sin(rad)
	turtle.goto(x,y)
	rad+=0.1
turtle.done()