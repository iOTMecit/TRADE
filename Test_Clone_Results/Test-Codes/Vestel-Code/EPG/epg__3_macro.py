
def test(api):
    try:
        if api.UIName in ['amazon', 'toshiba18']:
            api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down+1*2', 'right+1*4', 'ok+2', 'down+1',  'gofirstitemgroup+1']

            api.MANUAL_CHANNEL_SCAN = api.INSTALL_MENU + ['down*1', 'ok+2', 'gofirstitemgroup+1', 'gofirstitem+1']
            api.IMPORT_CHANNEL_LIST = api.INSTALL_MENU + ['golastitemgroup', 'up+1*2', 'ok+40', 'clearosd+3']
            api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH25 = api.MANUAL_CHANNEL_SCAN + ['down+1', '25+10', 'ok+40']
            api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH26 = api.MANUAL_CHANNEL_SCAN + ['down+1', '26+10', 'ok+40']
            api.TIMERS = ['exit2+2*2', 'menu+2', 'down+1', 'right+1*3', 'ok+2']
        else:
            api.INSTALL_MENU = api.SETTINGS_MENU = []
            if api.UIName == 'carbon':
                api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down', 'ok+2', 'gofirstitemgroup+1']
                api.SETTINGS_MENU = ['exit2+2*2', 'menu+2', 'right+1', 'up+1', 'ok+1', 'gofirstitemgroup+1']
            if api.UIName == 'panasonic':
                api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down*3', 'ok+2', 'gofirstitemgroup+1']
                api.SETTINGS_MENU = ['exit2+2*2', 'menu+2', 'down*2', 'ok+2', 'gofirstitemgroup+1']
            elif api.UIName == 'titanium':
                api.INSTALL_MENU = ['exit2+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down', 'ok+2', 'gofirstitemgroup+1']
                api.SETTINGS_MENU = ['exit2+2*2', 'menu+2', 'ok+5', 'right+1*2', 'ok+2', 'gofirstitemgroup+1']

            api.MANUAL_CHANNEL_SCAN = api.INSTALL_MENU + ['down*1', 'ok+2', 'gofirstitemgroup+1', 'gofirstitem+1']
            api.IMPORT_CHANNEL_LIST = api.INSTALL_MENU + ['up+1*2', 'ok+20', 'clearosd+3']
            api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH25 = api.MANUAL_CHANNEL_SCAN + ['down+1', '25+10', 'ok+40']
            api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH26 = api.MANUAL_CHANNEL_SCAN + ['down+1', '26+10', 'ok+40']
            api.TIMERS = api.SETTINGS_MENU + ['down+1*3', 'ok+3']
    except:
        api.printError()

