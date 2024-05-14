
def test(api):
    try:
        api.blackScreenMask = ['blackScreen-mask', (1, 1, 1919, 1079), (650, 300, 1280, 750, 1)]
        if api.UIName == 'carbon':
            if api.projectName == 'raphael':
                api.lightChannelListMask = ['lightChannelList-mask', (25, 200, 650, 870)]
                api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (400, 200, 1560, 915)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (106, 45, 1810, 1030)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (30, 60, 1060, 935)]
            elif api.projectName == 'yoda':
                api.lightChannelListMask = ['lightChannelList-mask', (40, 130, 605, 860)]
                api.infoBarMask = ['infoBar-mask', (1, 840, 1919, 1079), (1, 920, 1919, 1020, 1), (1590, 855, 1760, 915, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (400, 200, 1560, 915)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (200, 60, 1790, 900)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (30, 60, 1060, 935)]
            else:
                api.lightChannelListMask = ['lightChannelList-mask', (40, 130, 690, 870)]
                api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (396, 118, 1567, 878)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (106, 45, 1810, 1030)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (8, 30, 689, 1059)]
        elif api.UIName == 'panasonic':
            if api.projectName == 'michelangelo':
                api.lightChannelListMask = ['lightChannelList-mask', (25, 200, 650, 870)]
                api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (400, 200, 1560, 915)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (106, 45, 1810, 1030)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (30, 60, 1060, 935)]
            else:
                api.lightChannelListMask = ['lightChannelList-mask', (40, 130, 690, 870)]
                api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (396, 118, 1567, 878)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (106, 45, 1810, 1030)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (8, 30, 689, 1059)]
        elif api.UIName == 'titanium':
            if api.projectName == 'raphael':
                api.lightChannelListMask = ['lightChannelList-mask', (25, 200, 650, 870)]
                api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (400, 200, 1560, 915)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (106, 45, 1810, 1030)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (30, 60, 1060, 935)]
            elif api.projectName == 'yoda':
                api.lightChannelListMask = ['lightChannelList-mask', (40, 130, 605, 860)]
                api.infoBarMask = ['infoBar-mask', (1, 840, 1919, 1079), (1, 920, 1919, 1020, 1), (1590, 855, 1760, 915, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (400, 200, 1560, 915)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (200, 60, 1790, 900)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (30, 60, 1060, 935)]
            else:
                api.lightChannelListMask = ['lightChannelList-mask', (40, 130, 690, 870)]
                api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 1079, 1)]
                api.filterChannelListMask = ['filterChannelList-mask', (396, 118, 1567, 878)]
                api.advanceChannelListMask = ['advanceChannelList-mask', (106, 45, 1810, 1030)]
                api.enterPINWithoutInfoBar = ['enterPINWithoutInfoBar-mask', (680, 430, 1919, 890)]
                api.quickMenuMask = ['quickMenu-mask', (8, 30, 689, 1059)]
    except:
        api.printError()

