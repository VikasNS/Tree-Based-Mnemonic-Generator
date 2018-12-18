import pickle
from itertools import permutations

class Node():
    def __init__(self):
        self.count=0
        self.nodes=dict()

    def add_node(self,letter):
        if letter not in self.nodes:
            self.nodes[letter]=Node()
        return self.nodes[letter]

    def next(self,letter):
        return self.nodes[letter]

with open('node','rb') as input_file:
    base_node=pickle.load(input_file)

#words_to_remember=['Lotus','Hibiscuss','Orchids','Lilly','Evening Primrose']
#words_to_remember=["America","North Korea",'South Korea',"Hungary","Australia","South Africa"]
words_to_remember=["Apple","Amazon","Microsoft","Google"]
#words_to_remember=["NLP","DBMS","OR","OS","IPR","CN"]
#words_to_remember=["Happy","Beautiful","Sad","Ugly"]




test=[]
for word in words_to_remember:
    test.append(word[0].lower())

test=permutations(test)

for case in test:
    node = base_node
    broke=0
    for letter in case:
        try:
            node=node.next(letter)
        except:
            broke=1
            break
    if not broke:
        try:
            print(case,node.word , node.count)
        except:
           pass
