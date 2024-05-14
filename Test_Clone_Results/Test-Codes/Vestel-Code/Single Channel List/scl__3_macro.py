
def test(api):
    try:
        api.firstChannelName = 'BBC ONE'
        api.deleteChannelName = 'TRT1 HD'
        api.moveChannelName = 'TRT SPOR'
        api.lockPassword = '0000'
        api.DVBT_CHN1 = api.firstChannelName
        api.DVBT_CHN2 = 'BBC TWO'
        api.DVBC_CHN1 = 'Das Erste HD'
        api.DVBC_CHN2 = 'ZDF HD'

        if api.UIName == 'carbon':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down+1', 'ok+2', 'gofirstitemgroup+1']
            api.ADD_CHEDIT_MOVE = ['ok+1', 'down+1', 'ok+1']
        elif api.UIName == 'panasonic':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down*3', 'ok+2', 'gofirstitemgroup+1']
            api.ADD_CHEDIT_MOVE = ['ok+1', 'down+1', 'ok+1']
        elif api.UIName == 'titanium':
            api.INSTALL_MENU = ['exit+2*2', 'clearosd+5', '4725+5', 'menu+2', 'down+1', 'ok+2', 'gofirstitemgroup+1']
            api.ADD_CHEDIT_MOVE = ['ok+1', 'green+1', 'ok+1', 'down+1', 'ok+1']

        api.IMPORT_CHANNEL_LIST = api.INSTALL_MENU + ['up*3', 'ok+50', 'clearosd+10']
        api.IMPORT_CHANNEL_LIST_FTI = api.INSTALL_MENU + ['up*2', 'ok+50', 'clearosd+10']
        api.GOFIRSTCHANNELOFLIST = ['1+3']
        api.ADVANCECHLIST_MENU = ['clearosd+3', 'menu+2', 'down+1*2', 'ok+1']
        api.CHANNEL_LIST_FILTER_ALL = ['exit+2*2', '1+5', 'ok+1', 'blue', 'gofirstitem+1']
        api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY = ['exit+2*2', '1+5', 'ok+1', 'blue', 'gofirstitem+1', 'right+1']
        api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY = ['exit+2*2', '1+5', 'ok+1', 'blue', 'gofirstitem+1', 'right*2+1']
        api.CHANNEL_LIST_FILTER_SATELLITE_ONLY = ['exit+2*2', '1+5', 'ok+1', 'blue', 'gofirstitem+1', 'right*3+1']
        api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY = ['exit+2*2', '1+5', 'ok+1', 'blue', 'gofirstitem+1', 'right*4+1']
        api.ADVANCECHLIST = ['exit+2', 'ok+2', 'green+2']
        api.LIGHTCHLIST = ['exit+2', 'ok+2']
        api.FILTER_CHLIST_RADIOONLY = api.LIGHTCHLIST + ['blue+1', 'down+1', 'gofirstitem+1', 'right+1*2']
        api.FILTER_CHLIST_TVONLY = api.LIGHTCHLIST + ['blue+1', 'down+1', 'gofirstitem+1', 'right+1']
        api.FILTER_CHLIST_TVRADIOALL = api.LIGHTCHLIST + ['blue+1', 'down+1', 'gofirstitem+1']
        api.FILTER_CHLIST_FREE = api.LIGHTCHLIST + ['blue+1', 'down+1*2', 'gofirstitem+1', 'right+1']
        api.FILTER_CHLIST_ENCRYPTED = api.LIGHTCHLIST + ['blue+1', 'down+1*2', 'gofirstitem+1', 'right*2+1']
        api.FILTER_CHLIST_FREECAS_ALL = api.LIGHTCHLIST + ['blue+1', 'down+1*2', 'gofirstitem+1']
        api.FILTER_CHLIST_A_Z_A = api.LIGHTCHLIST + ['blue+1', 'down+1*3', 'gofirstitem+1', 'right+4']
        api.FILTER_CHLIST_A_Z_ALL = api.LIGHTCHLIST + ['blue+1', 'down+1*3', 'gofirstitem+1']
        api.FILTER_CHLIST_SORT_ALPH = api.LIGHTCHLIST + ['blue+1', 'down+1*4', 'gofirstitem+1', 'right+1']
        api.FILTER_CHLIST_SORT_NUM = api.LIGHTCHLIST + ['blue+1', 'down+1*4', 'gofirstitem+1']
        api.FILTER_CHLIST_HDSD_ALL = api.LIGHTCHLIST + ['blue+1', 'down+1*5', 'gofirstitem+1']
        api.FILTER_CHLIST_HDSD_HD = api.LIGHTCHLIST + ['blue+1', 'down+1*5', 'gofirstitem+1', 'right+1*2']
        api.FILTER_CHLIST_HDSD_SD = api.LIGHTCHLIST + ['blue+1', 'down+1*5', 'gofirstitem+1', 'right+1']
        api.FILTER_CHLIST_FAVOURITE_1 = api.LIGHTCHLIST + ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1']
        api.FILTER_CHLIST_FAVOURITE_2 = api.LIGHTCHLIST + ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1*2']
        api.FILTER_CHLIST_FAVOURITE_3 = api.LIGHTCHLIST + ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1*3']
        api.FILTER_CHLIST_FAVOURITE_4 = api.LIGHTCHLIST + ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1*4']
        api.FILTER_CHLIST_FAVOURITE_NONE = api.LIGHTCHLIST + ['blue+1', 'down+1*6', 'gofirstitem+1']
        api.ADD_SATLIST_ASTRA = ['down*7', 'gofirstitem+1', 'left+1']
        api.ADD_SATLIST_TURKSAT = ['up+1', 'gofirstitem+1', 'right+2*2']
        api.ADD_SATLIST_HOTBIRD = ['down*7', 'gofirstitem+1', 'right+1*3']
        api.ADD_SATLIST_EUTELSAT = ['down*7', 'gofirstitem+1', 'right+1']
        api.ADD_SATLIST_ALL = ['down*7', 'gofirstitem+1']
        api.ADD_CHEDIT_DEL = ['ok+1', 'down*2', 'ok+1']
        api.ADD_CHEDIT_MOVE_MULTI = ['ok+1', 'ok+1']
        api.ADD_CHEDIT_EDIT = ['ok+1', 'down+1*3', 'ok+1']
        api.ADD_CHEDIT_LOCKUNLOCK = ['ok+1', 'down+1*4', 'ok+1']
        api.EDIT_FAVOURITE = ['quick_menu+1', 'down*5', 'ok']  #3D Support
        api.ADV_CHLIST_FILTER_SATELLITE_ONLY = ['blue+1', 'gofirstitem+1', 'right+1*3']
        api.ADV_CHLIST_FILTER_DIGITAL_AERIAL_ONLY = ['blue', 'gofirstitem+1', 'right+1']
        api.ADV_CHLIST_FILTER_DIGITAL_CABLE_ONLY = ['blue', 'gofirstitem+1', 'right+1*2']
        api.ADV_CHLIST_FILTER_ANALOGUE_TV_ONLY = ['blue', 'gofirstitem+1', 'right*4+1']
        api.ADV_CHLIST_FILTER_ALL = ['blue', 'gofirstitem+1']
        api.ADV_CHLIST_FILTER_RADIOONLY = ['blue+1', 'down+1', 'gofirstitem+1', 'right+1*2']
        api.ADV_CHLIST_FILTER_TVONLY = ['blue+1', 'down+1', 'gofirstitem+1', 'right+1']
        api.ADV_CHLIST_FILTER_TVRADIOALL = ['blue+1', 'down+1', 'gofirstitem+1']
        api.ADV_CHLIST_FILTER_FREE = ['blue+1', 'down+1*2', 'gofirstitem+1', 'right+1']
        api.ADV_CHLIST_FILTER_ENCRYPTED = ['blue+1', 'down+1*2', 'gofirstitem+1', 'right*2+1']
        api.ADV_CHLIST_FILTER_FREECAS_ALL = ['blue+1', 'down+1*2', 'gofirstitem+1']
        api.ADV_CHLIST_FILTER_A_Z_A = ['blue+1', 'down+1*3', 'gofirstitem+1', 'right+1']
        api.ADV_CHLIST_FILTER_A_Z_T = ['blue+1', 'down+1*3', 'gofirstitem+1', 'left+2*7']
        api.ADV_CHLIST_FILTER_A_Z_ALL = ['blue+1', 'down+1*3', 'gofirstitem+1']
        api.ADV_CHLIST_FILTER_SORT_ALPH = ['blue+1', 'down+1*4', 'gofirstitem+1', 'right+1']
        api.ADV_CHLIST_FILTER_SORT_NUM = ['blue+1', 'down+1*4', 'gofirstitem+1']
        api.ADV_CHLIST_FILTER_HDSD_HD = ['blue+1', 'down+1*5', 'gofirstitem+1', 'right+1*2']
        api.ADV_CHLIST_FILTER_HDSD_SD = ['blue+1', 'down+1*5', 'gofirstitem+1', 'right+1']
        api.ADV_CHLIST_FILTER_HDSD_ALL = ['blue+1', 'down+1*5', 'gofirstitem+1']
        api.ADV_CHLIST_LOCKUNLOCKALLCHANNEL = ['ok+2', 'up+2*2', 'ok+3']
        api.ADD_FAV1_SELECTEDCHANNELS = ['ok+1', 'up+1', 'ok+1', 'gofirstitem+1', 'right+1', 'ok+3' ]
        api.QUICKMENU_SELECT_FAVLIST = ['exit+1*2', 'quick_menu+1', 'gofirstitemgroup+1', 'down+1*4', 'gofirstitem+1']  #3D Support
        api.FILTER_FAVOURITE_1 = ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1']
        api.FILTER_FAVOURITE_2 = ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1*2']
        api.FILTER_FAVOURITE_3 = ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1*3']
        api.FILTER_FAVOURITE_4 = ['blue+1', 'down+1*6', 'gofirstitem+1', 'right+1*4']
        api.FILTER_FAVOURITE_NONE = ['blue+1', 'down+1*6', 'gofirstitem+1']
        api.CLEAR_FILTER = ['blue+1', 'red+6', 'back+1']
    except:
        api.printError()

