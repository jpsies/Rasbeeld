# pylint: disable-msg=too-few-public-methods
#trend
import configparser

class IndicatorTwo():
    def __init__(self):
        pass

    def category(self, values):
        result = self._find_score(values)
        return result

    @staticmethod
    def _find_score(values):
        value = 5
        return value
