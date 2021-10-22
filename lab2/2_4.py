class Node:
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.price = price
        self.product_code = code

    def __str__(self):
        return f'c:{self.product_code}\np:{self.price}'

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, code, price):
        if self.root is None:
            self.root = Node(code, price)
        else:
            self._add(code, price, self.root)

    def _add(self, code, price, node):
        if code < node.product_code:
            if node.left is not None:
                self._add(code, price, node.left)
            else:
                node.left = Node(code, price)
        else:
            if node.right is not None:
                self._add(code, price, node.right)
            else:
                node.right = Node(code, price)

    def find(self, code):
        if self.root is not None:
            return self._find(code, self.root)
        else:
            return None

    def _find(self, code, node):
        if code == node.product_code:
            return node
        elif (code < node.product_code and node.left is not None):
            return self._find(code, node.left)
        elif (code > node.product_code and node.right is not None):
            return self._find(code, node.right)

    def deleteTree(self):
        self.root = None

    def calc(self, code, quan):
        if quan<1:
            raise ValueError("Quantity must above 0")
        prod = self.find(code)
        return int(quan) * prod.price

tree = Tree()
tree.add(3, 100)
tree.add(4, 200)
tree.add(0, 300)
tree.add(8, 250)
tree.add(2, 150)
print(tree.find(3))
print(tree.find(10))
quan = int(input())
print(tree.calc(3,quan))
tree.deleteTree()