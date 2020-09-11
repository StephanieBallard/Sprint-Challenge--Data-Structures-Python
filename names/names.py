import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # left case?
        # check if the value is less than the root value?
        if value < self.value:
            # move to the left and check if it is none?
            if not self.left:
                # insert node here
                self.left = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # right case?
        # otherwise
        else:
            # move to the right and check if it is none?
            if not self.right:
                # insert the node here
                self.right = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's right node
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case?
        # check the root node value against target
        # if the root node's value and the target are the same
        if self.value == target:
            # return True
            return True
        
        # left case
        # check if the target is less than the root's value
        if target < self.value:
            # check if there is no child to the left
            if not self.left:
                # return False
                return False
            # otherwise
            else:
                # return call contains on the left child
                return self.left.contains(target)
        # right case
        # otherwise
        else:
            # check if there is no child to the right
            if not self.right:
                # return False
                return False
            # otherwise
            else:
                # return call contains on the right child
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if the tree is empty return none
        if not self:
            return None

        # while there is a right child
        while self.right:
            # move to the right
            self = self.right
        
        # once there are no more children to traverse we can return the value
        return self.value

    # return the minimum value found in a tree
    def get_min(self):
        # base case
        # if the tree is empty return none
        if not self:
            return None

        # while there is a left child
        while self.left:
            # move to the left
            self = self.left
        
        # once there are no more children to traverse we can return the value
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call foreach on the root node
        fn(self.value)

        # if left exists
        if self.left:
            # call for each on the left child
            self.left.for_each(fn)

        # if right exists
        if self.right:
            # call for each on the right child
            self.right.for_each(fn)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BSTNode("")

for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
