import turtle

t = turtle.Turtle()
t.speed(30)
t.pensize(3)

jowls_colors = 'red'
nose_color = 'black'
complexion = 'gold'
details_of_the_ears = 'black'
eye_color = 'black'
reflection = 'white'

t.up()
t.forward(60)
t.down()

#Верхняя часть головы 
t.fillcolor(complexion)
t.begin_fill()
t.left(90)
t.circle(60, 180)

#Нижняя часть головы
t.right(30)
t.forward(10)
t.left(30)
t.circle(65, 180)
t.left(30)
t.forward(10)
t.right(30)

#Правое ухо
t.circle(60, 35)
t.right(80)
for i in range(2):
    t.forward(5)
    t.left(5)

for i in range(8):
    t.forward(10)
    t.left(5)
t.forward(10)
t.left(100)
t.forward(5)
t.left(8)

for i in range(5):
    t.forward(15)
    t.left(8)
t.forward(15)
t.left(8)
t.forward(7)
t.right(72)

#Левое ухо
t.forward(18)
t.right(72)
t.forward(7)
t.left(8)
for i in range(6):
    t.forward(15)
    t.left(8)
t.forward(5)
t.left(100)

for i in range(9):
    t.forward(10)
    t.left(5)
t.forward(5)
t.left(5)
t.forward(11)
t.end_fill()
t.up()

#Нос
t.home()
t.left(90)
t.up()
t.backward(20)
t.down()
t.fillcolor(nose_color)
t.begin_fill()
t.right(30)
t.forward(10)
for i in range(2):
    t.left(120)
    t.forward(10)
t.end_fill()

#Левый глаз
t.up()
t.home()
t.left(90)
t.forward(15)
t.left(90)
t.forward(26)
t.down()
t.fillcolor(eye_color)
t.begin_fill()
t.circle(10)
t.end_fill()

#Правый глаз
t.up()
t.left(180)
t.forward(52)
t.left(180)
t.down()
t.fillcolor(eye_color)
t.begin_fill()
t.circle(10)
t.end_fill()

#Рот
t.up()
t.home()
t.right(90)
t.forward(30)
t.down()
t.circle(10, 100)
t.up()
t.home()

t.right(90)
t.forward(30)
t.circle(10, 90)
t.backward(20)
t.down()
t.circle(10, 90)

#Детали ушей
t.up()
t.home()
t.left(90)
t.forward(100)
t.right(90)
t.forward(34)
t.down()
t.fillcolor(details_of_the_ears)
t.begin_fill()

for i in range(10):
    t.forward(5)
    t.right(8)
t.forward(2)
t.left(148)

for i in range(2):
    t.forward(10)
    t.left(5)
t.forward(10)
t.left(16)
t.forward(30)
t.left(115)
t.forward(20)

for i in range(2):
    t.forward(10)
    t.left(10)
t.left(5)
t.forward(11)
t.end_fill()

t.up()
t.home()
t.left(90)
t.forward(100)
t.left(90)
t.forward(34)
t.down()
t.begin_fill()

for i in range(11):
    t.forward(5)
    t.left(8)
t.forward(4)
t.right(155)
t.forward(8)
t.right(8)

for i in range(5):
    t.forward(10)
    t.right(5)
t.forward(6)
t.right(100)

for i in range(5):
    t.forward(10)
    t.right(5)
t.forward(2)
t.end_fill()
t.up()

#Блики в глазах
t.home()
t.left(90)
t.forward(15)
t.right(90)
t.forward(25)
t.pensize(2)
t.down()
t.fillcolor(reflection)
t.begin_fill()
t.right(90)
t.circle(10, 90)
t.end_fill()

t.up()
t.home()
t.left(90)
t.forward(15)
t.left(90)
t.forward(27)
t.left(90)
t.down()
t.begin_fill()
t.circle(10, 90)
t.end_fill()
t.up()
t.home()

#Щеки
t.pensize(3)
t.right(90)
t.forward(22)
t.left(90)
t.forward(63)
t.down()
t.fillcolor(jowls_colors)
t.begin_fill()
t.left(160)
t.circle(20, 160)
t.left(88)
for i in range(2):
    t.forward(10)
    t.left(5)

for i in range(3):
    t.forward(5)
    t.left(5)
t.forward(2)
t.end_fill()

t.up()
t.home()
t.right(90)
t.forward(56)
t.right(90)
t.forward(41)
t.down()
t.fillcolor(jowls_colors)
t.begin_fill()
t.right(133)
t.circle(20, 156)
t.left(90)
for i in range(4):
    t.forward(10)
    t.left(5)
t.forward(1)
t.end_fill()
t.ht()
t.up()
t.home()

turtle.done()