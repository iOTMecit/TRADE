
def test(api):
    try:
        if api.UIName == 'carbon':
            api.txtMask = ['txt-mask', (1, 1, 1919, 900), (1000, 1, 1919, 65, 1), (1, 1010, 1919, 1079, 1)]
            api.infoBarMask = ['infoBar-mask', (1, 840, 1919, 1079), (1, 920, 1919, 1015, 1), (1600, 860, 1760, 915, 1)]
            api.txtPageNoMask = ['txt-pageNo', (90, 5, 275, 60)]
            api.txtNotAvailable = ['txt-notAvailable', (545, 405, 1280, 555)]
        elif api.UIName == 'panasonic' or api.UIName == 'titanium':
            if api.projectName == 'raphael':
                api.txtNotAvailable = ['txt-notAvailable', (670, 315, 1265, 615)]
            else:
                api.txtNotAvailable = ['txt-notAvailable', (680, 420, 1260, 540)]
            api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
            api.txtMask = ['txt-mask', (1, 1, 1919, 900), (1, 485, 1919, 605, 1), (1000, 1, 1919, 75, 1)]
            api.txtPageNoMask = ['txt-pageNo', (90, 5, 275, 60)]
    except:
        api.printError()

