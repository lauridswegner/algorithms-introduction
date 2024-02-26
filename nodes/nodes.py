class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def preorder(root):
    # v - l - r
    if root:
        # print root
        print(str(root.value) + "->", end="")
        # traverse left
        preorder(root.left)
        # traverse right
        preorder(root.right)


def postorder(root):
    # l - r - v
    if root:
        # traverse left
        postorder(root.left)
        # traverse right
        postorder(root.right)
        # print root
        print(str(root.value) + "->", end="")

def inorder(root):
    # r - v - l
    if root:
        # traverse right
        inorder(root.right)
        # print root
        print(str(root.value) + "->", end="")
        # traverse left
        inorder(root.left)


def printTree(root, level=0):
    if root:
        printTree(root.left, level + 1)
        print(" " * 4 * level + "->" + str(root.value))
        printTree(root.right, level + 1)

# root
root = Node("a")
# 1st layer
root.left = Node("b")
root.right = Node("c")
# 2nd layer
root.left.left = Node("d")
root.left.right = Node("e")
root.right.left = Node("f")
# 3rd layer
root.left.left.right = Node("g")

print("Printing tree...\n\n")
printTree(root)
print("\n\n")

# preorder
print("Pre-Order:")
preorder(root)
print("\n\n")

# postorder
print("Post-Order:")
postorder(root)
print("\n\n")

# inorder
print("In-Order:")
inorder(root)
print("\n\n")
