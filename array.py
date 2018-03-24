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
