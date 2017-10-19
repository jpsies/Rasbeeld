# pylint: disable-msg=too-many-locals
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

@view_config(route_name='save', request_method='POST')
def setup_save_page(request):
    """ Setup the form page
    """
    species_name = request.POST.get('species', '')
    breed_name = request.POST.get('breed', '')
    name_association = request.POST.get('name_association', '')
    N_breeding_females = request.POST.get('N_breeding_females', '')
    N_breeding_males = request.POST.get('N_breeding_males', '')
    N_breed_keeping_members = request.POST.get('N_breed_keeping_members', '')
    N_active_breeders = request.POST.get('N_active_breeders', '')
    continuity_breeding = request.POST.get('continuity_breeding', '')
    provinces = request.POST.getall('provinces')
    breed_present_abroad = request.POST.get('breed_present_abroad', '')
    abroad_examples = request.POST.get('abroad_examples', '')
    promotion = request.POST.getall('promotion')
    activities = request.POST.getall('activities')
    herdbook = request.POST.get('herdbook', '')
    elements_breeding_program = request.POST.get('elements_breeding_program', '')
    cryobank = request.POST.get('cryobank', '')
    breeding_limitations = request.POST.getall('breeding_limitations')
    professional_members = request.POST.get('professional_members', '')
    profitable_output = request.POST.get('profitable_output', '')
    output_examples = request.POST.get('output_examples', '')
    specialty_use = request.POST.get('specialty_use', '')
    specialty_examples = request.POST.get('specialty_examples', '')
    governmental_support = request.POST.get('governmental_support', '')
    support_examples = request.POST.get('support_examples', '')


    species_db = species.get_species_by_name(species_name)
    breed_db = breeds.get_breed_by_name(breed_name)

    if species_db.name != species_name:
        species_uuid = uuid.uuid4()
        new_species = Species(
            id=species_uuid,
            name=species_name
        )
        species_db = new_species
        session.add(new_species)
        session.commit()
    else:
        species_uuid = species_db.id

    if breed_db.name != breed_name:
        breed_uuid = uuid.uuid4()
        new_breed = Breed(
            id=breed_uuid,
            name=breed_name
        )
        session.add(new_breed)
        session.commit()
    else:
        breed_uuid = breed_db.id

    risk_factor_uuid = uuid.uuid4()
    new_risk_factor = RiskFactor(
        id=risk_factor_uuid,
        species=species_uuid,
        breed=breed_uuid,
        name_association=name_association,
        N_breeding_females=int(N_breeding_females),
        N_breeding_males=int(N_breeding_males),
        N_breed_keeping_members=int(N_breed_keeping_members),
        N_active_breeders=int(N_active_breeders),
        continuity_breeding=int(continuity_breeding),
        provinces=','.join(provinces),
        breed_present_abroad=int(breed_present_abroad),
        abroad_examples=abroad_examples,
        promotion=','.join(promotion),
        activities=','.join(activities),
        herdbook=int(herdbook),
        elements_breeding_program=int(elements_breeding_program),
        cryobank=int(cryobank),
        breeding_limitations=','.join(breeding_limitations),
        professional_members=int(professional_members),
        profitable_output=int(profitable_output),
        output_examples=output_examples,
        specialty_use=int(specialty_use),
        specialty_examples=specialty_examples,
        governmental_support=int(governmental_support),
        support_examples=support_examples
    )
    session.add(new_risk_factor)
    session.commit()

    return HTTPFound(location=request.route_url('saved', risk_factor_uuid=risk_factor_uuid))
