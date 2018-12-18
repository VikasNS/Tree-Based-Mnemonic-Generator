import pickle

with open('all_words','rb') as input_file:
    all_words=pickle.load(input_file)

class Node():
    def __init__(self):
        self.count = 0
        self.nodes = dict()

    def add_node(self, letter):
        if letter not in self.nodes:
            self.nodes[letter] = Node()
        return self.nodes[letter]

    def next(self, letter):
        return self.nodes[letter]

base_node=Node()

for word in all_words:

        node=base_node

        for letter in word:
            node=node.add_node(letter)
        node.word=word
        node.count+=1

with open('node','wb') as output_file:
    pickle.dump(base_node,output_file)
