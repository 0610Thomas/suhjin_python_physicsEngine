


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



myVector = Vector(1, 2, 3)

secondVector = Vector(2, 2, 2)

mass = 10.0
accel = Vector(2,3,1)

print(force(mass, accel))


