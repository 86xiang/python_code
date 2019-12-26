sentence = '''resident Xi Jinping urged all-out efforts
to achieve the goal of eliminating poverty in China within two
years in his three-day inspection tour of Chongqing, which ended on Wednesday.
'''
sentence = sentence.replace(",", " ")
sentence = sentence.replace(".", " ")
words = sentence.split()
print(len(words))
