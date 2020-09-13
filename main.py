from parser import NpmParser

if NpmParser.getDependencies("bootstrap-fileinput"):
    print(NpmParser.getDependencies("bootstrap-fileinput"))