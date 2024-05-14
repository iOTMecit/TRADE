
def test(api):
    try:
        api.defaultParentKey = '0000'
        api.defaultParentKey_France = '1111'

        api.INSTALL_MENU = api.SETTINGS_MENU = []
        if api.UIName == 'carbon':
            api.INSTALL_MENU = ['exit2+2*2', 'menu+2', 'down+1', 'ok+1', 'gofirstitemgroup+1']
            api.SETTINGS_MENU = ['exit2+2*2', 'menu+2', 'right+1', 'up+1', 'ok+1', 'gofirstitemgroup+1']
            api.PICTURE_MENU = ['exit2+2*2', 'menu+2', 'right+1', 'ok+1', 'gofirstitemgroup+1']
            api.SOUND_MENU = ['exit2+2*2', 'menu+2', 'right+1', 'down+1', 'ok+1', 'gofirstitemgroup+1']
        elif api.UIName == 'panasonic':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down*3', 'ok+2', 'gofirstitemgroup+1']
            api.SETTINGS_MENU = ['exit+2*2', 'menu+2', 'down*2', 'ok+2', 'gofirstitemgroup+1']
            api.PICTURE_MENU = ['exit+2*2', 'menu+2', 'ok+2', 'gofirstitemgroup+1']
            api.SOUND_MENU = ['exit+2*2', 'menu+2', 'down', 'ok+2', 'gofirstitemgroup+1']
        elif api.UIName == 'titanium':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down', 'ok+2', 'gofirstitemgroup+1']
            api.SETTINGS_MENU = ['exit+2*2', 'menu+2', 'ok+5', 'right+1*2', 'ok+2', 'gofirstitemgroup+1']
            api.PICTURE_MENU = ['exit+2*2', 'menu+2', 'ok+5*2', 'gofirstitemgroup+1']
            api.SOUND_MENU = ['exit+2*2', 'menu+2', 'ok+5', 'right+1', 'ok+2', 'gofirstitemgroup+1']

        api.MANUAL_CHANNEL_SCAN = api.INSTALL_MENU + ['down+0.5', 'ok+2', 'gofirstitemgroup+1', 'gofirstitem+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE = api.MANUAL_CHANNEL_SCAN + ['gofirstitem+1', 'right+1']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '746+2', 'down*2', '6875+10', 'ok*2+5']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_738FREG_6875SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '738+2', 'down*2', '6875+10', 'ok*2+5']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_730FREG_6875SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '730+2', 'down*2', '6875+10', 'ok*2+5']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '722+2', 'down*2', '6900+10', 'ok*2+5']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_706FREG_6875SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '706+2', 'down*2', '6875+10', 'ok*2+5']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '698+2', 'down*2', '6875+10', 'ok*2+5']
        api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_690FREG_6875SYMB = api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '690+2', 'down*2', '6875+10', 'ok*2+5']
        api.PARENTAL_MENU = api.SETTINGS_MENU + ['down*2', 'ok+1']
        api.MATURITY_LOCK_PSWRD_0000 = api.PARENTAL_MENU + ['0000+1', 'down+1', 'gofirstitem+1']
        api.MATURITY_LOCK_PSWRD_1111 = api.PARENTAL_MENU + ['1111+1', 'down+1', 'gofirstitem+1']
        api.PARENTALMENU_MATURITY_PSWRD0000_OFF = api.MATURITY_LOCK_PSWRD_0000 + ['exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AGE4 = api.MATURITY_LOCK_PSWRD_0000 + ['right+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AGE10 = api.MATURITY_LOCK_PSWRD_0000 + ['right+1*7', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AGE12 = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*7', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AGE16 = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*3', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AGE17 = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AGE18 = api.MATURITY_LOCK_PSWRD_0000 + ['left+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_C = api.MATURITY_LOCK_PSWRD_0000 + ['right+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_M = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*4', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_MA = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*3', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_AV = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_R = api.MATURITY_LOCK_PSWRD_0000 + ['left+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_P = api.MATURITY_LOCK_PSWRD_0000 + ['right+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_PG = api.MATURITY_LOCK_PSWRD_0000 + ['right+1*4', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_G = api.MATURITY_LOCK_PSWRD_0000 + ['right+1*3', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD1111_AGE10 = api.MATURITY_LOCK_PSWRD_1111 + ['exit+5']
        api.PARENTALMENU_MATURITY_PSWRD1111_AGE12 = api.MATURITY_LOCK_PSWRD_1111 + ['right+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD1111_AGE16 = api.MATURITY_LOCK_PSWRD_1111 + ['right+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD1111_AGE18 = api.MATURITY_LOCK_PSWRD_1111 + ['left+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD1111_PARENTALAPPROVAL = api.MATURITY_LOCK_PSWRD_1111 + ['left+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_AGE7 = api.MATURITY_LOCK_PSWRD_0000 + ['right+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_AGE13 = api.MATURITY_LOCK_PSWRD_0000 + ['right+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_AGE18 = api.MATURITY_LOCK_PSWRD_0000 + ['left+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_XRATED = api.MATURITY_LOCK_PSWRD_0000 + ['left+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SWEDEN_YOUTH = api.MATURITY_LOCK_PSWRD_0000 + ['right+1*2', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SWEDEN_ADULT = api.MATURITY_LOCK_PSWRD_0000 + ['left+1', 'exit+5']
        api.PARENTALMENU_MATURITY_PSWRD0000_SWEDEN_CHILDREN = api.MATURITY_LOCK_PSWRD_0000 + ['right+1', 'exit+5']
    except:
        api.printError()

