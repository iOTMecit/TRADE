
def test(api):
    try:
        api.doFTI = _doFTI
        api.doPowerCycle = _doPowerCycle
        api.doStandByCycle = _doStandByCycle
    except:
        api.printError()

def _doFTI(api, countryName='GERMANY'):
    try:
        api.sendKeys(['STARTFTI+5', '4725+1', 'left+1', 'ok+50', 'SETCOUNTRY '+countryName.upper()+'+2', 'ok+1', 'up+0.5*5', 'gofirstitem+2', 'ok*2+1', '1+0.5*8+5', 'ok+1*5'])
    except:
        api.printError()

def _doPowerCycle(api):
    try:
        api.sendKeys(['poweroff+15', 'poweron+45', 'RNS_0+15'])
        # api.setTvIP(api.getTV_IP(api)[0])
    except:
        api.printError()

def _doStandByCycle(api, offTime=40, onTime=40):
    try:
        api.sendKeys(['standby+'+str(offTime), 'RNS_0+'+str(onTime), 'exit2+2'])
        # api.setTvIP(api.getTV_IP(api)[0])
    except:
        api.printError()

