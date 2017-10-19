# pylint: disable-msg=too-few-public-methods
import configparser
import os

config = configparser.ConfigParser()
path = os.path.abspath('config.ini')
config.read(path)

class IndicatorOne():

    def __init__(self):
        pass

    def category(self, species, value):
        result = self._find_score(species, value)
        return result

    @staticmethod
    def _find_score(species, value):
        li = config["female threshold"][species]

        for i, category in enumerate(li.split()):
            if value > int(category):
                return i
                break
