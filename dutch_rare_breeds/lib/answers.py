# pylint: disable-msg=no-else-return
def continuity_breeding(value):
    ability = ['bijna allemaal', 'helft', 'bijna geen']
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
    presence = ['Ja', 'Nee']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def promotion(value):
    promotionlist = ['een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven']
    return [promotionlist[int(i)] for i in value.split(',')]

def activities(value):
    activitylist = ['een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven']
    return [activitylist[int(i)] for i in value.split(',')]

def herdbook(value):
    presence = ['open', 'gesloten', 'geen stamboek']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def elements_breeding_program(value):
    presence = ['database', 'stimuleren mannelijke dieren', 'fokdoelen']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def cryobank(value):
    presence = ['Ja', 'Nee']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def limitations(value):
    if value == '':
        return value
    else:
        limitationlist = ['een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven']
        value = [limitationlist[int(i)] for i in value.split(',')]
    return value

def professional_members(value):
    members = ['meer dan 20%', 'tot 20%', 'geen']
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
    presence = ['Ja', 'Nee']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)

def governmental_support(value):
    presence = ['Ja', 'Nee']
    if isinstance(value, int):
        return presence[value]
    else:
        return presence.index(value)
