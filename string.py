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
