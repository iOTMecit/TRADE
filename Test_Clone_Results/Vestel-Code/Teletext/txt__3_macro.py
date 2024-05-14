
def test(api):
    try:
        api.usingChannelName = 'TRT 1'
        api.usingChannelName2 = 'CINE+'
        api.usingChannelName3 = 'TF1'

        api.FTI = ['STARTFTI+5', 'left+1', 'ok+45']
        api.CONFIRMFTI = ['ok+2*7+5']
        api.INSTALL_MENU = api.SETTINGS_MENU = []
        if api.UIName == 'carbon':
            api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', 'menu+2', 'down+1', 'ok+1', 'gofirstitemgroup+1']
            api.SETTINGS_MENU = ['exit2+2*2', 'clearosd+5', 'menu+2', 'right+1', 'up+1', 'ok+1', 'gofirstitemgroup+1']
        elif api.UIName == 'panasonic':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down*3', 'ok+2', 'gofirstitemgroup+1']
            api.SETTINGS_MENU = ['exit+2*2', 'menu+2', 'down*2', 'ok+2', 'gofirstitemgroup+1']
        elif api.UIName == 'titanium':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down', 'ok+2', 'gofirstitemgroup+1']
            api.SETTINGS_MENU = ['exit+2*2', 'menu+3', 'ok+3', 'right+2*2', 'ok+2', 'gofirstitemgroup+1']

        api.SET_ASTRA1 = api.INSTALL_MENU + ['down+1*4', 'ok+1', 'down+1', 'ok+1', 'left+1', 'ok+1', 'up+1', 'gofirstitem+2', 'down+1', 'gofirstitem+2', 'left+1', 'ok+6']
        api.MANUAL_CHANNEL_SCAN = api.INSTALL_MENU + ['down*1', 'ok+2', 'gofirstitemgroup+1', 'gofirstitem+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL = api.MANUAL_CHANNEL_SCAN
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE = api.MANUAL_CHANNEL_SCAN + ['gofirstitem+1', 'right+1']
        api.MANUAL_CHANNEL_SCAN_ANALOGUE = api.MANUAL_CHANNEL_SCAN + ['gofirstitem+1', 'left+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 = api.MANUAL_CHANNEL_SCAN + ['right*2+1', 'up+1', 'right+1', 'down+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH21 = api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL + ['down+1', '21+15', 'ok+60']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH49 = api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL + ['down', '49+15', 'ok']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_338FREG = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '338+15', 'down*2', '6900+2', 'ok+60']
        api.MANUAL_CH_SCAN_SAT_10750FREG = api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 + ['down', '10750+3', 'down+1', 'gofirstitem+1', 'left+1', 'down+1', '27500+10', 'ok+60']
        api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN12 = api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['down*3+1', '12+15', 'ok+40']
        api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN35 = api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['down*3+1', '35+15', 'ok+40']

        api.SETTINGS_LANGUAGE = api.SETTINGS_MENU + ['down+1', 'ok+1', 'gofirstitemgroup+1']
        api.LANGUAGESETTING_TXT = api.SETTINGS_LANGUAGE + ['down+1*5', 'gofirstitem+1', 'exit2+2*2', 'clearosd+5']
        api.LANGUAGESETTING_TXT_TURKGRE_DVBT = api.SETTINGS_LANGUAGE + ['down+1*5', 'gofirstitem+1', 'left+1*2', 'exit2+2*2', 'clearosd+5']
        api.LANGUAGESETTING_TXT_EAST_DVBT = api.SETTINGS_LANGUAGE + ['down+1*5', 'gofirstitem+1', 'right+1', 'exit2+2*2', 'clearosd+5']
        api.LANGUAGESETTING_TXT_CYRILLIC_DVBT = api.SETTINGS_LANGUAGE + ['down+1*5', 'gofirstitem+1', 'right+1*2', 'exit2+2*2', 'clearosd+5']
        api.LANGUAGESETTING_TXT_ARABIC_DVBT = api.SETTINGS_LANGUAGE + ['down+1*5', 'gofirstitem+1', 'left+1', 'exit2+2*2', 'clearosd+5']
    except:
        api.printError()

