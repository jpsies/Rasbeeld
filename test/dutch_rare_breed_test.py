# pylint: disable-msg=too-many-instance-attributes
import unittest
from dutch_rare_breeds.lib.analysis.core import Analysis
from dutch_rare_breeds.lib.analysis.indicator_one import IndicatorOne
from dutch_rare_breeds.lib.analysis.indicator_two import IndicatorTwo
from dutch_rare_breeds.lib.analysis.indicator_three import IndicatorThree
from dutch_rare_breeds.lib.analysis.indicator_four import IndicatorFour
from dutch_rare_breeds.lib.analysis.indicator_five import IndicatorFive
from dutch_rare_breeds.lib.analysis.indicator_six import IndicatorSix

class TestIndicators(unittest.TestCase):

    def test_indicator_one(self):
        self.species = 'rund'
        self.factor_one = 600
        assert IndicatorOne().category(self.species, self.factor_one) == 4

    def test_indicator_two_min(self):
        self.factor_two = 5
        assert IndicatorTwo().category(self.factor_two) == 5

    def test_indicator_two_max(self):
        self.factor_two = 1
        assert IndicatorTwo().category(self.factor_two) == 5

    def test_indicator_three_min(self):
        self.males = 5000
        self.females = 10000
        self.herdbook = 2
        assert IndicatorThree().category(self.males, self.females, self.herdbook) == 0

    def test_indicator_three_middle(self):
        self.males = 20
        self.females = 10000
        self.herdbook = 1
        assert IndicatorThree().category(self.males, self.females, self.herdbook) == 4

    def test_indicator_three_max(self):
        self.males = 5
        self.females = 100
        self.herdbook = 1
        assert IndicatorThree().category(self.males, self.females, self.herdbook) == 5

    def test_indicator_four_min(self):
        self.provinces = ['Groningen', 'Drenthe', 'Zeeland']
        self.abroad = 0
        assert IndicatorFour().category(self.provinces, self.abroad) == 1

    def test_indicator_four_max(self):
        self.provinces = ['Groningen']
        self.abroad = 1
        assert IndicatorFour().category(self.provinces, self.abroad) == 5

    def test_indicator_five_min(self):
        self.factor_five = 0
        self.factor_six = 0
        self.factor_seven = 0
        self.factor_eight = 0
        self.factor_nine = 0
        self.weights = [1.0, 1.0, 1.2, 0.8, 1]
        self.answers = [self.factor_five, self.factor_six, self.factor_seven, self.factor_eight, self.factor_nine]
        assert IndicatorFive().category(self.answers, self.weights) == 0

    def test_indicator_five_max(self):
        self.factor_five = 2
        self.factor_six = 2
        self.factor_seven = 2
        self.factor_eight = 2
        self.factor_nine = 2
        self.weights = [1.0, 1.0, 1.2, 0.8, 1]
        self.answers = [self.factor_five, self.factor_six, self.factor_seven, self.factor_eight, self.factor_nine]
        assert IndicatorFive().category(self.answers, self.weights) == 5

    def test_indicator_six_min(self):
        self.species = 'rund'
        self.factor_ten = 0
        self.factor_eleven = 0
        self.factor_twelve = 0
        self.factor_thirteen = 0
        self.factor_fourteen = 0
        self.weights = [1.0, 1.0, 1.2, 0.8, 1]
        self.answers = [self.factor_ten, self.factor_eleven, self.factor_twelve, self.factor_thirteen, self.factor_fourteen]
        assert IndicatorSix().category(self.species, self.answers, self.weights) == 0

    def test_indicator_six_middle(self):
        self.species = 'rund'
        self.factor_ten = 1
        self.factor_eleven = 1
        self.factor_twelve = 1
        self.factor_thirteen = 1
        self.factor_fourteen = 1
        self.weights = [1.0, 1.0, 1.2, 0.8, 1]
        self.answers = [self.factor_ten, self.factor_eleven, self.factor_twelve, self.factor_thirteen, self.factor_fourteen]
        assert IndicatorSix().category(self.species, self.answers, self.weights) == 2

    def test_indicator_six_max(self):
        self.species = 'rund'
        self.factor_ten = 2
        self.factor_eleven = 2
        self.factor_twelve = 2
        self.factor_thirteen = 2
        self.factor_fourteen = 2
        self.weights = [1.0, 1.0, 1.2, 0.8, 1]
        self.answers = [self.factor_ten, self.factor_eleven, self.factor_twelve, self.factor_thirteen, self.factor_fourteen]
        assert IndicatorSix().category(self.species, self.answers, self.weights) == 5
