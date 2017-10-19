function remove_options(select, default_option){
    select
        .find('option')
        .remove()
        .end()
        .append('<option disabled selected>' + default_option + '</option>')
    ;
}

function disable_send_button(value=true) {
    $('#requestStatus').prop('disabled', value)
}

function requestStatus() {
    url = '/status/' + $('#mySelectSpecies').val() + '/' + $('#mySelectBreed').val() + '/' + $('#mySelectAssociation').val()
    window.location.replace(url )
}

function selectSpecies() {
    disable_send_button(true)
    var endpoint = '/api/species'
    var select = $('#mySelectSpecies')
    retrieveAndSetData(endpoint, select)
}

function selectBreed() {
    disable_send_button(true)
    remove_options($('#mySelectBreed'), 'Kies ras')
    remove_options($('#mySelectAssociation'), 'Kies vereniging')

    var endpoint = '/api/breed/' + $('#mySelectSpecies').val()
    var select = $('#mySelectBreed')
    retrieveAndSetData(endpoint, select)
}

function selectAssociation() {
    disable_send_button(true)
    remove_options($('#mySelectAssociation'), 'Kies vereniging')

    var endpoint = '/api/association/' + $('#mySelectBreed').val()
    var select = $('#mySelectAssociation')
    retrieveAndSetData(endpoint, select)
}

function retrieveAndSetData(endpoint, select) {
    $.get(endpoint).done(function( data ) {
        data_array = data["data"]
        for (var i = 0; i < data_array.length; i++){
            select.append($('<option>', { value : data_array[i][0] })
          .text(data_array[i][1])); 
        }
    });
};