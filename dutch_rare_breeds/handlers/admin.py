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


@view_config(route_name='admin', renderer='../templates/admin.pt')
def setup_admin_page(request):
    """ Setup the home page
    """

    # risk_factor_id = request.matchdict['risk_factor_uuid']

    # risk_factor_data = risk_factors.get_risk_factor(risk_factor_id)
    # species_data = species.get_species(risk_factor_data.species)
    # breed_data = breeds.get_breed(risk_factor_data.breed)


    return {'title':'Zeldzame Huisdierrassen Nederland'}
    