import configparser
import os
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from dutch_rare_breeds.lib.db.model import risk_factors, breeds, species

config = configparser.ConfigParser()
config.optionxform = lambda option: option
path = os.path.abspath('config.ini')
config.read(path)

@view_config(route_name='form', renderer='../templates/form.pt')
def setup_home_page(request):
    """ Setup the form page
    """
    risk_factor_id = request.matchdict['risk_factor_uuid']

    risk_factor_data = risk_factors.get_risk_factor(risk_factor_id)
    species_data = species.get_species(risk_factor_data.species)
    breed_data = breeds.get_breed(risk_factor_data.breed)

    questions = config["question"]


    # config = request.registry.settings
    data = ['1', '3', '2', '4', '3']
    return {
        'title': 'Vragen',
        'question':questions,
        'data': data,
        'risk_factor_data': risk_factor_data,
        'species': species_data.name,
        'breed': breed_data.name
    }
