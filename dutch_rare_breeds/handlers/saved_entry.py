from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from dutch_rare_breeds.lib.db.model import risk_factors, breeds, species
from dutch_rare_breeds.lib.analysis import Analysis

@view_config(route_name='saved_entry', renderer='../templates/saved_entry.pt')
def setup_home_page(request):
    """ Setup the saved page
    """

    #breed_id = request.GET.get('breed_id', '')
    risk_factor_uuid = request.matchdict['risk_factor_uuid']
    message = request.matchdict['message']
    data_risk_factor = risk_factors.get_risk_factor(risk_factor_uuid)
    data_breed = breeds.get_breed(data_risk_factor.breed)
    data_species = species.get_species(data_risk_factor.species)

    if message == 'True':
        message = 'al opgeslagen.'
    else:
        message = 'succesvol toegevoegd.'

    return {
        'title': 'Nieuwe invoer',
        'breed':data_breed,
        'species':data_species,
        'name_association': data_risk_factor.name_association,
        'message': message
    }
