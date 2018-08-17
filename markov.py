import numpy as np

class Chain:
    def __init__(self):
        self.dict = {}

    def feed(self, string):
        string = '/START ' + string + ' /END'
        word_list = string.split()

        for i in range(len(word_list)):
            node = Node(word_list[i])

            #All except last gets next word as neighbor
            if i < len(word_list) - 1:
                node.add_neighbor(word_list[i+1])

            self.add_node(node)

    def erase(self):
        self.dict = {}

    def add_node(self, node):
        #New node
        if node.word not in self.dict:
            self.dict[node.word] = node
        #Updates neighbors of existing node
        elif node.neighbors:
            self.dict[node.word].add_neighbor(node.neighbors[0])
    
    def write(self, max_c):
        text = ''
        node = self.dict['/START']

        while True:
            node = self.dict[node.get_neighbor()]
            if node.word == '/END':
                break
            text += node.word + ' '

        print(text[0:max_c] + '...')

        return text



class Node:
    def __init__(self, word):
        self.word = word
        self.neighbors = []
        self.count = []
        self.distribution = []


    def add_neighbor(self, neighbor):
        #New word
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.count.append(1)
            self.distribution.append(0)
        #Word already a neighbor
        else:
            self.count[self.neighbors.index(neighbor)] += 1

        #Generates new distribution
        for i in range(len(self.count)):
            self.distribution[i] = self.count[i]/sum(self.count)

    #Samples random neighbor
    def get_neighbor(self):
        return np.random.choice(self.neighbors, 1, p=list(self.distribution))[0]
