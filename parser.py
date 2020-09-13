import json
import requests
from bs4 import BeautifulSoup


class NpmParser:
    url = "https://www.npmjs.com/package/"
    dependence = "bootstrap-fileinput"

    @staticmethod
    def getDependencies(dependence):
        page = requests.get(NpmParser.url + dependence)
        soup = BeautifulSoup(page.text, 'html.parser')
        json_str = str(soup.find_all('script')[1].contents[0])[21:]
        json_object = json.loads(json_str)["context"]

        if 'packageVersion' not in json_object:
            raise NameError('Package \'' + dependence + '\' not found')

        return json_object["packageVersion"]["dependencies"]
