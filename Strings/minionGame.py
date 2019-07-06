# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(string):
    list1 = []
    kevinCount = 0
    stuartCount = 0
    for i in range(0, len(string)):
        val = string[i]
        if val[0] in 'AEIOU':
            kevinCount += 1
        else:
            stuartCount += 1
        for j in range(i + 1, len(string)):
            val = val + string[j]

            if val[0] in 'AEIOU':
                kevinCount += 1
            else:
                stuartCount += 1

    if kevinCount > stuartCount:
        print("Kevin", kevinCount)
    elif kevinCount < stuartCount:
        print("Stuart", stuartCount)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)