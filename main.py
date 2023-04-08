

from __future__ import annotations
import math
from typing import List, Union
'''
We are using typing library.
Pythong is duck typed and dynamically typed. When we declare a variable
a = 10, we don't specify what type of variable it is. In C, we saw that to declare
a variable, we need to use
int a = 10;
This becomes an issue in Python, for collaboration. Because if A writes a code, B has hard time understanding the code.
'''

class Point(Vector):
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

	def __mul__(self, right: Union[Vector, float]):
		if type(right) == Vector:
			return Vector(self.x*right.x, self.y*right.y, self.z*right.z)
		elif type(right) == float:
			return Vector(self.x*right, self.y*right, self.z*right)

	def __len__(self) -> int:
        	return 3

	def crossProd(self, right):
		return Vector(self.y*right.z - right.y*self.z, -(self.x*right.z - right.x*self.z), self.x*right.y-right.x*self.y)


class Force:
	def __init__(self, strength: Union[Vector, List[float]]) -> None:
		if type(strength) == list:
			if len(strength) > 3:
				print("the length of the array is longer than 3. \n Deprecating the", "array to size 3")
			x = strength[0]
			y = strength[1]
			z = strength[2]
			self.val = Vector(x, y, z)
			'''
			myForce = Force(1,2,3)
			myForce.val -> Vector(1,2,3)
			val is how we access the variable strength.
			'''
			self.x = x
			self.y = y
			self.z = z
		elif type(strength) == Vector:
			self.val = strength
			self.x = strength.x
			self.y = strength.y
			self.z = strength.z

	def acc(self, mass: float) -> Vector:
	'''
	gives acceleration
	'''
		return Vector(self.x / mass, self.y / mass, self.z / mass)


	def acc(mass: float) -> Vector:
		'''
		gives acceleration
		'''
		return Vector(self.x / mass, self.y / mass, self.z / mass)

def force(mass: float, acc: Vector) -> Vector:
	return Vector(mass* acc.x, mass* acc.y, mass* acc.z)

class Body:
	def __init__(self, mass: float, pos: Point, vel: Vector, acc: Vector, t: Number = 0) -> None:
		self.mass = mass
		self.position = pos
		self.vel = vel
		self.acc = acc
		self.t = t

	def apply(force: Force) -> None:
		"""
		Updates the acceleration of the body
		"""
		self.acc = self.acc + force.acc(self.mass)

	def evaluateAt(self, t: float) -> None:
		if t == self.t:
			return

		deltaT:float = float(t - self.t)
		self.mass = self.mass
		self.acc = self.acc
		self.vel = self.vel + self.acc * deltaT
		self.position = (
			self.position + self.vel * deltaT + self.acc * deltaT**2 * (1/2)
		)
'''body, v, t
p, v ini, m, t'''





class Kinematic:
	def __init__(self, iniV: Vector, acc: Vector, x: Point, ti) -> None:
		self.iniV = iniV
		self.acc = acc
		self.x = x
		self.time = ti

	def finalVX(self, iniV: Vector, acc: Vector) -> float:
		return iniV.x + acc.x * self.time

	def finalVY(self, iniV: Vector, acc: Vector) -> float:
		return iniV.y + acc.y * self.time

	def finalVZ(self, iniV: Vector, acc: Vector) -> float:
		return iniV.z + acc.z * self.time


	def distX(self, iniV: Vector, finalV: Vector, time: float) -> float:
		return ((iniV.x + finalV.x)/2) * time

	def distX2(self, iniV: Vector, acc: Vector, time: float) -> float:
		return iniV.x*time + (1/2) * acc.x * (time**2)


	def distY(self, iniV: Vector, finalV: Vector, time: float) -> float:
		return ((iniV.y + finalV.y)/2) * time

	def distY2(self, iniV: Vector, acc: Vector, time: float) -> float:
                return iniV.y*time + (1/2) * acc.y * (time**2)


	def distZ(self, iniV: Vector, finalV: Vector, time: float) -> float:
		return ((iniV.z + finalV.z)/2) * time

	def distX2(self, iniV: Vector, acc: Vector, time: float) -> float:
                return iniV.x*time + (1/2) * acc.x * (time**2)

	def distY2(self, iniV: Vector, acc: Vector, time: float) -> float:
                return iniV.y*time + (1/2) * acc.y * (time**2)

	def distZ2(self, iniV: Vector, acc: Vector, time: float) -> float:
                return iniV.z*time + (1/2) * acc.z * (time**2)


	def FinalVX2(self, iniV: Vector, acc: Vector, distX: float) -> float:
		return math.sqrt(iniV.x **2 + 2* acc.x * distX)

	def FinalVY2(self, iniV: Vector, acc: Vector, distY: float) -> float:
                return math.sqrt(iniV.y **2 + 2* acc.y * distY)

	def FinalVZ2(self, iniV: Vector, acc: Vector, distZ: float) -> float:
                return math.sqrt(iniV.x **2 + 2* acc.x * distZ)



myVector = Vector(1, 2, 3)

secondVector = Vector(2, 2, 2)

myForce = Force([1, 2, 6])

mass = 10.0

initialV = Vector(0, 0, 2)
accel = Vector(2,3,1)
posi = Point(2,3,4)
sec = 5.0

myBody = Body(mass, posi, initialV, accel)
me = Kinematic(initialV, accel, posi, sec)


myBody.evaluateAt(5)
# print(myBody.acc * 5, type(5))
print(me.finalVZ(initialV, accel), myBody.vel.z)
print(len(myVector), len([1,2,3]))



"""
Kinematic.finalVZ -> final z velocity
a Body doesn not have this property
"""
