class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def printInorder(root):

	if root:

		# Primeira recorrência na esquerda
		printInorder(root.left)

		# imprima os dados do nó
		print(root.val),

		# agora recorre na direita
		printInorder(root.right)


def printPostorder(root):

	if root:

		# Primeira recorrência na esquerda
		printPostorder(root.left)

		# agora recorre na direita
		printPostorder(root.right)

		# imprima os dados do nó
		print(root.val),


def printPreorder(root):

	if root:

		# Primeiro imprima os dados do nó
		print(root.val),

		# Em seguida, repita a esquerda
		printPreorder(root.left)

		# Finalmente recorra a direita
		printPreorder(root.right)


# inseri arvore da questão
root = Node(50)
root.left = Node(17)
root.right = Node(76)
root.right.left = Node(54)
root.right.left.right = Node(72)
root.right.left.right.left = Node(67)
root.left.left = Node(9)
root.left.left.right = Node(14)
root.left.left.right.left = Node(12)
root.left.right = Node(23)
root.left.right.left = Node(19)


#Printando as execuções
print("Pré ordem:")
printPreorder(root)

print("\nIn ordem:")
printInorder(root)

print("\nPos ordem:")
printPostorder(root)
