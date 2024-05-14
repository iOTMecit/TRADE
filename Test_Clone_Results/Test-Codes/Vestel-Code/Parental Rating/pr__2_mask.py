
def test(api):
    try:
        if api.UIName == 'carbon':
            api.parentMaturityMask = ['parentMaturity-mask', (30, 380, 1070, 440)]
            api.guidanceMhegEpgMask = ['guidanceMhegEpg-mask', (60, 245, 950, 290)]
        elif api.UIName == 'panasonic':
            api.parentMaturityMask = ['parentMaturity-mask', (20, 320, 1040, 385)]
            api.guidanceMhegEpgMask = ['guidanceMhegEpg-mask', (670, 400, 1250, 680)]
        elif api.UIName == 'titanium':
            api.parentMaturityMask = ['parentMaturity-mask', (0, 365, 490, 425)]
            api.guidanceMhegEpgMask = ['guidanceMhegEpg-mask', (50, 230, 430, 280)]
    except:
        api.printError()

