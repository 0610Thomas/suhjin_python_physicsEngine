


import math



class Point:
	def __init__(self, x, y, z) -> None:
                self.x = x
                self.y = y
                self.z = z

	def dist(self, right) -> float:
		'''
		The space between two points. Return
		'''
		return sqrt((right.x-self.x)**2 + (right.y-self.y)**2 + (right.z-self.z)**2)

	def __str__(self) -> str:
                return f"({self.x}, {self.y}, {self.z})"

class Vector:
	def __init__(self, x, y, z) -> None:
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, right):
		return Vector(self.x + right.x, self.y + right.y, self.z + right.z)

	def __str__(self) -> str:
		return f"({self.x}, {self.y}, {self.z})"

	def __mul__(self, right):
		return Vector(self.x*right.x, self.y*right.y, self.z*right.z)

	def crossProd(self, right):
		return Vector(self.y*right.z - right.y*self.z, -(self.x*right.z - right.x*self.z), self.x*right.y-right.x*self.y)




def force(mass: float, acc: Vector) -> Vector:
	return Vector(mass* acc.x, mass* acc.y, mass* acc.z)

class Body:
	def __init__(self, mass: float, pos: Point) -> None:
                self.mass = mass
                self.position = pos

class Kinematic:
	def __init__(self, iniV: Vector, acc: Vector, x: Point, ti) -> None:
		self.iniV = iniV
		self.acc = acc
		self.x = x
		self.time = ti

	def finalVX(self, iniV: Vector, acc: Vector) -> float:
		return iniV.x + acc.z * self.time

	def finalVY(self, iniV: Vector, acc: Vector) -> Vector:
                return iniV.y + acc.z * self.time

	def finalVZ(self, iniV: Vector, acc: Vector) -> Vector:
                return iniV.z + acc.z * self.time



myVector = Vector(1, 2, 3)

secondVector = Vector(2, 2, 2)

mass = 10.0

initialV = Vector(0, 0, 2)
accel = Vector(2,3,1)
posi = Point(2,3,4)
sec = 5.0

me = Kinematic(initialV, accel, posi, sec)


print(me.finalVZ(initialV, accel))
