s = input()

lettersU = [x for x in s if x.isalpha() and x.isupper()]
lettersL = [x for x in s if x.isalpha() and x.islower()]
numbersO = [x for x in s if x.isnumeric() and int(x)%2 != 0]
numbersE = [x for x in s if x.isnumeric() and int(x)%2 == 0]

res = "".join(sorted(lettersL))+"".join(sorted(lettersU))+"".join(sorted(numbersO))+"".join(sorted(numbersE))

print(res)