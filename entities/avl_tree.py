from entities.segment import Segment

class Node:
    def __init__(self, segment :Segment):
        self.key = segment
        self.left = None
        self.right = None
        self.height = 1


# Based on tree implemented in website "Programiz"
class AVLTree:
    def __init__(self):
       self.my_root = None
        
    # Treating initial root
    def insert_node(self, key: Segment):
        if self.my_root is None:
            self.my_root = Node(key)
        else:
            self._insert_node(self.my_root, key)
    
    
    # Key is tuple regarding point coordinates (x,y) 
    def _insert_node(self, root, key: Segment):
        # Find the correct location and insert the node
        if not root:
            return Node(key)
        elif key == root.key:
            return root
        elif key < root.key:
            root.left = self._insert_node(root.left, key)
        else:
            root.right = self._insert_node(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self._get_balance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root
    
    def find_predecessor(self, key: Segment):
        if self.my_root is None:
            return None
        self._find_predecessor(self.my_root, key)
    
    def _find_predecessor(self, root, key):
        if not root:
            return None

        predecessor = None

        while root:
            if key > root.key:
                predecessor = root
                root = root.right
            elif key < root.key:
                root = root.left
            else:
                # Node with the given key found
                if root.left:
                    # If the left subtree exists, predecessor is the maximum in the left subtree
                    predecessor = self._get_max_value_node(root.left)
                break

        return predecessor
    
    
    def find_successor(self, key: Segment):
        if self.my_root is None:
            return None
        self._find_successor(self.my_root, key)
        
    def _find_successor(self, root, key):
        breakpoint()
        if not root:
            return None

        successor = None

        while root:
            if key < root.key:
                successor = root
                root = root.left
            elif key > root.key:
                root = root.right
            else:
                # Node with the given key found
                if root.right:
                    # If the right subtree exists, successor is the minimum in the right subtree
                    successor = self._get_min_value_node(root.right)
                break

        return successor
    
    
    def delete_node(self, key: Segment):
        if self.my_root is None:
            return None
        self._delete_node(self.my_root, key)
    
    def _delete_node(self, root, key):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self._delete_node(root.left, key)
        elif key > root.key:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self._delete_node(root.right, temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self._get_height(root.left),
                              self._get_height(root.right))

        balanceFactor = self._get_balance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self._get_balance(root.left) >= 0:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
        if balanceFactor < -1:
            if self._get_balance(root.right) <= 0:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)
        return root

    
    # Function to perform left rotation
    def _left_rotate(self, z):
        y = z.right
        
        if y is None:
            return z  # No right rotation possible without a left child (already balanced)
        
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))
        return y


    # Function to perform right rotation
    def _right_rotate(self, z):
        y = z.left
        
        if y is None:
            return z  # No right rotation possible without a left child (already balanced)
        
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))
        return y

    
    # Get the height of the node
    def _get_height(self, root):
        if not root:
            return 0
        return root.height
    
    
    # Get balance factore of the node
    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)
    
    
    def _get_min_value_node(self, node):
        if not node:
            return None
        
        if node.left:
            return self._get_min_value_node(self, node.left)
        else:
            return node
        
    def _get_max_value_node(self, node):
        if not node:
            return None
        
        if node.left:
            return self._get_min_value_node(self, node.left)
        else:
            return node