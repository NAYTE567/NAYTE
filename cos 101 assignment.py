def a():
     # area = "length * breadth
     length=int(input("what is the length (in centemetres)"))
     breadth=int(input("what is the breadth( in centemetres)"))
     print(length*breadth)
a();


def b():
     # momentum = "mass * velocity"
     mass=int(input("what is the mass"))
     velocity=int(input("what is the velocity"))
     print(mass*velocity)
b();



def c():
     # force = "mass * acceleration"
     mass=int(input("Enter the mass (in kilogram)"))
     acceleration=int(input("Enter the acceleration (in metre per seconds square)"))
     print(mass*acceleration)
c();


def d():
    # acceleration = "v(final velocity) - u(initial velocity)\t(time taken)"
    v=int(input("Enter the final velocity"))
    u=int(input("Enter the initial velocity"))
    t=int(input("Enter the time taken"))
    print(v-u/t)
d();



def e():
    # speed = "distance/time"
    distance = int(input("Enter the distance"))
    time = int(input("Enter the time"))
    print(distance/time)
e();



