# 1st input :- Number of test cases
# 2nd input :- Numbers to be inserted in the tree
# 3rd input :- k (it will find the kth level order traversal of the tree!


from Queue import *


class tree():

    def __init__(self):
        self.root = None

    def insert(self, parent, n):
        if parent == None:
            parent = n
            return parent
        else:
            if parent.value < n.value:
                parent.right = self.insert(parent.right, n)
            elif parent.value > n.value:
                parent.left = self.insert(parent.left, n)
            return parent

    def preorder(self, n, depth, q, d, ans):
        if n == None or depth == d:
            if n == None:
                return
            else:
                q.put(n)
                return
        else:
            ans.append(n.value)
            self.preorder(n.left, depth+1, q, d, ans)
            self.preorder(n.right, depth+1, q, d, ans)

    def level(self, d, ans):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            self.preorder(q.get(), 0, q, d, ans)


class node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 0

t = input("Enter the number of tesy cases:")
j = 0
for j in range(t):
    x = raw_input(
        "Enter the numbers to be inserted in the tree seperated by a space\n")
    ans = []
    a = x.split(" ")
    d = input("Enter value of k:")
    bst = tree()
    for i in a:
        i = int(i)
        n = node(i)
        bst.root = bst.insert(bst.root, n)
    q = Queue()
    bst.level(d, ans)
    print "Ans : ",
    for j in range(len(ans)-1):
        print ans[j],
    print ans[len(ans)-1]
    j = j+1
