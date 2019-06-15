'''
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.
'''

def shortestWordDistance(words, first, second):
    indexes1 = []
    indexes2 = []
    ret = len(words)
    for i in range(len(words)):
        if words[i] == first:
            indexes1.append(i)
        if words[i] == second:
            indexes2.append(i)

    for i in range(len(indexes1)):
        for j in range(len(indexes2)):
            ret = min(ret, abs(indexes1[i] - indexes2[j]))
    return ret

def shortestWordDistance2(words, first, second):
    index1 = index2 = -1
    ret = len(words)
    for i in range(len(words)):
        if words[i] == first:
            index1 = i
        elif words[i] == second:
            index2 = i

        if index1 != -1 and index2 != -1:
            ret = min(ret, abs(index1 - index2))
    return ret

given = ["practice", "makes", "perfect", "coding", "makes"]
first_word = "coding"
second_word = "practice"

print shortestWordDistance2(given, first_word, second_word)
print "test"


