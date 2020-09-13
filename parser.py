import json
import requests
from package import Package


class NpmParser:
    url = 'https://registry.npmjs.org/'

    @staticmethod
    def getPackageJson(package):
        #print('Parsing ' + package)
        try:
            page = requests.get(NpmParser.url + package)
            json_object = json.loads(page.text)

            if 'error' in json_object or 'dist-tags' not in json_object or 'versions' not in json_object:
                #print('Package \'' + package + '\' not found')
                return None

            return json_object['versions'][json_object['dist-tags']['latest']]
        except IndexError:
            return None

    @staticmethod
    def getPackageVersion(package):
        json_object = NpmParser.getPackageJson(package)

        if json_object is not None and 'version' in json_object:
            return json_object['version']

        return None

    @staticmethod
    def getDependenciesJson(dependence):
        json_object = NpmParser.getPackageJson(dependence)

        if json_object is not None and 'dependencies' in json_object:
            return json_object['dependencies']

        return None

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
