# pylint: disable-msg=too-few-public-methods
#effective population
import configparser
import os

config = configparser.ConfigParser()
path = os.path.abspath('config.ini')
config.read(path)

class IndicatorThree():
    def __init__(self):
        pass

    def category(self, males, females, herdbook):
        result = self._find_score(males, females)
        if herdbook == 1:
            result += 1
            if result == 6:
                result = 5
        return result

    @staticmethod
    def _find_score(males, females):
        if (males <= 0) or (females <= 0):
            return 5
        catagories = ([[i, config.getfloat('inbreeding threshold', str(i))]
                       for i in range(0, 6)])

        delta = ((1.0 / (8 * males)) + (1.0 / (8 * females)))
        percentage = round((delta * 100), 2)

        for i in catagories:
            if percentage < i[1]:
                return i[0]
