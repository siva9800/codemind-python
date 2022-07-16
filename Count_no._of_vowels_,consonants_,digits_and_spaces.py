n=input()
v='aeiou'
vowel=[i for i in n if i in v]
cons=[i for i in n if i not in v and i.isalpha()==True]
digits=[i for i in n if i.isdigit()==True]
print('Vowels:',len(vowel))
print('Consonants:',len(cons))
print('Digits:',len(digits))
print('White spaces:',n.count(' '))