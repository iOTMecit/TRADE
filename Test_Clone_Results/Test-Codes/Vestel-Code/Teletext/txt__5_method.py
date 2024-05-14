from customTime import sleep

def test(api):
    try:
        api.doPowerCycle = _doPowerCycle
        api.plugInOutRFCable = _plugInOutRFCable
        api.stopPlayStream = _stopPlayStream
    except:
        api.printError()

def _doPowerCycle(api):
    try:
        api.sendKeys(['poweroff+15', 'poweron+45', 'RNS_0+15'])
        api.setTvIP(api.getTV_IP(api)[0])
    except:
        api.printError()

def _plugInOutRFCable(api, plugIn=True):
    try:
        if plugIn:
            api.dta.sendCommands(commandL=['Play; 1'], devnum=0)
            # api.sendKeys(['RFSIGNALON+5'])
        else:
            api.dta.sendCommands(commandL=['Stop; 0'], devnum=0)
            # api.sendKeys(['RFSIGNALOFF+5'])
    except:
        api.printError()

def _stopPlayStream(api, streamDevice='StreamPlayer', macro=[], delay=1):
    try:
        if streamDevice == 'StreamPlayer':
            api.dta107S.sendCommands(commandL=['Stop; 0'], devnum=0)
            api.dta107S.sendCommands(commandL=macro, devnum=0)
            api.dta107S.sendCommands(commandL=['Play; 1'], devnum=0)
        elif streamDevice == 'StreamPlayer2':
            api.dta.sendCommands(commandL=['Stop; 0'], devnum=0)
            api.dta.sendCommands(commandL=macro, devnum=0)
            api.dta.sendCommands(commandL=['Play; 1'], devnum=0)
        sleep(delay)
    except:
        api.printError()

