
def test(api):
    try:
        api.doFTI = _doFTI
        api.doPowerCycle = _doPowerCycle
        api.setEPGFilter = _setEPGFilter
    except:
        api.printError()

def _doFTI(api, countryName='GERMANY'):
    try:
        api.sendKeys(['STARTFTI+5', 'left+1', 'ok+50', 'SETCOUNTRY '+countryName.upper()+'+2', 'ok+1*7'])
    except:
        api.printError()

def _doPowerCycle(api):
    try:
        api.sendKeys(['poweroff+15', 'poweron+45', 'RNS_0+15'])
        api.setTvIP(api.getTV_IP(api)[0])
    except:
        api.printError()

def _setEPGFilter(api, fromView='NowNext', networkType='Digital Aerial Only', tvRadio='All', freeCas='All', az='All', sort='Numeric', hdsd='All', favourites='None'):
    try:
        fromView = fromView.lower()
        if fromView == 'nownext' or fromView == 'timeline':
            api.sendKeys(['blue+2', 'gofirstitemgroup+1'])
        elif fromView == 'list':
            api.sendKeys(['text+2', 'gofirstitemgroup+1'])

        networkType = networkType.lower()
        if networkType == 'digital cable only':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        elif networkType == 'satellite only':
            api.sendKeys(['gofirstitem+1', 'left+1'])
        else:
            api.sendKeys(['gofirstitem+1'])

        api.sendKeys(['down+1'])
        tvRadio = tvRadio.lower()
        if tvRadio == 'tv only':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        elif tvRadio == 'radio only':
            api.sendKeys(['gofirstitem+1', 'right+1*2'])
        elif tvRadio == 'text only':
            api.sendKeys(['gofirstitem+1', 'left+1'])
        else:
            api.sendKeys(['gofirstitem+1'])
        api.sendKeys(['down+1'])
        freeCas = freeCas.lower()
        if freeCas == 'free':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        elif freeCas == 'encrypted':
            api.sendKeys(['gofirstitem+1', 'left+1'])
        else:
            api.sendKeys(['gofirstitem+1'])

        api.sendKeys(['down+1'])
        az = az.lower()
        if az == 'a':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        elif az == 'b':
            api.sendKeys(['gofirstitem+1', 'right+1*2'])
        elif az == 'z':
            api.sendKeys(['gofirstitem+1', 'left+1'])
        else:
            api.sendKeys(['gofirstitem+1'])

        api.sendKeys(['down+1'])
        sort = sort.lower()
        if sort == 'alphabetic':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        else:
            api.sendKeys(['gofirstitem+1'])

        api.sendKeys(['down+1'])
        hdsd = hdsd.lower()
        if hdsd == 'sd':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        elif hdsd == 'hd':
            api.sendKeys(['gofirstitem+1', 'left+1'])
        else:
            api.sendKeys(['gofirstitem+1'])
            api.sendKeys(['down+1'])
            favourites = favourites.lower()
        if favourites == 'favourites1':
            api.sendKeys(['gofirstitem+1', 'right+1'])
        elif favourites == 'favourites3':
            api.sendKeys(['gofirstitem+1', 'left+1*2'])
        api.testImages('currentEPGFilter-ref', mask=api.EPGFilterMask, limit=90, msg='EPG filtresinin dogru oldugu gorulmelidir.')
        api.sendKeys(['exit+1'])
    except:
        api.printError()

