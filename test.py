import markov
import os

chain = markov.Chain()

file = open('texts/friends.txt', 'r')
chain.feed(file.read())
file.close()

print('')
text = chain.write(300)

file = open('output.txt', 'w')
file.write(text)
file.close()


