import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Implementing a Binary Search Tree:
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if new < node.value
        if value < self.value:
            # if left doesnt exist
            if not self.left:
                # creat left
                self.left = BST(value)
            # else:
            else:
                # leftnode.insert value
                # we can't creat here
                # it will keep searching
                self.left.insert(value)
        #if >=
        else:  # value is greater than or equal to
            # if right doesnt exist
            if not self.right:
                # creat right
                self.right = BST(value)
            else:
                self.right.insert(value)

    # def append(self, value):
    #     # recursively
    #     if value < self.value:
    #         if not self.left:
    #             self.left = BST(value)
    #         else:
    #             self.left.append(value)

    #     elif value >= self.value:
    #         if self.right is None:
    #             self.right = BST(value)
    #         else:
    #             self.right.append(value)
        

    #checking if specific value is in the tree
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)



bst = BST(names_1[0])
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


# for name_1 in names_1:
#     bst.append(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)



"runtime O(nlogn)"


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")





# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
