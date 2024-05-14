
def test(api):
    try:
        api.streamPath = 'D:/STREAMS/Installation Based On Menu/'
        api.DTV_DVB_C_346MHZ = ['ModulationType; DVBC', 'Frequency; 346', 'BitRate; 38014706', 'Constellation; QAM256', 'remultiplex; 1', 'Play; 1']

        tkgs = tddf = 0
        if api.TKGS:
            tkgs = 1
        if api.TKGS or api.DSmart or api.Digiturk or api.Fransat:
            tddf = 1

        api.INSTALL_MENU = api.OTHER_SETTINGS = []
        if api.UIName == 'carbon':
            api.INSTALL_MENU = ['clearosd+10', 'exit2+5*2', '4725+5', 'menu+2', 'down', 'ok+2', 'gofirstitemgroup+1']
            api.OTHER_SETTINGS = ['exit2+2*2', 'menu+2', 'right+2', 'down*2', 'ok+1', 'up', 'ok+1']
        elif api.UIName == 'panasonic':
            api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down*3', 'ok+2', 'gofirstitemgroup+1']
            api.OTHER_SETTINGS = ['exit2+2*2', 'menu+2', 'down*2', 'ok+1', 'up', 'ok+1']
        elif api.UIName == 'titanium':
            api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down+1', 'ok+2', 'gofirstitemgroup+1']
            api.OTHER_SETTINGS = ['exit2+2*2', 'menu+3', 'right*3', 'ok+1', 'up', 'ok+1']

        api.AUTOMATIC_CHANNEL_SCAN = api.INSTALL_MENU + ['down*'+str(tkgs), 'ok+2', 'gofirstitemgroup+1']
        api.MANUAL_CHANNEL_SCAN = api.INSTALL_MENU + ['down*'+str(1+tkgs), 'ok+2', 'gofirstitemgroup+1', 'gofirstitem+1']
        api.NETWORK_CHANNEL_SCAN = api.INSTALL_MENU + ['down*'+str(2+tkgs), 'ok+2', 'gofirstitemgroup+1']
        api.ANALOGUE_FINE_TUNE = api.INSTALL_MENU + ['down*'+str(3+tkgs), 'ok+2']
        api.SATELLITE_SETTINGS = api.INSTALL_MENU + ['down*'+str(4+tkgs), 'ok+1']

        api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL = api.AUTOMATIC_CHANNEL_SCAN + ['ok', 'left', 'ok', 'ok']
        api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE = api.AUTOMATIC_CHANNEL_SCAN + ['down', 'ok', 'left', 'ok', 'ok']
        api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE = api.AUTOMATIC_CHANNEL_SCAN + ['down*2', 'ok', 'left', 'ok', 'ok']
        api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_FULL = api.AUTOMATIC_CHANNEL_SCAN + ['up', 'ok+1*'+str(1+tddf), 'green']
        api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 = api.AUTOMATIC_CHANNEL_SCAN + ['up', 'ok+1*'+str(1+tddf), 'down', 'yellow']
        api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4 = api.AUTOMATIC_CHANNEL_SCAN + ['up', 'ok+1*'+str(1+tddf), 'down*3', 'yellow']
        api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4_withChannel = api.AUTOMATIC_CHANNEL_SCAN + ['up', 'ok+1', 'left', 'ok+1*'+str(1+tddf), 'down*3', 'yellow']

        api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL = api.MANUAL_CHANNEL_SCAN
        api.MANUAL_CHANNEL_SCAN_ANALOGUE = api.MANUAL_CHANNEL_SCAN + ['left+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE = api.MANUAL_CHANNEL_SCAN + ['right+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_1 = api.MANUAL_CHANNEL_SCAN + ['right*2+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 = api.MANUAL_CHANNEL_SCAN + ['right*2+1', 'up', 'right', 'down+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_3 = api.MANUAL_CHANNEL_SCAN + ['right*2+1', 'up', 'right*2', 'down+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4 = api.MANUAL_CHANNEL_SCAN + ['right*2+1', 'up', 'right*3', 'down+1']

        api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*2+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_SATELLITE_ONLY = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*3+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*4+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_1 = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*3+1', 'up+1', 'gofirstitem+1', 'right+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_2 = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*3+1', 'up+1', 'gofirstitem+1', 'right*2+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_3 = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*3+1', 'up+1', 'gofirstitem+1', 'right*3+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_4 = ['exit2+3*2', '1+5', 'ok', 'green+1', 'blue+1', 'red+1', 'right*3+1', 'up+1', 'gofirstitem+1', 'right*4+1', 'ok+2', 'exit2+3*2']
        api.CHANNEL_LIST_SCRAMBLED = ['exit2+3*2', '1+5', 'ok', 'green', 'blue+1', 'red+1', 'down*2', 'gofirstitem+1', 'left',  'ok+2', 'exit2+3*2']

        api.SATCODX = api.SATELLITE_SETTINGS + ['up', 'ok+2']
        api.OTHER_SETTINGS_BISS_KEY = api.OTHER_SETTINGS + ['down*5', 'ok+1']
        api.ANTENNAINSTALLATION = api.SATELLITE_SETTINGS + ['down+1', 'ok+2']
    except:
        api.printError()

