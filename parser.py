import json
import requests
from package import Package
from bs4 import BeautifulSoup


class NpmParser:
    url = 'https://www.npmjs.com/package/'

    @staticmethod
    def getPackageJson(package):
        #print('Parsing ' + package)
        try:
            page = requests.get(NpmParser.url + package)
            soup = BeautifulSoup(page.text, 'html.parser')
            json_str = str(soup.find_all('script')[1].contents[0])[21:]
            json_object = json.loads(json_str)['context']

            if 'packageVersion' not in json_object:
                #print('Package \'' + package + '\' not found')
                return None

            return json_object['packageVersion']
        except IndexError:
            return None

    @staticmethod
    def getPackageVersion(package):
        json_object = NpmParser.getPackageJson(package)

        if json_object is not None:
            return NpmParser.getPackageJson(package)['version']

        return None

    @staticmethod
    def getDependenciesJson(dependence):
        json_object = NpmParser.getPackageJson(dependence)

        if json_object is not None and 'dependencies' not in json_object:
            return None

        return json_object['dependencies']

    @staticmethod
    def getDependenciesList(package):
        dep_list = []
        json_object = NpmParser.getDependenciesJson(package)

        if json_object is not None:
            for name, version in json_object.items():
                package = Package(name, version)
                package.set_dependencies(NpmParser.getDependenciesList(name))
                dep_list.append(package)

        return dep_list

    @staticmethod
    def getPackage(name):
        package_version = NpmParser.getPackageVersion(name)

        if package_version is None:
            return None

        root_package = Package(name, NpmParser.getPackageVersion(name))
        root_package.set_dependencies(NpmParser.getDependenciesList(name))
        return root_package
