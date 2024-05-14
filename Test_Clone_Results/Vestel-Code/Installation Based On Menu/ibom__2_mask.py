
def test(api):
    try:
        if api.UIName == 'carbon':
            api.channelListMask = ['channelList-mask', (180, 55, 1800, 1025), (210, 180, 1745, 880, 1)]
            api.scrambledMask = ['scrambled-mask', (840, 410, 1190, 475)]
            api.infoBarMask = ['infoBar-mask', (1, 860, 1919, 1079), (1, 955, 1919, 1025, 1), (1600, 880, 1755, 940, 1)]
            api.analogFineTuneIconMask = ['analogFineTuneIcon-mask', (714, 1037, 774, 1079)]
            api.analogFrequancyMask = ['analogFrequancy-mask', (833, 480, 870, 518)]
            api.scanStatisticMask = ['scanStatistic-mask', (90, 55, 355, 95), (65, 185, 205, 510)]
            api.broadcastTypeMask = ['broadcastType-mask', (1650, 1045, 1730, 1070)]
        elif api.UIName == 'panasonic' or api.UIName == 'titanium':
            api.channelListMask = ['channelList-mask', (110, 45, 1815, 1035), (155, 180, 1755, 895, 1)]
            api.scrambledMask = ['scrambled-mask', (675, 400, 1245, 680)]
            api.infoBarMask = ['infoBar-mask', (1, 830, 1919, 1079), (1, 920, 1919, 1005, 1), (1775, 850, 1900, 900, 1)]
            api.analogFineTuneIconMask = ['analogFineTuneIcon-mask', (1220, 487, 1265, 522)]
            api.analogFrequancyMask = ['analogFrequancy-mask', (735, 1030, 770, 1053)]
            api.scanStatisticMask = ['scanStatistic-mask', (90, 30, 375, 85), (105, 175, 325, 520)]
            api.broadcastTypeMask = ['broadcastType-mask', (1440, 1035, 1530, 1065)]
    except:
        api.printError()

