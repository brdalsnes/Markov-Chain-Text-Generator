import markov
import os

chain = markov.Chain()

#Uses Trump speech as input
file = open('texts/trump.txt', 'r')
chain.feed(file.read())
file.close()

#Prints first 300 letters
print('')
text = chain.write(300)

#New text created by the Markov Chain
file = open('output.txt', 'w')
file.write(text)
file.close()


