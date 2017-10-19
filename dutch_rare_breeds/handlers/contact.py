from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='contact', renderer='../templates/contact.pt')
def setup_contact_page(request):
    """ Setup the home page
    """
    # config = request.registry.settings
    return {'title':'Zeldzame Huisdierrassen Nederland'}
