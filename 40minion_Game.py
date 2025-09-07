def minion_game(string):
    vowels, n = 'AEIOU', len(string)
    stuart = sum([n - i for i in range(0, n) if string[i] not in vowels])
    kevin = sum([n - i for i in range(0, n) if string[i] in vowels])

    diff = stuart - kevin
    if diff > 0:
        print(f"Stuart {stuart}")
    elif diff < 0:
        print(f"Kevin {kevin}")
    else:
        print("Draw")    

if __name__ == '__main__':
    s = input()
    minion_game(s)