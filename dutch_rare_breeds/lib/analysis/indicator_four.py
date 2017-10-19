# pylint: disable-msg=too-few-public-methods
#Spread across provinces
import configparser
import math
import os

config = configparser.ConfigParser()
path = os.path.abspath('config.ini')
config.read(path)

coordinates = {
    'Groningen': [53.251468, 6.793511],
    'Friesland': [53.083172, 5.917473],
    'Drenthe': [52.853667, 6.578472],
    'Overijssel': [52.437432, 6.442630],
    'Gelderland': [52.110404, 5.978711],
    'Flevoland': [52.521629, 5.631785],
    'Utrecht': [52.106920, 5.155217],
    'Noord-Brabant': [51.605863, 5.162783],
    'Limburg': [51.218738, 5.982791],
    'Noord-Holland': [52.639663, 4.879977],
    'Zuid-Holland': [52.068358, 4.550403],
    'Zeeland': [51.529053, 3.872955]}

class IndicatorFour():
    def __init__(self):
        pass

    def category(self, provinces, abroad):
        provincescore = self._find_score(provinces)
        if abroad == 0:
            result = provincescore - 1
        else:
            result = provincescore
        return result

    @staticmethod
    def _find_score(provinces):

        def Euclidean(x, y):
            d = 0.0
            for i, dimension in enumerate(x):
                d += math.sqrt((x[i]-y[i])**2)
            return d

        def distance(prov):
            li = [coordinates[i] for i in prov]
            d = [Euclidean(i, j) for i in li for j in li]
            return sum(set(d))

        catagories = ([[i, config.getfloat('province threshold', str(i))]
                       for i in range(5, 0, -1)])
        dist = distance(provinces)
        for i in catagories:
            if dist < i[1]:
                return i[0]
