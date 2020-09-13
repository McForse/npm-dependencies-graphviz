import re
from package import Package


class Graphviz:

    @staticmethod
    def generateText(package):
        if type(package) is Package:
            text = 'digraph ' + Graphviz.normalizeName(package.get_name()) + ' {\n'
            text += Graphviz.getPackageText(package)
            text += '}'
            return text
        elif package is None:
            return 'Package not found!'
        else:
            return 'Passed object is not a package!'

    @staticmethod
    def getPackageText(package):
        text = ''

        for dependence in package.get_dependencies():
            dep_name = Graphviz.normalizeName(dependence.get_name())
            text += '\t{} -> {};\n'.format(Graphviz.normalizeName(package.get_name()), dep_name)
            text += Graphviz.getPackageText(dependence)

        return text

    @staticmethod
    def normalizeName(string):
        if not re.search(r'^[0-9a-zA-Z]+$', string):
            string = '\"' + string + '\"'

        return string
