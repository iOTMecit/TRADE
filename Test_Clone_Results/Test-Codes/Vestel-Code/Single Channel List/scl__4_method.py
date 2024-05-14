
def test(api):
    try:
        api.doFTI = _doFTI
        api.doPowerCycle = _doPowerCycle
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

