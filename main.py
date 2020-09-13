import sys
from parser import NpmParser
from graphviz import Graphviz

args = sys.argv

if len(args) != 2:
    print('Error! Wrong number of arguments')
    exit()

print(Graphviz.generateText(NpmParser.getPackage(args[1])))
