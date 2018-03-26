####################################
# 238. Product of Array Except Self
# left to me, right to me

nums = [1, 2, 3, 4]

res = []
tmp = 1
for i in range(len(nums)):
    res.append(tmp)
    tmp *= nums[i]
tmp = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] *= tmp
    tmp *= nums[i]

print(res)

####################################
# 78. Subsets

nums = [1, 2, 3]


def subset(nums, cur, res):
    res.append(cur)
    for i in range(len(nums)):
        subset(nums[i + 1:], cur + [nums[i]], res)


cur, res = [], []
subset(nums, cur, res)

print(res)

####################################
# 287. Find the Duplicate Number

nums = [2, 1, 3, 2]

if len(nums) > 1:
    slow = nums[0]
    fast = nums[slow]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

print(slow)

# same idea
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)

# 141. Linked List Cycle


def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head != None and head.next != None:
        slow = head.next
        fast = slow.next
        while slow != fast and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        if fast == None or fast.next == None:
            return False
        else:
            return True
    return False

# 142. Linked List Cycle II


def detectCycle(head):
    if head != None and head.next != None:
        slow = head.next
        fast = slow.next
        while slow != fast and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        if fast == None or fast.next == None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None


####################################
# 62. Unique Paths
m = 1
n = 2

numpath = [[1 for i in range(n)] for j in range(m)]
for i in range(1, m):
    for j in range(1, n):
        numpath[i][j] = numpath[i][j - 1] + numpath[i - 1][j]

print(numpath[-1][-1])

####################################
# 48. Rotate Image

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(matrix)

'''
result =
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''
for i in range(len(matrix)):
    for j in range(len(matrix) - i):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[len(matrix) - 1 - j][len(matrix) - 1 - i]
        matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] = tmp

matrix.reverse()
print(matrix)

####################################
# 75. Sort Colors

nums = [0, 2, 2, 1, 1, 1, 0, 2, 1, 0, 1, 1, 0]

pre = 0
last = len(nums) - 1
i = 0
while pre != last and i <= last and i >= pre:
    if nums[i] == 0:
        tmp = nums[pre]
        nums[pre] = nums[i]
        nums[i] = tmp
        pre += 1
        i += 1
    elif nums[i] == 2:
        tmp = nums[last]
        nums[last] = nums[i]
        nums[i] = tmp
        last -= 1
    else:
        i += 1

print(nums)
