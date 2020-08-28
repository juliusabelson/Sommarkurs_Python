# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.


#-------------------------------------------------------------------------------
# Assignment 1
#-------------------------------------------------------------------------------

def movieTickets():
        numbTickets = int(input("Hur många biljetter vill du köpa? "))
        underAge = int(input("Hur många av er är under 18 år? "))
        time = int(input("Vilken föreställning (ange klockslag i hela timmar)? "))

        overAge = numbTickets - underAge
        price = 0
        price = underAge * 50
        price += overAge * 100
        if time < 18:
            price *= 0.9
        
        print('Biljetterna kostar sammanlagt', round(price,0), 'kr.')

#movieTickets()


#-------------------------------------------------------------------------------
# Assignment 2
#-------------------------------------------------------------------------------

def pepLineLength(filename):
    file = open(filename, "r") # Assumes same dict
    lines = file.readlines()
    file.close()
    numbOfLines = 0
    for i in range(len(lines)):
        if len(lines[i]) > 79:
            print('Line', i+1, 'too long:', len(lines[i]))
            #print(lines[i])
            numbOfLines += 1

    print(numbOfLines, 'lines are too long')
  

#print(pepLineLength('./Lab 3/chirps.txt'))


#-------------------------------------------------------------------------------
# Assignment 3
#-------------------------------------------------------------------------------

class Tree:
    def __init__(self, node, trees):
        self.root = node 
        self.subtrees = trees
    
    def getParts(self):
        return self.root, self.subtrees

Victoria = Tree('Victoria', [Tree('Estelle', []), Tree('Oscar', [])])
CarlPhilip = Tree('Carl Philip', [Tree('Alexander', [])])
Madeleine = Tree('Madeleine', [Tree('Leonore', []), Tree('Nicolas', [])])

royal = Tree('Carl Gustaf', [Victoria, CarlPhilip, Madeleine])


## Semi works/ugly solution
respValPreorder = []
def preorder(tree):
    root, subtrees = tree.getParts()
    #print(tree.getParts()) 
    respValPreorder.append(root)
    for subtree in subtrees:
        preorder(subtree)

    return respValPreorder

## WORKS
def postorder(tree):
    root, subtrees = tree.getParts()
    #print(tree.getParts())
    respVal = []
    for subtree in subtrees:
        for node in postorder(subtree):
            respVal.append(node)

    respVal.append(str(root))
    return respVal


#print('Preorder:', preorder(royal))
#print('Postorder:', postorder(royal))