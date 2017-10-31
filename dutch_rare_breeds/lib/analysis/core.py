# pylint: disable-msg=too-few-public-methods
# pylint: disable-msg=no-else-return
# pylint: disable-msg=len-as-condition
import configparser
import os
from dutch_rare_breeds.lib.db.model import risk_factors, breeds, species
from dutch_rare_breeds.lib import answers
from . import indicator_one, indicator_two, indicator_three, indicator_four, indicator_five, indicator_six

config = configparser.ConfigParser()
path = os.path.abspath('config.ini')
config.read(path)

class Analysis():

    def __init__(self):
        pass

    def reportData(self, breed_id, name_association):
        data_risk_factor = self._retrieve_risk_factors_data(breed_id, name_association)
        data_species = self._retrieve_species_data(data_risk_factor.species)
        indicator_one = self.indicatorOne(data_species, data_risk_factor)
        indicator_two = self.indicatorTwo(data_risk_factor)
        indicator_three = self.indicatorThree(data_risk_factor)
        indicator_four = self.indicatorFour(data_risk_factor)
        indicator_five = self.indicatorFive(data_risk_factor)
        indicator_six = self.indicatorSix(data_species, data_risk_factor)
        return data_risk_factor.id, indicator_one, indicator_two, indicator_three, indicator_four, indicator_five, indicator_six

    @staticmethod
    def indicatorOne(data_species, data_risk_factor):
        N_breeding_females = data_risk_factor.N_breeding_females
        getvalue = indicator_one.IndicatorOne()
        value = getvalue.category(data_species.name, N_breeding_females)
        return value

    @staticmethod
    def indicatorTwo(data_risk_factor):
        N_breeding_females = data_risk_factor.N_breeding_females
        getvalue = indicator_two.IndicatorTwo()
        value = getvalue.category(N_breeding_females)
        return value

    @staticmethod
    def indicatorThree(data_risk_factor):
        N_breeding_females = data_risk_factor.N_breeding_females
        N_breeding_males = data_risk_factor.N_breeding_males
        herdbook_situation = data_risk_factor.herdbook
        getvalue = indicator_three.IndicatorThree()
        value = getvalue.category(N_breeding_females, N_breeding_males, herdbook_situation)
        return value

    @staticmethod
    def indicatorFour(data_risk_factor):
        provinces = data_risk_factor.provinces
        provincelist = answers.provinces(provinces)
        breed_present_abroad = data_risk_factor.breed_present_abroad
        getvalue = indicator_four.IndicatorFour()
        value = getvalue.category(provincelist, breed_present_abroad)
        return value

    def indicatorFive(self, data_risk_factor):
        association = self._check_name_association(data_risk_factor.name_association)
        elements_breeding_program_score = self._score_breeding_program(data_risk_factor.elements_breeding_program)
        cryobank_score = self._cryobank_scoring(data_risk_factor.cryobank)
        herdbook = data_risk_factor.herdbook
        activities_score = self._activities(data_risk_factor.activities)
        promotion_score = self._promotion(data_risk_factor.promotion)
        answers = [association, elements_breeding_program_score, cryobank_score, herdbook, activities_score, promotion_score]
        weights = [1, 1, 1, 1, 1, 1]
        getvalue = indicator_five.IndicatorFive()
        value = getvalue.category(answers, weights)
        return value

    def indicatorSix(self, data_species, data_risk_factor):
        breeding_limitations_score = self._limitations(data_risk_factor.breeding_limitations)
        professional_members_score = self._prof_scoring(data_risk_factor.professional_members)
        profitable_output = data_risk_factor.profitable_output
        specialty_use = data_risk_factor.specialty_use
        governmental_support_score = self._government_score(data_risk_factor.governmental_support)
        continuity_breeding = data_risk_factor.continuity_breeding
        answers = [
            breeding_limitations_score,
            professional_members_score,
            profitable_output,
            specialty_use,
            governmental_support_score,
            continuity_breeding
        ]
        weights = [1, 1, 1, 1, 1, 1]
        getvalue = indicator_six.IndicatorSix()
        value = getvalue.category(species, answers, weights)
        return value

    @staticmethod
    def _score_breeding_program(elements_breeding_program):
        if elements_breeding_program == '':
            return 2
        elif len(elements_breeding_program) == 1:
            return 1
        elif len(elements_breeding_program) >= 2:
            return 0

    @staticmethod
    def _government_score(governmental_support):
        if governmental_support == '':
            return 2
        elif len(governmental_support) == 0:
            return 1
        elif len(governmental_support) == 1:
            return 1
        else:
            return 0

    @staticmethod
    def _check_name_association(name_association):
        if name_association != '':
            return 0
        else:
            return 1

    @staticmethod
    def _cryobank_scoring(cryobank):
        if cryobank == 0:
            return 0
        else:
            return 2

    @staticmethod
    def _activities(activities):
        if activities == '':
            return 2
        elif len(activities) >= 5:
            return 0
        elif len(activities) <= 4 & len(activities) >= 2:
            return 1
        else:
            return 2

    @staticmethod
    def _promotion(promotion):
        if promotion == '':
            return 2
        elif len(promotion) >= 4:
            return 0
        elif len(promotion) <= 3 & len(promotion) >= 2:
            return 1
        else:
            return 2

    @staticmethod
    def _limitations(limitations):
        if limitations == '':
            return 0
        elif len(limitations) >= 5:
            return 0
        elif len(limitations) <= 4 & len(limitations) >= 3:
            return 1
        else:
            return 2

    @staticmethod
    def _prof_scoring(professional_members):
        if professional_members == 0:
            return 2
        elif professional_members == 1:
            return 1
        elif professional_members == 2:
            return 0
        elif professional_members == 3:
            return 0
        elif professional_members == 4:
            return 2

    @staticmethod
    def _retrieve_risk_factors_data(breed_id, name_association):
        data_risk_factor = risk_factors.get_most_recent_risk_factors_by_breed_id(breed_id, name_association)
        return data_risk_factor

    @staticmethod
    def _retrieve_species_data(risk_factor_species):
        data_species = species.get_species(risk_factor_species)
        return data_species
