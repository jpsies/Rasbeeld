def setup_routes(config):
    config.add_route('home', '/')
    config.add_route('save', '/save')
    config.add_route('saved', '/saved/{risk_factor_uuid}')
    config.add_route('status', '/status/{selectedspecies}/{selectedbreed}/{association}')
    config.add_route('form', '/form/{risk_factor_uuid}')
    config.add_route('contact', '/contact')
    config.add_route('admin', '/admin')
    config.add_route('new_entry', '/new_entry')
    config.add_route('saved_entry', '/saved_entry/{risk_factor_uuid}/{message}')

    config.add_route('api_species', '/api/species')
    config.add_route('api_breed', '/api/breed/{selectedspecies}')
    config.add_route('api_association', '/api/association/{selectedbreed}')
