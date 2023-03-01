

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
		return Vector(0,0,0)

myVector = Vector(1, 2, 3)

secondVector = Vector(1, 2, 3)

print(myVector + (secondVector))
