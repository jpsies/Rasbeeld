$( document ).ready(function() {
    selectSpecies()
    $('body').on('change', '#mySelectSpecies', selectBreed);
    $('body').on('change', '#mySelectBreed', selectAssociation);
    $('body').on('change', '#mySelectAssociation', function(){
        disable_send_button(false)
    });
    $('body').on('click', '#requestStatus', requestStatus)
});
