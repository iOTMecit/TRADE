
def test(api):
    try:
        api.EPGChannelNameMask = ['EPGChannelName-mask', (1, 1, 1919, 1079), (1550, 65, 1919, 130, 1), (1, 190, 1919, 260, 1), (1, 260, 1919, 340, 1), (1, 340, 1919, 950, 1)]
        api.timeshiftInfoBar = ['timeshiftInfoBar-mask', (5, 910, 1180, 960)]
        api.TimerMask = ['Timer-mask', (110, 150, 1800, 830)]
        if api.UIName == 'carbon' or api.UIName == 'titanium':
            api.timeshiftNotAvailable = ['timeshiftNotAvailable-mask', (670, 320, 1270, 615)]
            api.infoBarMask = ['infoBar-mask', (1, 840, 1919, 1079), (1, 920, 1919, 1015, 1), (1600, 860, 1760, 915, 1)]
            api.EPGChannelListMask = ['EPGChannelList-mask', (30, 200, 620, 965)]
            api.EPGFilterMask = ['EPGFilter-mask', (315, 170, 1605, 905)]
        elif api.UIName == 'panasonic':
            if projectName == 'michelangelo':
                api.timeshiftNotAvailable = ['timeshiftNotAvailable-mask', (665, 405, 1280, 620)]
            elif projectName == 'raphael':
                api.timeshiftNotAvailable = ['timeshiftNotAvailable-mask', (550, 410, 1260, 670)]
            api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1760, 850, 1910, 1075, 1)]
            api.EPGChannelListMask = ['EPGChannelList-mask', (70, 265, 545, 950)]
            api.EPGFilterMask = ['EPGFilter-mask', (400, 200, 1565, 920)]
    except:
        api.printError()

