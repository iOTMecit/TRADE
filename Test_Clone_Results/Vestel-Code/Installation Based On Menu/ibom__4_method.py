from customTime import sleep

def test(api):
    try:
        api.doFTI = _doFTI
        api.setDiseqC = _setDiseqC
        api.doPowerCycle = _doPowerCycle
        api.audioCompare = _audioCompare
        api.stopPlayStream = _stopPlayStream
    except:
        api.printError()

def _doFTI(api, scanEncryptedChannels=1, aerial=0, cable=0, satellite=0, analogue=0, favNetType=-1, diseqc=None):
    try:
        api.sendKeys(['STARTFTI+5', 'left+1', 'ok+45', 'ok+2']) # FTI Country Selection
        if not scanEncryptedChannels:
            api.sendKeys(['down+0.5', 'GOFIRSTITEM+1', 'GOFIRSTITEMGROUP+2'])
        if not (aerial or cable or satellite or analogue):
            api.sendKeys(['ok+3*7+5'])
            if diseqc:
                api.sendKeys(api.ANTENNAINSTALLATION)
                api.setDiseqC(api, diseqc=diseqc)
        else:
            # Favourite Network Type Selection
            if favNetType == 'aerial':
                api.sendKeys(['down+0.5*2', 'GOFIRSTITEM+1', 'right+1', 'GOFIRSTITEMGROUP+2'])
            elif favNetType == 'cable':
                api.sendKeys(['down+0.5*2', 'GOFIRSTITEM+1', 'right+0.5*2', 'GOFIRSTITEMGROUP+2'])
            elif favNetType == 'satellite':
                api.sendKeys(['down+0.5*2', 'GOFIRSTITEM+1', 'left+0.5*2', 'GOFIRSTITEMGROUP+2'])
            elif favNetType == 'analogue':
                api.sendKeys(['down+0.5*2', 'GOFIRSTITEM+1', 'left+1', 'GOFIRSTITEMGROUP+2'])
            # DVB Type Selection
            if aerial and favNetType != 'aerial':
                api.sendKeys(['down+0.5*3', 'GOFIRSTITEM+1', 'right+1', 'GOFIRSTITEMGROUP+2'])
            if cable and favNetType != 'cable':
                api.sendKeys(['up+0.5*3', 'GOFIRSTITEM+1', 'right+1', 'GOFIRSTITEMGROUP+2'])
            if satellite and favNetType != 'satellite':
                api.sendKeys(['up+0.5*2', 'GOFIRSTITEM+1', 'right+1', 'GOFIRSTITEMGROUP+2'])
            if analogue and favNetType != 'analogue':
                api.sendKeys(['up+1', 'GOFIRSTITEM+1', 'right+1', 'GOFIRSTITEMGROUP+2'])
            # Network /Internet Settings
            api.sendKeys(['ok+1*3'])
            # Cable Network Search or Antenna Installation
            api.sendKeys(['ok+1'])
            if cable:
                api.sendKeys(['right+0.5', 'ok+1*2'])
            if satellite:
                api.setDiseqC(api, diseqc=diseqc)
    except:
        api.printError()

def _setDiseqC(api, diseqc=['', '', '', '']):
    try:
        api.sendKeys(['GOFIRSTITEM+1', 'left+1', 'ok+1'])
        if diseqc[3] == 'astra 1' and diseqc[1] != 'turksat':
            api.sendKeys(['left+1', 'up+1', 'right+1', 'down+1', 'right+1'])
        elif diseqc[3] != 'astra 1' and diseqc[1] == 'turksat':
            api.sendKeys(['down+1', 'left+1*2', 'up+1', 'left+1'])
        else:
            api.sendKeys(['right+1*13', 'down+1', 'left+1*2', 'down+1', 'right+1*19', 'down+1', 'right+1'])
        api.sendKeys(['ok'])
    except:
        api.printError()

def _doPowerCycle(api):
    try:
        api.sendKeys(['poweroff+15', 'poweron+45', 'RNS_0+15'])
        # api.setTvIP(api.getTV_IP(api)[0])
    except:
        api.printError()

def _audioCompare(api):
    for i in range(50):
        api.sendKeys(['exit+2'])
        if api.testImages(['scrambled-ref', 'blackScreen-ref'], expectMatch=False, mask=api.scrambledMask, recordResults=False, msg='Goruntude bir problem olmamali.')[0]:
            break
        api.sendKeys(['progup+10'])
    api.checkAudio(msg='Seste bir problem olmamali')

def _stopPlayStream(api, streamFile='', macro=[], delay=1):
    try:
        api.dta.sendCommands(commandL=['Stop; 0'], devnum=0)
        sleep(1)
        if not streamFile:
            return
        else:
            api.dta.sendCommands(commandL=['InputFile; '+api.streamPath+str(streamFile)], devnum=0)
            api.dta.sendCommands(commandL=macro, devnum=0)
        api.dta.sendCommands(commandL=['ignore_stop; 1'], devnum=0)
        api.dta.sendCommands(commandL=['Play; 1'], devnum=0)
        sleep(delay)
    except:
        api.printError()

