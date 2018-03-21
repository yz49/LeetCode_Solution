# String
#############################################################
# 2018-3-19
# 3.Longest Substring Without Repeating Characters

s = 'abba'

start, longest, length, useddict = 0, 0, 0, {}
for i in range(len(s)):
    if (s[i] not in useddict) or (useddict[s[i]] < start):
        length += 1
    else:
        start = useddict[s[i]] + 1
        length = i - start + 1
    useddict[s[i]] = i
    longest = max(longest, length)

print(longest)

##############################################################
# 2018-3-19
# 5.Longest Palindromic Substring
# Manacher’s Algorithm

s = 'abb'

s = '#' + "#".join(list(s)) + '#'
pos, maxRight, RL = 0, 0, []

for i in range(len(s)):
    RL.append(0)
    if i < maxRight:
        RL[i] = min(RL[2 * pos - i], maxRight - i)
        # j = 2 * pos - i
        # if i + RL[j] <= maxRight:
        #     RL[i] = RL[j]
        # else:
        # 	RL[i] = maxRight - i
    # print(s[(pos - RL[pos]):(pos + RL[pos])])
    while (i - RL[i] - 1 >= 0) and (i + RL[i] + 1 < len(s)) and (s[i - RL[i] - 1] == s[i + RL[i] + 1]):
        RL[i] += 1
    # print(s[(pos - RL[pos]):(pos + RL[pos])])
    newRight = i + RL[i]
    if newRight > maxRight:
        maxRight = newRight
        pos = i


res = s[RL.index(max(RL)) - max(RL):RL.index(max(RL)) +
        max(RL) + 1].replace('#', '')
print(res)

##############################################################
# 2018-3-20
# 17.Letter Combinations of a Phone Number

digits = '23'

mapdict = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return [c for c in mapdict[digits]]
    return [x + y for x in mapdict[digits[0]] for y in letterCombinations(digits[1:])]

print(letterCombinations(digits))

##############################################################
# 2018-3-20
# 22. Generate Parentheses

n = 3

def generateParenthesis(n):
    res = []
    generateParenthesisRec(n, n, '', res)
    return res

def generateParenthesisRec(left, right, current, res):
    if right == 0:
        res.append(current)
    else:
        if left > 0:
            generateParenthesisRec(left - 1, right, current + '(', res)
        if right > left:
            generateParenthesisRec(left, right - 1, current + ')', res)

print(generateParenthesis(n))

##############################################################
# 2018-3-21
# 49. Group Anagrams

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sdict = dict()
for str in sorted(strs):
    if sdict.__contains__(tuple(sorted(str))):
        sdict[tuple(sorted(str))].append(str)
    else:
        sdict[tuple(sorted(str))] = [str]
res = []
for key, value in sdict.items():
    res.append(value)

print(res)


##############################################################
# 2018-3-21
# 647. Palindromic Substrings
# Manacher’s Algorithm

s = 'abc'

s = '#' + "#".join(list(s)) + '#'
pos, maxRight, RL = 0, 0, []

for i in range(len(s)):
    RL.append(0)
    if i < maxRight:
        RL[i] = min(RL[2 * pos - i], maxRight - i)
    while (i - RL[i] - 1 >= 0) and (i + RL[i] + 1 < len(s)) and (s[i - RL[i] - 1] == s[i + RL[i] + 1]):
        RL[i] += 1
    newRight = i + RL[i]
    if newRight > maxRight:
        maxRight = newRight
        pos = i
res = sum((rl + 1) // 2 for rl in RL)

print(res)
