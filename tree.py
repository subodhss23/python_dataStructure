class Tree(object):
	def __init__(self):
		self.left = None	
		self.right = None
		self.data = None

root = Tree()
root.data = "what"
print(root.data)

root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

print(root.left.data)
print(root.right.data)

root.left.left = Tree()
root.left.left.data = "left 2"

root.left.right = Tree()
root.left.right.dat = "right 2"

print(root)
