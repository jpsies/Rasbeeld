# pylint: disable-msg=too-few-public-methods
#Socio-economic variable
import configparser

class IndicatorSix():

    def __init__(self):
        pass

    def category(self, species, answers, weights):
        result = self._find_score(answers, weights)
        return result

    @staticmethod
    def _find_score(answers, weights):
        """
answers = a list of integers 0, 1, or 2
weigths = a list of weights
        """
        #checks if correct weights are used
        if sum(weights) != len(weights) or len(weights) != len(answers):
            return "Wrong weights used!"

        factor = 0
        for i, answer in enumerate(answers):
            factor += answer*weights[i]

        return round(factor/len(answers)*5/2, 0)
        #normalizes to a value between 0 and 5
