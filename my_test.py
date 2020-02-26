class MyClass:
	__flag = True

	def __private_method(self):
		print("fuck y0u")
		pass

	def __init__(self) -> None:
		super().__init__()


myclass = MyClass()
myclass.flag = False

