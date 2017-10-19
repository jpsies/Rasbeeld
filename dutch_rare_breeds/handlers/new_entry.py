import uuid
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from dutch_rare_breeds.lib.db.model.meta import DBSession as session
from dutch_rare_breeds.lib.db.model import risk_factors, breeds, species
from dutch_rare_breeds.lib.db.model import (
    Breed,
    Species,
    RiskFactor
)

@view_config(route_name='new_entry', request_method='POST')
def setup_new_entry_page(request):

    species_name = request.POST.get('species', '')
    breed_name = request.POST.get('breed', '')
    name_association = request.POST.get('association', '')
    message = False

    if species.get_species_by_name(species_name) is None:
        species_uuid = uuid.uuid4()
        new_species = Species(
            id=species_uuid,
            name=species_name
        )
        session.add(new_species)
        session.commit()
    else:
        species_db = species.get_species_by_name(species_name)
        species_uuid = species_db.id

    if breeds.get_breed_by_name(breed_name) is None:
        breed_uuid = uuid.uuid4()
        new_breed = Breed(
            id=breed_uuid,
            name=breed_name
        )
        session.add(new_breed)
        session.commit()
    else:
        breed_db = breeds.get_breed_by_name(breed_name)
        breed_uuid = breed_db.id

    if (species.get_species_by_name(species_name) is not None) & (breeds.get_breed_by_name(breed_name) is not None):
        breed_db = breeds.get_breed_by_name(breed_name)
        breed_uuid = breed_db.id
        if risk_factors.get_most_recent_risk_factors_by_breed_id(breed_uuid, name_association) is None:
            risk_factor_uuid = uuid.uuid4()
            new_risk_factor = RiskFactor(
                id=risk_factor_uuid,
                species=species_uuid,
                breed=breed_uuid,
                name_association=name_association,
            )
            session.add(new_risk_factor)
            session.commit()
        else:
            risk_factor_data = risk_factors.get_most_recent_risk_factors_by_breed_id(breed_uuid, name_association)
            risk_factor_uuid = risk_factor_data.id
            message = True

    return HTTPFound(location=request.route_url('saved_entry', risk_factor_uuid=risk_factor_uuid, message=message))
