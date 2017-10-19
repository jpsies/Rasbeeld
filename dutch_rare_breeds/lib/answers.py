# pylint: disable-msg=no-else-return
def continuity_breeding(value):
    ability = ['Vrijwel alle huidige fokkers', 'De helft van de huidige fokkers', 'Vrijwel geen van de huidige fokkers']
    if isinstance(value, int):
        return ability[value]
    else:
        return ability.index(value)

def provinces(value):
    if value == '':
        return value
    else:
        provincelist = [
            'Groningen',
            'Friesland',
            'Drenthe',
            'Overijssel',
            'Flevoland',
            'Gelderland',
            'Utrecht',
            'Noord-Holland',
            'Zuid-Holland',
            'Zeeland',
            'Noord-Brabant',
            'Limburg'
        ]
        value = [provincelist[int(i)] for i in value.split(',')]
    return value

def abroad(value):
    presence = ['Ja', 'Nee', 'Onbekend']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def promotion(value):
    promotionlist = [
        'Website',
        'Sociale media',
        'Evenementen of jaarmarkten',
        'Tentoonstellingen toegankelijk voor niet leden',
        'Artikelen in tijdschriften',
        'Crowdfunding',
        'Anders'
    ]
    return [promotionlist[int(i)] for i in value.split(',')]

def activities(value):
    activitylist = [
        'Algemene ledenvergadering',
        'Keuringen',
        'Cursus',
        'Show evenement',
        'Sportevenement',
        'Excursie',
        'Gastspreker',
        'Nieuwsbrief of clubblad',
        'Merchandise',
        'Anders, namelijk'
    ]
    return [activitylist[int(i)] for i in value.split(',')]

def herdbook(value):
    presence = ['Ja, een gesloten stamboek', 'Ja een open stamboek', 'Nee']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def elements_breeding_program(value):
    presence = [
        'Ja, de gegevens worden vastgelegd in een centrale database',
        'Ja, de vereniging stimuleert diversiteit in het gebruik van mannelijke fokdieren',
        'Ja, de vereniging geeft paringsadvies'
    ]
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def cryobank(value):
    presence = ['Ja', 'Nee', 'Niet bekend']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def limitations(value):
    if value == '':
        return value
    else:
        limitationlist = [
            'Verandering in beschikbaarheid van land of ruimte',
            'Verandering in beschikbaarheid van dieren',
            'Nieuwe regelgeving m.b.t. vaccinaties',
            'Nieuwe regelgeving m.b.t. emissies',
            'Overige nieuwe regelgeving',
            'Kennis bij nieuwe leden over het houden of fokken van het ras',
            'Aanschafprijs van de dieren',
            'Afzet van overtollige dieren',
            'Lokale overlast door de dieren',
            'Overschot van mest',
            'Anders'
            ]
        value = [limitationlist[int(i)] for i in value.split(',')]
    return value

def professional_members(value):
    members = [
        'Minder dan 1%',
        'Tussen 1% en 11%',
        'Tussen 11% en 30%',
        'Meer dan 30%',
        'Onbekend'
    ]
    if isinstance(value, int):
        return members[value]
    else:
        return members.index(value)

def profitable_output(value):
    presence = ['Ja', 'Nee']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def specialty_use(value):
    presence = ['Ja', 'Nee', 'Wel in potentie maar (nog) niet in praktijk']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def governmental_support(value):
    presence = [
        'Ja, financieel',
        'Ja, ze stellen land of diensten beschikbaar (Natura)',
        'Ja, anders'
    ]
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)
