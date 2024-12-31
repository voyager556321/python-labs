import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        
        balance = self.get_balance_factor(node)
        
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def print_tree(self, root, level=0, prefix="Root:"):
        if root is not None:
            print("    " * level + prefix + str(root.key))
            if root.left is not None:
                self.print_tree(root.left, level + 1, "L---")
            if root.right is not None:
                self.print_tree(root.right, level + 1, "R---")
    
    def plot_tree(self):
        # Створення графу для дерева
        G = nx.DiGraph()
        pos = {}
        labels = {}
        
        def add_edges(node, pos_x, pos_y, x_offset):
            if node:
                pos[node.key] = (pos_x, pos_y)
                labels[node.key] = node.key
                if node.left:
                    G.add_edge(node.key, node.left.key)
                    l_pos = add_edges(node.left, pos_x - x_offset, pos_y - 1, x_offset / 2)
                if node.right:
                    G.add_edge(node.key, node.right.key)
                    r_pos = add_edges(node.right, pos_x + x_offset, pos_y - 1, x_offset / 2)
            return pos
        
        # Стартуємо з кореня
        add_edges(self.root, 0, 0, 4)
        
        # Побудова графу
        plt.figure(figsize=(10, 6))
        nx.draw(G, pos=pos, with_labels=True, labels=labels, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=False)
        plt.title("AVL Tree Visualization")
        plt.show()

# Демонстрація роботи AVL-дерева з візуалізацією
avl_tree = AVLTree()
avl_tree.insert_key(50)
avl_tree.insert_key(30)
avl_tree.insert_key(70)
avl_tree.insert_key(20)
avl_tree.insert_key(40)
avl_tree.insert_key(60)
avl_tree.insert_key(80)

# Виведення дерева (прямий обхід)
print("Pre-order traversal of the AVL tree:")
avl_tree.pre_order(avl_tree.root)
print("\n")

# Виведення дерева в консоль
print("Tree structure in the console:")
avl_tree.print_tree(avl_tree.root)
print("\n")

# Візуалізація дерева
avl_tree.plot_tree()
