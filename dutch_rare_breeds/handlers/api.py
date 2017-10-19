import json
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from dutch_rare_breeds.lib.db.model import risk_factors, breeds, species
from dutch_rare_breeds.lib.db.model.meta import DBSession as session


@view_config(route_name='api_species', renderer='json')
def retrieve_species(request):
    """ Retrieve species from database
    """
    try:
        data = species.get_all_species()
    except Exception:
        session.rollback()
        data = species.get_all_species()

    species_data = []
    for species_name in data:
        species_row = []
        species_row.append(str(species_name.id))
        species_row.append(species_name.name)
        species_data.append(species_row)
    return {'data': species_data}

@view_config(route_name='api_breed', renderer='json')
def retrieve_breeds(request):
    """ Retrieve species from database
    """
    species_id = request.matchdict['selectedspecies']
    breeds_from_risk_factor = risk_factors.get_breed_by_species_id(species_id)
    breeds_data = []
    for breed_id in breeds_from_risk_factor:
        single_breed = breeds.get_breed(breed_id)
        breed_row = []
        breed_row.append(str(single_breed.id))
        breed_row.append(single_breed.name)
        if breed_row not in breeds_data:
            breeds_data.append(breed_row)
    return {'data': breeds_data}

@view_config(route_name='api_association', renderer='json')
def retrieve_associations(request):
    """ Retrieve species from database
    """
    breed_id = request.matchdict['selectedbreed']
    associations_from_breed = risk_factors.get_association_by_breed_id(breed_id)
    association_data = []
    for association in associations_from_breed:
        association_row = []
        association_row.append(association)
        association_row.append(association)
        if association_row not in association_data:
            association_data.append(association_row)
    return {'data': association_data}
