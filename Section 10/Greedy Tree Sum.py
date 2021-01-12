class BinaryTree:
	class TreeNode:
		def __init__(self, data):
			self.data = data
			self.left, self.right = None, None

	def __init__(self, data: int):
		self.head = self.TreeNode(data=data)

	def insertNode(self, data: int):
		head, parent = self.head, None
		while head:
			parent = head
			if data < head.data:
				head = head.left
			else:
				head = head.right

		if data < parent.data:
			parent.left = self.TreeNode(data=data)
		else:
			parent.right = self.TreeNode(data)


def getGreedySum(head: BinaryTree.TreeNode):
	while head:
		yield head.data
		head = head.right


if __name__ == "__main__":
	tree = BinaryTree(10)

	for i in [20, 16, 8, 17, 12, 5, 9, 22]:
		tree.insertNode(i)

	"""
			10
		/       \\
		8       20
	/   \\      /   \\
	5   4      16   22
			/   \\
			12  17
	"""

	print(sum(getGreedySum(tree.head)))
