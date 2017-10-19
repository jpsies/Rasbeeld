$( document ).ready(function() {
    fill_continuity_breeding()
    fill_provinces()
    fill_breed_present_abroad()
    fill_promotion()
    fill_activities()
    fill_herdbook()
    fill_elements_breeding_program()
    fill_cryobank()
    fill_breeding_limitations()
    fill_professional_members()
    fill_profitable_output()
    fill_specialty_use()
    fill_governmental_support()
});

function fill_continuity_breeding() {
    continuity_breeding = $('#continuity_breeding_value').val()
    switch(continuity_breeding) {
        case '0':
            $('#continuity_1').prop("checked", true)
            break;
        case '1':
            $('#continuity_2').prop("checked", true)
            break;
        case '2':
            $('#continuity_3').prop("checked", true)
            break;
        default:
            $('#continuity_1').prop("checked", true)
    }
}

function fill_provinces() {
    provinces = $('#provinces_value').val().split(',')
    $.each(new Array(12), function(n) {
        if ($.inArray( n.toString(), provinces ) != -1) {
            $('#provinces_' + n).prop("checked", true)
        }
    });
}

function fill_breed_present_abroad() {
    breed_present_abroad = $('#breed_present_abroad_value').val()
    switch(breed_present_abroad) {
        case '0':
            $('#breed_present_abroad_1').prop("checked", true)
            break;
        case '1':
            $('#breed_present_abroad_2').prop("checked", true)
            break;
        default:
            $('#breed_present_abroad_1').prop("checked", true)
    }
}

function fill_promotion() {
    promotion = $('#promotion_value').val().split(',')
    $.each(new Array(7), function(n) {
        if ($.inArray( n.toString(), promotion ) != -1) {
            $('#promotion_' + n).prop("checked", true)
        }
    });
}

function fill_activities() {
    activities = $('#activities_value').val().split(',')
    $.each(new Array(10), function(n) {
        if ($.inArray( n.toString(), activities ) != -1) {
            $('#activities_' + n).prop("checked", true)
        }
    });
}

    function fill_herdbook() {
    herdbook = $('#herdbook_value').val()
    switch(herdbook) {
        case '0':
            $('#herdbook_1').prop("checked", true)
            break;
        case '1':
            $('#herdbook_2').prop("checked", true)
            break;
        case '2':
            $('#herdbook_3').prop("checked", true)
            break;
        default:
            $('#herdbook_1').prop("checked", true)
    }
}

function fill_elements_breeding_program() {
    elements_breeding_program = $('#elements_breeding_program_value').val().split(',')
    $.each(new Array(3), function(n) {
        if ($.inArray( n.toString(), elements_breeding_program ) != -1) {
            $('#elements_breeding_program_' + n).prop("checked", true)
        }
    });
}

    function fill_cryobank() {
    cryobank = $('#cryobank_value').val()
    switch(cryobank) {
        case '0':
            $('#cryobank_1').prop("checked", true)
            break;
        case '1':
            $('#cryobank_2').prop("checked", true)
            break;
        default:
            $('#cryobank_1').prop("checked", true)
    }
}

function fill_breeding_limitations() {
    breeding_limitations = $('#breeding_limitations_value').val().split(',')
    $.each(new Array(11), function(n) {
        if ($.inArray( n.toString(), breeding_limitations ) != -1) {
            $('#breeding_limitations_' + n).prop("checked", true)
        }
    });
}

    function fill_professional_members() {
    professional_members = $('#professional_members_value').val()
    switch(professional_members) {
        case '0':
            $('#professional_members_1').prop("checked", true)
            break;
        case '1':
            $('#professional_members_2').prop("checked", true)
            break;
        case '2':
            $('#professional_members_3').prop("checked", true)
            break;
        case '3':
            $('#professional_members_4').prop("checked", true)
            break;
        case '4':
            $('#professional_members_5').prop("checked", true)
            break;
        default:
            $('#professional_members_1').prop("checked", true)
    }
}

    function fill_profitable_output() {
    profitable_output = $('#profitable_output_value').val()
    switch(profitable_output) {
        case '0':
            $('#profitable_output_1').prop("checked", true)
            break;
        case '1':
            $('#profitable_output_2').prop("checked", true)
            break;
        default:
            $('#profitable_output_1').prop("checked", true)
    }
}

    function fill_specialty_use() {
    specialty_use = $('#specialty_use_value').val()
    switch(specialty_use) {
        case '0':
            $('#specialty_use_1').prop("checked", true)
            break;
        case '1':
            $('#specialty_use_2').prop("checked", true)
            break;
        case '2':
            $('#specialty_use_3').prop("checked", true)
            break;
        default:
            $('#specialty_use_1').prop("checked", true)
    }
}

function fill_governmental_support() {
    governmental_support = $('#governmental_support_value').val().split(',')
    $.each(new Array(3), function(n) {
        if ($.inArray( n.toString(), governmental_support ) != -1) {
            $('#governmental_support_' + n).prop("checked", true)
        }
    });
}