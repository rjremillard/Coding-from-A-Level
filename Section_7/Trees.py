class Tree:
	def __init__(self, lst: list):
		self.table = [{"left": i[0], "data": i[1], "right": i[2]} for i in lst]

	def preorder(self, r: int):
		print(self.table[r]["data"])
		if self.table[r]["left"] != -1:
			self.preorder(self.table[r]["left"])
		if self.table[r]["right"] != -1:
			self.preorder(self.table[r]["right"])


tree = Tree([
    [1,17,4],
    [2,8,6],
    [-1,4,7],
    [-1,14,-1],
    [5,22,8],
    [-1,19,-1],
    [-1,12,3],
    [-1,5,-1],
    [9,30,-1],
    [-1,25,-1]
    ])

tree.preorder(0)
