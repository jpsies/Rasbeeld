# pylint: disable-msg=too-many-locals
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from dutch_rare_breeds.lib.analysis import Analysis
from dutch_rare_breeds.lib.db.model import risk_factors, breeds, species
from dutch_rare_breeds.lib import answers

@view_config(route_name='status', renderer='../templates/status.pt')
def setup_status_page(request):
    """ Setup the status page
    """
    species_id = request.matchdict['selectedspecies']
    breed_id = request.matchdict['selectedbreed']
    selected_association = request.matchdict['association']


    data_risk_factor = risk_factors.get_most_recent_risk_factors_by_breed_id(breed_id, selected_association)
    species_name = species.get_species(species_id)
    breed = breeds.get_breed(breed_id)
    if data_risk_factor.continuity_breeding is not None:
        continuity_breeding_answer = answers.continuity_breeding(data_risk_factor.continuity_breeding)
        provinces_answer = answers.provinces(data_risk_factor.provinces)
        abroad_answer = answers.abroad(data_risk_factor.breed_present_abroad)
        promotion_answer = answers.promotion(data_risk_factor.promotion)
        activities_answer = answers.activities(data_risk_factor.activities)
        herdbook_answer = answers.herdbook(data_risk_factor.herdbook)
        elements_breeding_program_answer = answers.elements_breeding_program(data_risk_factor.elements_breeding_program)
        cryobank_answer = answers.cryobank(data_risk_factor.cryobank)
        limitations_answer = answers.limitations(data_risk_factor.breeding_limitations)
        professional_members_answer = answers.professional_members(data_risk_factor.professional_members)
        profitable_output_answer = answers.profitable_output(data_risk_factor.profitable_output)
        specialty_use_answer = answers.specialty_use(data_risk_factor.specialty_use)
        governmental_support_answer = answers.governmental_support(data_risk_factor.governmental_support)

        analysis = Analysis()
        data = analysis.reportData(breed_id, selected_association)
        data_risk_factor = risk_factors.get_risk_factor(data[0])
        radarvalues = [data[1], data[2], data[3], data[4], data[5], data[6]]
        message = ''
    else:
        message = 'Geen rapport en analyse beschikbaar'
        continuity_breeding_answer = ''
        provinces_answer = ''
        abroad_answer = ''
        promotion_answer = ''
        activities_answer = ''
        herdbook_answer = ''
        elements_breeding_program_answer = ''
        cryobank_answer = ''
        limitations_answer = ''
        professional_members_answer = ''
        profitable_output_answer = ''
        specialty_use_answer = ''
        governmental_support_answer = ''
        radarvalues = ''

    edit_link = '/form/{}'.format(data_risk_factor.id)

    # config = request.registry.settings
    return {
        'title':'Status',
        'association':data_risk_factor.name_association,
        'species':species_name,
        'breed':breed,
        'trend_N_breeding_females':'Trend in number of breeding females',
        'N_breeding_females':data_risk_factor.N_breeding_females,
        'N_breeding_males':data_risk_factor.N_breeding_males,
        'N_breed_keeping_members':data_risk_factor.N_breed_keeping_members,
        'N_active_breeders':data_risk_factor.N_active_breeders,
        'continuity_breeding':continuity_breeding_answer,
        'provinces':', '.join(provinces_answer),
        'abroad':abroad_answer,
        'abroad_examples':data_risk_factor.abroad_examples,
        'promotion':', '.join(promotion_answer),
        'activities':', '.join(activities_answer),
        'herdbook':herdbook_answer,
        'elements_breeding_program':elements_breeding_program_answer,
        'cryobank':cryobank_answer,
        'breeding_limitations':', '.join(limitations_answer),
        'professional_members':professional_members_answer,
        'profitable_output':profitable_output_answer,
        'output_examples':data_risk_factor.output_examples,
        'specialty_use':specialty_use_answer,
        'specialty_examples':data_risk_factor.specialty_examples,
        'governmental_support':governmental_support_answer,
        'support_examples':data_risk_factor.support_examples,
        'radar':radarvalues,
        'edit_link': edit_link,
        'message':message
    }
