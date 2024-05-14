# Mustafa DEMIRKAPI
# Installation BasedOn Menu Test Suite v1.0
# TV

# import VestaAPI
from customTime import sleep

''' Bu ayarlari degistirmeyiniz '''
previousCaseNumber = 0

def test(api):
    try:
        # ''' Case 1 - Automatic Channel Scan '''
        Case101(api)
        Case102(api)
        Case103(api)
        Case104(api)
        Case105(api)
        Case106(api)
        Case107(api)
        Case108(api)
        Case109(api)
        Case110(api)
        Case111(api)
        Case112(api)
        Case113(api)
        Case114(api)
        Case115(api)
        Case116(api)
        Case117(api)
        Case118(api)
        Case119(api)
        Case120(api)
        Case121(api)
        Case122(api)
        Case123(api)
        Case124(api)
        Case125(api)
        # ''' Case 2 - Manual Channel Scan '''
        Case201(api)
        Case202(api)
        Case203(api)
        Case204(api)
        Case205(api)
        Case206(api)
        Case207(api)
        Case208(api)
        Case209(api)
        Case210(api)
        Case211(api)
        Case212(api)
        # ''' Case 3 - Network Channel Scan '''
        Case301(api)
        Case302(api)
        Case303(api)
        # ''' Case 4 - Satellite Settings '''
        Case401(api)
        Case402(api)
        Case403(api)
        Case404(api)
        Case405(api)
        Case406(api)
        Case407(api)
        Case408(api)
        Case409(api)
        Case410(api)
        # ''' Case 5 - First Time Installation '''
        Case501(api)
        Case502(api)
        Case503(api)
        Case504(api)
        Case505(api)
        Case506(api)
        Case507(api)
        Case508(api)
        Case509(api)
        Case510(api)
        Case511(api)
        Case512(api)
    except:
        api.printError()

def Case101(api):
    # ''' 1. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 2. Installation menu altindan Automatic channel scan menusunu aciniz ve Vestel sistem yayinini kullanarak Digital Cable search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-C kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_01')
    api.setTestCaseDescription('DVB-C Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                api.channelSearchCompleteControl(timeout=300)
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 2

def Case102(api):
    # ''' 3. Kanal listesinde Digital Cable kanallar var iken Auto channel scan menusunden Vestel sistem yayinini kullanarak Digital Aerial Search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-T kanallari yakalamalidir. DVB-C ve DVB-T kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_02')
    api.setTestCaseDescription('DVB-C + DVB-T Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 1:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
    previousCaseNumber = 2
    api.end(False)

def Case103(api):
    # ''' 4. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 5. Installation menu altindan Automatic channel scan menusunu aciniz ve Vestel sistem yayinini kullanarak Digital Cable search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-C kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_03')
    api.setTestCaseDescription('DVB-C Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 3

def Case104(api):
    # ''' 6. Kanal listesinde Digital Cable kanallar var iken Auto channel scan menusunden Diseqc 4 Astra 1 uydusunda Digital Satellite search yapiniz. '''
    # ''' Beklenen Sonuc: Astra1 uydusundan gelen tum DVB-S kanallari yakalamalidir. DVB-C ve DVB-S kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_04')
    api.setTestCaseDescription('DVB-C + DVB-S Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 3:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.ANTENNAINSTALLATION)
                    setDiseqC(api, diseqc=['', '', '', 'astra 1'])
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4_withChannel)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 4

def Case105(api):
    # ''' 7. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 8. Installation menu altindan Automatic channel scan menusunu aciniz ve Vestel sistem yayinini kullanarak Digital Cable search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-C kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_05')
    api.setTestCaseDescription('DVB-C Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 5

def Case106(api):
    # ''' 9. Kanal listesinde Digital Cable kanallar var iken Auto channel scan menusunden Analogue Search yapiniz. '''
    # ''' Beklenen Sonuc: Tum analogue kanallari yakalamalidir. DVB-C ve Analogue kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_06')
    api.setTestCaseDescription('DVB-C + Analogue Automatic Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 5:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 6

def Case107(api):
    # ''' 10. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' Beklenen Sonuc: Kanal bulunmadigina dair uyari vermelidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_07')
    api.setTestCaseDescription('No Channel Messsage')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 7

def Case108(api):
    # ''' 12. Installation menu altindan Automatic channel scan menusunu aciniz ve Diseqc 4 Astra 1 uydusunda Digital Satellite search yapiniz. '''
    # ''' Beklenen Sonuc: Astra1 uydusuna ait tum kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_08')
    api.setTestCaseDescription('DVB-S (Astra 1) Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 7:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 8

def Case109(api):
    # ''' 13. Kanal listesinde Digital Satellite kanallar var iken Auto channel scan menusunden Vestel sistem yayinini kullanarak Digital Cable Search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-C kanallari yakalamalidir. DVB-S ve DVB-C kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_09')
    api.setTestCaseDescription('DVB-S (Astra 1) + DVB-C Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 8:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 9

def Case110(api):
    # ''' 14. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 15. Installation menu altindan Automatic channel scan menusunu aciniz ve Diseqc 4 Astra 1 uydusunda Digital Satellite search yapiniz. '''
    # ''' Beklenen Sonuc: Astra1 uydusuna ait tum kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_10')
    api.setTestCaseDescription('DVB-S (Astra 1) Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 10

def Case111(api):
    # ''' 16. Kanal listesinde Digital Satellite kanallar var iken Auto channel scan menusunden Vestel sistem yayinini kullanarak Digital Aerial Search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-T kanallari yakalamalidir. DVB-S ve DVB-T kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_11')
    api.setTestCaseDescription('DVB-S (Astra 1) + DVB-T Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBS:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 10:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 11

def Case112(api):
    # ''' 17. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 18. Installation menu altindan Automatic channel scan menusunu aciniz ve Diseqc 4 Astra 1 uydusunda Digital Satellite search yapiniz. '''
    # ''' Beklenen Sonuc: Astra1 uydusuna ait tum kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_12')
    api.setTestCaseDescription('DVB-S (Astra 1) Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 12

def Case113(api):
    # ''' 19. Kanal listesinde Digital Satellite kanallar var iken Auto channel scan menusunden Analogue Search yapiniz. '''
    # ''' Beklenen Sonuc: Tum analogue kanallari yakalamalidir. DVB-S ve Analogue kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_13')
    api.setTestCaseDescription('DVB-S (Astra 1) + Analogue Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBS or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 12:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 13

def Case114(api):
    # ''' 20. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 21. Installation menu altindan Automatic channel scan menusunu aciniz ve Analogue search yapiniz. '''
    # ''' Beklenen Sonuc: Tum analogue kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_14')
    api.setTestCaseDescription('Analogue Automatic Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 14

def Case115(api):
    # ''' 22. Kanal listesinde Analogue kanallar var iken Auto channel scan menusunden Vestel sistem yayinini kullanarak Digital Cable Search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-C kanallari yakalamalidir. Analogue ve DVB-C kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_15')
    api.setTestCaseDescription('Analogue + DVB-C Automatic Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 14:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 15

def Case116(api):
    # ''' 23. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 24. Installation menu altindan Automatic channel scan menusunu aciniz ve Analogue search yapiniz. '''
    # ''' Beklenen Sonuc: Tum analogue kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_16')
    api.setTestCaseDescription('Analogue Automatic Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 16

def Case117(api):
    # ''' 25. Kanal listesinde Analogue kanallar var iken Auto channel scan menusunden Diseqc 4 Astra 1 uydusunda Digital Satellite search yapiniz. '''
    # ''' Beklenen Sonuc: Astra1 uydusundan gelen tum DVB-S kanallari yakalamalidir. Analogue ve DVB-S kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_17')
    api.setTestCaseDescription('Analogue + DVB-S Automatic Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG or not api.DVBS:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 16:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4_withChannel)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 17

def Case118(api):
    # ''' 26. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 27. Installation menu altindan Automatic channel scan menusunu aciniz ve Analogue search yapiniz. '''
    # ''' Beklenen Sonuc: Tum analogue kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_18')
    api.setTestCaseDescription('Analogue Automatic Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 18

def Case119(api):
    # ''' 28. Kanal listesinde Analogue kanallar var iken Auto channel scan menusunden Vestel sistem yayinini kullanarak Digital Aerial Search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-T kanallari yakalamalidir. Analogue ve DVB-T kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_19')
    api.setTestCaseDescription('Analogue + DVB-T Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 18:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 19

def Case120(api):
    # ''' 29. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 30. Installation menu altindan Automatic channel scan menusunu aciniz ve Vestel sistem yayinini kullanarak Digital Aerial search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-T kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_20')
    api.setTestCaseDescription('DVB-T Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 20

def Case121(api):
    # ''' 31. Kanal listesinde Digital Aerial kanallar var iken Auto channel scan menusunden Diseqc 4 Astra 1 uydusunda Digital Satellite search yapiniz. '''
    # ''' Beklenen Sonuc: Astra1 uydusundan gelen tum DVB-S kanallari yakalamalidir. DVB-T ve DVB-S kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_21')
    api.setTestCaseDescription('DVB-T + DVB-S Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBS:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 20:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.ANTENNAINSTALLATION)
                    api.setDiseqC(api, diseqc=diseqc)
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4_withChannel)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 21

def Case122(api):
    # ''' 32. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 33. Installation menu altindan Automatic channel scan menusunu aciniz ve Vestel sistem yayinini kullanarak Digital Aerial search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-T kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_22')
    api.setTestCaseDescription('DVB-T Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 22

def Case123(api):
    # ''' 34. Kanal listesinde Digital Aerial kanallar var iken Auto channel scan menusunden Analogue Search yapiniz. '''
    # ''' Beklenen Sonuc: Tum analogue kanallari yakalamalidir. DVB-T ve Analogue kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_23')
    api.setTestCaseDescription('DVB-T + Analogue Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 22:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_ANALOGUE)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 23

def Case124(api):
    # ''' 35. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, Diseqc4"e Astra1 atayiniz, (diger diseqc"ler none olarak biraklimalidir) kanal bulmadan FTI"dan cikiniz. '''
    # ''' 36. Installation menu altindan Automatic channel scan menusunu aciniz ve Vestel sistem yayinini kullanarak Digital Aerial search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-T kanallari yakalamalidir. Ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_24')
    api.setTestCaseDescription('DVB-T Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 24

def Case125(api):
    # ''' 37. Kanal listesinde Digital Aerial kanallar var iken Auto channel scan menusunden Vestel sistem yayinini kullanarak Digital Cable Search yapiniz. '''
    # ''' Beklenen Sonuc: Vestel sistem yayinindan gelen tum DVB-C kanallari yakalamalidir. DVB-T ve DVB-C kanallarda ses ve goruntude bir problem olmamalidir. '''
    global previousCaseNumber
    api.setTestCaseName('Installation_BasedOn_Menu_01_25')
    api.setTestCaseDescription('DVB-T + DVB-C Automatic Channel Scan')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                if previousCaseNumber != 24:
                    api.doFTI(api, diseqc=['', '', '', 'astra 1'])
                    sleep(10)
                    api.testImages('noChannel-ref')
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_AERIAL)
                    api.channelSearchCompleteControl()
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_CABLE)
                    api.channelSearchCompleteControl()
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+5'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)
    previousCaseNumber = 25

def Case201(api):
    # ''' 1. FTI yapiniz, Ulkeyi Germany seciniz, FTI"da broadcast type DVB-S seciniz ve anten tipini Diseqc secerek, asagidaki uydulari set ediniz. kanal bulmadan FTI"dan cikiniz. Stimulation: DiSEqC1: Eutelsat 7A, DiSEqC2: Turksat 4A, DiSEqC3: Hotbird, DiSEqC4: Astra 1 '''
    # ''' 2. Installation menu altindan Manual channel scan menusunu aciniz ve asagidaki parametreleri girerek search yapiniz. Stimulation: Search Type: Digital Aerial, Channel: CH45, Frequency: 666.000 MHz, Network channel scan: Disabled '''
    # ''' Beklenen Sonuc: Muxtaki DVB-T kanallara tune olmalidir, bulunan kanallarda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_01')
    api.setTestCaseDescription('DVB-T Manual Channel Scan')
    if not api.start():
        try:
            if not api.DVBT:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL + ['down', '45', 'down+2', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case202(api):
    # ''' 4. Manual Search menusunden Turksat uydusunu seciniz ve network channal scan enabled yaparak belirtilen parametreler ile satellite network fast scan yapiniz. (Turksat 4A, 12423+H+30000, 12380+V+27500) '''
    # ''' Beklenen Sonuc: Network search sorunsuz tamamlanmali, search sonunda kanallar bulunabilmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_02')
    api.setTestCaseDescription('DVB-S (Turksat) Satellite Network Fast Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 + ['down', '12380', 'down', 'GOFIRSTITEM', 'down', '27500', 'down', 'right', 'ok'])
                api.channelSearchCompleteControl()
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC2-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case203(api):
    # ''' 5. Installation menu altindan Manual channel scan menusunu aciniz ve parametreleri girerek search yapiniz.(LH-Eutelsat 7A 10721 H 22000) '''
    # ''' Beklenen Sonuc: BBC Persian kanali bulunmalidir, kanalda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_03')
    api.setTestCaseDescription('DVB-S (LH-Eutelsat) Manual Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_1 + ['down', '10721', 'down', 'right', 'down', '22000', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case204(api):
    # ''' 6. Installation menu altindan Manual channel scan menusunu aciniz ve parametreleri girerek search yapiniz.(HH-Turksat 12329 H 6666) '''
    # ''' Beklenen Sonuc: Fox HD kanali bulunmalidir, kanalda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_04')
    api.setTestCaseDescription('DVB-S (HH-Turksat) Manual Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 + ['down', '12329', 'down', 'right', 'down', '06666', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case205(api):
    # ''' 7. Installation menu altindan Manual channel scan menusunu aciniz ve parametreleri girerek search yapiniz.(LV-Astra1 / 11347+V+22000) '''
    # ''' Beklenen Sonuc: Kika HD kanali bulunmalidir, kanalda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_05')
    api.setTestCaseDescription('DVB-S (LV-Astra 1) Manual Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4 + ['down', '11347', 'down*2', '22000', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', '2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case206(api):
    # ''' 8. Installation menu altindan Manual channel scan menusunu aciniz ve parametreleri girerek search yapiniz.(HV-Hotbird 12597 V 27500) 12558 V 27500 '''
    # ''' Beklenen Sonuc: BBC World News kanali bulunmalidir, kanalda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_06')
    api.setTestCaseDescription('DVB-S (HV-Hotbird) Manual Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_3 + ['down', '12558', 'down*2', '27500', 'down+5', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', '8+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case207(api):
    # ''' 9. Astra 19, 2 11494+H+22000 parametreleri ile manual search yapiniz. '''
    # ''' Beklenen Sonuc: Das Erste HD (DVB-S2) kanali bulunmalidir, kanalda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_07')
    api.setTestCaseDescription('DVB-S2 (Astra 1) Manual Channel Scan')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_4 + ['down', '11494', 'down', 'right', 'down', '22000', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', '2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case208(api):
    # ''' 10. Installation menu altindan Manual channel scan menusunu aciniz ve asagidaki parametreleri girerek search yapiniz. Stimulation: Search Type: Analogue, Band: C, TV System: BG, Channel: C12, Frequency: 224.25 MHz '''
    # ''' Beklenen Sonuc: Analog C12 kanalina tune olmalidir, bulunan kanalda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_08')
    api.setTestCaseDescription('Analogue (C12 224.25MHz) Manual Channel Scan')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['down*3', '12', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', limit=70)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case209(api):
    # ''' 11. Installation menu altindaki Analogue Fine Tune menusune giriniz, Fine Tune degerini 4 arttirip(0"dan 4"e getirip), manual search menusune giriniz ve mevcut frekans degerini kontrol ediniz. '''
    # ''' Beklenen Sonuc: Kanalin merkez frekansi Fine Tune edilen degere gore artmis olmali, degismelidir. Kanal info barda Fine tune ikonu cikmali. Merkez frekans tan kaydirildikca videoda bozulma gozlenmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_09')
    api.setTestCaseDescription('Analogue (C12 224.25MHz) Fine Tune +4')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['down*3', '12', 'down', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['up+2'])
                api.grabImage('PIC4')
                api.sendKeys(['exit2+7', '1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', limit=70)
                api.audioCompare(api)
                api.sendKeys(api.ANALOGUE_FINE_TUNE + ['right*5+1', 'ok+2', 'exit2+7', 'info+1'])
                api.testImages('PIC3-ref', mask=api.analogFineTuneIconMask)
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['up+2'])
                api.testImages('PIC4', mask=api.analogFrequancyMask, expectMatch=False)
        except:
            api.printError()
        api.end(False)

def Case210(api):
    # ''' 12. Installation menu altindaki Analogue Fine Tune menusune giriniz, Fine Tune degerini 9 azaltip(4"ten -5"e getirip), manual search menusune giriniz ve mevcut frekans degerini kontrol ediniz. '''
    # ''' Beklenen Sonuc: Kanalin merkez frekansi Fine Tune edilen degere gore azalmis olmali, degismelidir. Kanal info barda Fine tune ikonu cikmali. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_10')
    api.setTestCaseDescription('Analogue (C12 224.25MHz) Fine Tune -5')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['down*3', '12', 'down', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['up+2'])
                api.grabImage('PIC4')
                api.sendKeys(['exit2+7', '1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', limit=70)
                api.audioCompare(api)
                api.sendKeys(api.ANALOGUE_FINE_TUNE + ['left*5+1', 'ok+2', 'exit2+7', 'info+1'])
                api.testImages('PIC3-ref', mask=api.analogFineTuneIconMask)
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['up+2'])
                api.testImages('PIC4', mask=api.analogFrequancyMask, expectMatch=False)
        except:
            api.printError()
        api.end(False)

def Case211(api):
    # ''' 13. Installation menu altindaki Analogue Fine Tune menusune giriniz, Fine Tune degerini 5 arttirip(-5"ten 0"a getirip), manual search menusune giriniz ve mevcut frekans degerini kontrol ediniz. '''
    # ''' Beklenen Sonuc: Frekans bilgisi kanalin merkez frekansine geri donmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_11')
    api.setTestCaseDescription('Analogue (C12 224.25MHz) Fine Tune 0')
    if not api.start():
        try:
            if not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['down*3', '12', 'down', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['up+2'])
                api.grabImage('PIC4')
                api.sendKeys(['exit2+7', '1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', limit=70)
                api.audioCompare(api)
                api.sendKeys(api.ANALOGUE_FINE_TUNE + ['right*5+1', 'ok+2', 'exit2+7', 'info+1'])
                api.testImages('PIC3-ref', mask=api.analogFineTuneIconMask)
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE + ['up+2'])
                api.testImages('PIC4', mask=api.analogFrequancyMask)
        except:
            api.printError()
        api.end(False)

def Case212(api):
    # ''' 14. Installation menu altindan Manual channel scan menusunu aciniz ve asagidaki parametreleri girerek search yapiniz. Stimulation: Search Type: Digital Cable, Frequency: 338.00 Mhz, Modulation: Auto, Symbol Rate: 6900, Network channel scan: Disabled '''
    # ''' Beklenen Sonuc: Muxtaki DVB-C kanallara tune olmalidir, bulunan kanallarda ses ve goruntude bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_02_12')
    api.setTestCaseDescription('DVB-C (338.00 MHz) Manual Channel Search')
    if not api.start():
        try:
            if not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE + ['down', '33800', 'ok'])
                api.channelSearchCompleteControl(60)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['exit2+7', 'info+1'])
                api.testImages('PIC2-ref', mask=api.infoBarMask)
                api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case301(api):
    # ''' 1. Stimulation"daki streami oynatiniz ve DVB-C cable network search yapiniz. (346mhz 256qm 6900sym nid:9999) Stimulation: \\manrdswfile3\Streams\Functional Test Streams\MBT_Streams\InstallationBasedonOperators\Germany\3_UM_CI+_TS131_346MHz_QAM256_DLID42_01082014.ts '''
    # ''' Beklenen Sonuc: Network search sorunsuz tamamlanmali, search sonunda kanallar bulunabilmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_03_01')
    api.setTestCaseDescription('DVB-C (346.00 Mhz) Cable Network Search')
    if not api.start():
        try:
            if not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doPowerCycle(api)
                # VestaAPI.generate_stream_signal('StreamPlayer2', 'C:\\Streams\\3_UM_CI+_TS131_346MHz_QAM256_DLID42_01082014.ts', '[DTV_DVB_C_346MHZ]')
                api.stopPlayStream(api, streamFile='3_UM_CI+_TS131_346MHz_QAM256_DLID42_01082014.ts', macro=api.DTV_DVB_C_346MHZ)
                api.doFTI(api)
                api.testImages('noChannel-ref')
                api.sendKeys(api.NETWORK_CHANNEL_SCAN + ['down', 'ok', 'down', '34600', 'ok'])
                api.channelSearchCompleteControl()
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC2-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case302(api):
    # ''' 2. Manual Search menusunden Turksat uydusunu seciniz ve network channal scan enabled yaparak belirtiken parametreler ile satellite network fast scan yapiniz. (Turksat 4A, 12423+H+30000, 12380+V+27500) '''
    # ''' Beklenen Sonuc: Network search sorunsuz tamamlanmali, search sonunda kanallar bulunabilmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_03_02')
    api.setTestCaseDescription('DVB-S (Turksat) Satellite Network Search')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2 + ['down', '12380', 'down', 'GOFIRSTITEM', 'down', '27500', 'down', 'right', 'ok'])
                api.channelSearchCompleteControl()
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC2-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case303(api):
    # ''' 3. TV"yi INTRF1"e baglayiniz, Installation menu altindan Network Channel Scan menusunu aciniz ve Digital Aerial search yapiniz. '''
    # ''' Beklenen Sonuc: Network search sorunsuz tamamlanmali, search sonunda kanallar bulunabilmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_03_03')
    api.setTestCaseDescription('DVB-T (INTRF1) Aerial Network Search')
    if not api.start():
        try:
            if not api.DVBT:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case401(api):
    # ''' 1. FTI yapiniz, ulkeyi Germany seciniz ve kanal kurulumu yapmadan FTI"i tamamlayiniz. '''
    # ''' 2. Antenna Installation menuden Antenna Type"i Diseqc seciniz ve Diseqc 1: Eutelsat 7A, Diseqc 2: Turksat, Diseqc 3: Hotbird, Diseqc 4: Astra1 secerek tum uydularda kanal arama baslatiniz. '''
    # ''' Beklenen Sonuc: Tum uydulara ait kanallari bulmali, audio-videoda bir problem olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_01')
    api.setTestCaseDescription('DVB-S (Full Diseqc) FTI Auto Search')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_FULL)
                api.channelSearchCompleteControl(3300)
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_1 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC1-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_2 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_3 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC5-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC6-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_4 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC7-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC8-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case402(api):
    # ''' 3. FTI yapiniz, ulkeyi Germany seciniz ve kanal kurulumu yapmadan FTI"i tamamlayiniz. '''
    # ''' 4. Antenna Installation menuden Antenna Type"i Diseqc seciniz ve Diseqc 1: None, Diseqc 2: Turksat, Diseqc 3: None, Diseqc 4: None secerek Turksat uydusunda kanal arama baslatiniz. '''
    # ''' Beklenen Sonuc: Turksat uydusundaki kanallari bulmalidir, audio-video"da bir problem olmamalidir '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_02')
    api.setTestCaseDescription('DVB-S (Turksat) FTI Auto Search')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['', 'turksat', '', ''])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.AUTOMATIC_CHANNEL_SCAN_DIGITAL_SATELLITE_DISEQC_2)
                api.channelSearchCompleteControl()
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC1-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC2-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case403(api):
    # ''' 5. FTI yapiniz, Ulkeyi Turkey seciniz, FTI"da broadcast type DVB-S seciniz ve anten Diseqc2: Turksat set edip, kanal aramasi yapmadan cikiniz. '''
    # ''' 6. Linkteki streame tune olunuz.(HD kanal; TRT HD) Stimulation: \\manrdswfile3\Streams\Functional Test Streams\MBT_Streams\InstallationBasedonMenu\Bisskey\ Turksat_11041_V_8400_TRTHD_BissKey\Turksat 2A3A 42.0 E 11041 V 02-05 13-45-27.ts '''
    # ''' Beklenen Sonuc: Kanal sifreli gelmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_03')
    api.setTestCaseDescription('DVB-S Bisskey Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case404(api):
    # ''' 7. Other Settings menuden Bisskey menuyu aciniz, TRT HD kanali icin 13 haneli sifrenin ilk hanesini 1 yapiniz ve geri kalanlari 0 olarak birakip kaydederek kanala geri donunuz. '''
    # ''' Beklenen Sonuc: Kanala geri donuldugunde ekranda sifreli kanal uyarisi olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_04')
    api.setTestCaseDescription('DVB-S Bisskey Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case405(api):
    # ''' 8. Program Up/Down yaparak mevcut kanala geri donunuz. '''
    # ''' Beklenen Sonuc: Sifre cozulmus olmalidir. Kanalda audio/video problemsiz alinmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_05')
    api.setTestCaseDescription('DVB-S Bisskey Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case406(api):
    # ''' 9. Linkteki streame tune olunuz.(SD kanal; ATV) Stimulation: \\manrdswfile3\Streams\Functional Test Streams\MBT_Streams\InstallationBasedonMenu\ Bisskey\ATV_BISS_15min.trp '''
    # ''' Beklenen Sonuc: Kanal sifreli gelmelidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_06')
    api.setTestCaseDescription('DVB-S Bisskey Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case407(api):
    # ''' 10. Other Settings menuden Bisskey menuyu aciniz, ATV kanali icin 13 haneli sifrenin ilk hanesini 1 yapiniz ve geri kalanlari 0 olarak birakip kaydederek kanala geri donunuz. '''
    # ''' Beklenen Sonuc: Kanala geri donuldugunde ekranda sifreli kanal uyarisi olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_07')
    api.setTestCaseDescription('DVB-S Bisskey Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case408(api):
    # ''' 11. Standby off/on yapiniz. '''
    # ''' Beklenen Sonuc: Sifre cozulmus olmalidir. Kanalda audio/video problemsiz alinmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_08')
    api.setTestCaseDescription('DVB-S Bisskey Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
        except:
            api.printError()
        api.end(False)

def Case409(api):
    # ''' 12. FTI yapiniz ve kanal arama yapmadan FTI"dan cikiniz. '''
    # ''' 13. Other Settings menuyu kontrol ediniz. '''
    # ''' Beklenen Sonuc: Kanal listesi bosken ya da satellite kanal olmadigi zaman Other Settings menu altinda Bisskey menusu cikmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_09')
    api.setTestCaseDescription('DVB-S Bisskey Menu Item Control')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api)
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.OTHER_SETTINGS_BISS_KEY)
                api.testImages('PIC1-ref', msg='Other Settings menu altinda Bisskey menusu cikmamalidir.')
        except:
            api.printError()
        api.end(False)

def Case410(api):
    # ''' 15. Antenna Installation menuden Antenna Type"i Diseqc seciniz ve Diseqc 1: Eutelsat 7A, Diseqc 2: Turksat, Diseqc 3: Hotbird, Diseqc 4: Astra1 secerek kaydedip menuden cikiniz. '''
    # ''' 16. Satellite Settings menusunden Satcodx menusune giriniz ve daha onceden USB"ye kopyaladiginiz linkteki Satcodx dosyasini TV"ye 'Download Satcodx' ile yukleyiniz. Stimulation: \\manrdswfile3\Streams\Functional Test Streams\MBT_Streams\InstallationBasedonMenu\Satcodx '''
    # ''' Beklenen Sonuc: Kanallar satcodx dosyasindan TV"ye yuklenirken, uyari OSD"si cikmali, yukleme islemi bittikten sonra 4 uyduya ait kanallar TV"de gorulmelidir, audio-video problemi olmamalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_04_10')
    api.setTestCaseDescription('DVB-S Download Satcodx')
    if not api.start():
        try:
            if not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, diseqc=['eutelsat 7a', 'turksat', 'hotbird', 'astra 1'])
                sleep(10)
                api.testImages('noChannel-ref')
                api.sendKeys(api.SATCODX + ['down', 'ok+2', 'ok+5'])
                api.testImages('PIC1-ref')
                sleep(100)
                if api.testImages('noChannel-ref', expectMatch=False)[0]:
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_1 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC2-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC3-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_2 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC4-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC5-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_3 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC6-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC7-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
                    api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY_DISEQC_4 + ['1+10', 'ok+2', 'green+5'])
                    api.testImages('PIC8-ref', mask=api.channelListMask)
                    api.sendKeys(['up+5'])
                    api.testImages('PIC9-ref', mask=api.channelListMask)
                    api.sendKeys(['exit2+10'])
                    api.audioCompare(api)
        except:
            api.printError()
        api.end(False)

def Case501(api):
    # ''' 1. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 2. FTI ekraninda Broadcast Type olarak Aerial ve Satellite(Diseq 2-Turksat) seciniz, Favourite network"u ise Aerial seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Aerial ve Satellite kanallari bulmalidir. Search sonunda Aerial ve Satellite kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda DVB-T kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_01')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, DVB-T) - Favourite Aerial')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBT:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, aerial=1, satellite=1, favNetType='aerial', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(1800, counts=2, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case502(api):
    # ''' 3. FTI ekraninda Broadcast Type olarak Aerial ve Analogue seciniz, Favourite network"u ise Analogue seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Analogue ve Aerial kanallar bulunmalidir. Search sonunda Aerial ve Analogue kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Analogue kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_02')
    api.setTestCaseDescription('FTI Auto Search - (DVB-T, Analogue) - Favourite Analogue')
    if not api.start():
        try:
            if not api.ANALOG or not api.DVBT:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, aerial=1, analogue=1, favNetType='analogue')
                api.channelSearchCompleteControl(2000, counts=2, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case503(api):
    # ''' 4. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 5. FTI ekraninda Broadcast Type olarak Cable ve Satellite(Diseq 2-Turksat) seciniz, Favourite network"u ise Satellite seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Cable ve Satellite kanallar bulunmalidir. Search sonunda Cable ve Satellite kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Satellite kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_03')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, DVB-C) - Favourite Satellite')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, cable=1, satellite=1, favNetType='satellite', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(1800, counts=2, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case504(api):
    # ''' 6. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 7. FTI ekraninda Broadcast Type olarak Cable ve Analogue seciniz, Favourite network"u ise Analogue seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Cable ve Analogue kanallar bulunmalidir. Search sonunda Cable ve Analogue kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Analogue kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_04')
    api.setTestCaseDescription('FTI Auto Search - (DVB-C, Analogue) - Favourite Analogue')
    if not api.start():
        try:
            if not api.DVBC or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, cable=1, analogue=1, favNetType='analogue')
                api.channelSearchCompleteControl(1800, counts=2, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case505(api):
    # ''' 8. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 9. FTI ekraninda Broadcast Type olarak Analogue ve Satellite(Diseq 2-Turksat) seciniz, Favourite network"u ise Satellite seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Satellite ve Analogue kanallar bulunmalidir. Search sonunda Satellite ve Analogue kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Satellite kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_05')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, Analogue) - Favourite Satellite')
    if not api.start():
        try:
            if not api.DVBS or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, analogue=1, satellite=1, favNetType='satellite', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(1800, counts=2, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case506(api):
    # ''' 10. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 11. FTI ekraninda Broadcast Type olarak Analogue, Cable ve Aerial seciniz, Favourite network"u ise Aerial seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Analogue, Cable ve Aerial kanallar bulunmalidir. Search sonunda Analogue, Cable ve Aerial kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Aerial kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_06')
    api.setTestCaseDescription('FTI Auto Search - (DVB-T, DVB-C, Analogue) - Favourite Aerial')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBC or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, cable=1, analogue=1, aerial=1, favNetType='aerial')
                api.channelSearchCompleteControl(1800, counts=3, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case507(api):
    # ''' 12. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 13. FTI ekraninda Broadcast Type olarak Analogue, Aerial ve Satellite seciniz, Favourite network"u ise Aerial seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Analogue, Aerial ve Satellite kanallar bulunmalidir. Search sonunda Analogue, Cable ve Aerial kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Aerial kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_07')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, DVB-T, Analogue) - Favourite Aerial')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBT or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, aerial=1, analogue=1, satellite=1, favNetType='aerial', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(1800, counts=3, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case508(api):
    # ''' 14. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 15. FTI ekraninda Broadcast Type olarak Cable, Aerial ve Satellite(Diseq 2-Turksat) seciniz, Favourite network"u ise Cable seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Cable, Aerial ve Satellite kanallar bulunmalidir. Search sonunda Cable, Aerial ve Satellite kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Cable kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_08')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, DVB-T, DVB-C) - Favourite Cable')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBC or not api.DVBS:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, aerial=1, cable=1, satellite=1, favNetType='cable', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(1800, counts=3, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case509(api):
    # ''' 16. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 17. FTI ekraninda Broadcast Type olarak Analogue, Cable ve Satellite(Diseq 2-Turksat) seciniz, Favourite network"u ise Satellite seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Analogue, Cable ve Satellite kanallar bulunmalidir. Search sonunda Analogue, Cable ve Satellite kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Satellite kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_09')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, DVB-C, Analogue) - Favourite Satellite')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBC or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, analogue=1, cable=1, satellite=1, favNetType='satellite', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(1800, counts=3, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case510(api):
    # ''' 18. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 19. FTI ekraninda Broadcast Type olarak Analogue, Aerial, Cable ve Satellite(Diseq 2-Turksat) seciniz, Favourite network"u ise Aerial seciniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Analogue, Cable, Aerial ve Satellite kanallar bulunmalidir. Search sonunda Analogue, Aerial, Cable ve Satellite kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda Aerial kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_10')
    api.setTestCaseDescription('FTI Auto Search - (DVB-S Turksat, DVB-T, DVB-C, Analogue) - Favourite Aerial')
    if not api.start():
        try:
            if not api.DVBS or not api.DVBT or not api.DVBC or not api.ANALOG:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, aerial=1, cable=1, satellite=1, analogue=1, favNetType='aerial', diseqc=['', 'turksat', '', ''])
                api.channelSearchCompleteControl(3600, counts=4, finish=False)
                api.testImages('PIC1-ref', mask=api.scanStatisticMask)
                api.sendKeys(['ok+10', 'exit2+10', 'info+1'])
                api.testImages('PIC2-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['progup+10', 'info+1'])
                api.testImages('PIC3-ref', mask=api.broadcastTypeMask)
                api.sendKeys(['1+10', 'ok+2', 'green+5'])
                api.testImages('PIC4-ref', mask=api.channelListMask)
                api.sendKeys(['up+5'])
                api.testImages('PIC5-ref', mask=api.channelListMask)
        except:
            api.printError()
        api.end(False)

def Case511(api):
    # ''' 20. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 21. FTI ekraninda Broadcast Type olarak Cable"i seciniz, Scan Encrypted Channels secenegini enable set edip kanal aramaya baslatiniz. '''
    # ''' Beklenen Sonuc: Search sonunda sifreli kanallari da bulmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_11')
    api.setTestCaseDescription('FTI DVB-C Auto Search - Encrypted Channels Enable')
    if not api.start():
        try:
            if not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, cable=1)
                api.channelSearchCompleteControl(counts=1)
                api.sendKeys(['ok+10'] + api.CHANNEL_LIST_SCRAMBLED + ['exit2+10'])
                api.testImages('scrambled-ref', mask=api.scrambledMask)
        except:
            api.printError()
        api.end(False)

def Case512(api):
    # ''' 22. FTI yapiniz ve ulkeyi Germany seciniz. '''
    # ''' 23. FTI ekraninda Broadcast Type olarak Aerial ve Cable seciniz, Favourite network"u Cable seciniz, Scan Encrypted Channels secenegini disable set ediniz ve kanal arama baslatiniz. (Vestel sistem yayini) '''
    # ''' Beklenen Sonuc: Aerial ve Cable sifresiz kanallari bulmalidir. Search sonunda Aerial ve Cable kanallarindan kacar adet (TV/Radio) kanal bulunduguna dair bilgi vermelidir. Kanal listesinin en basinda DVB-C kanallar olmalidir. '''
    api.setTestCaseName('Installation_BasedOn_Menu_05_12')
    api.setTestCaseDescription('FTI Auto Search DVB-T, DVB-C Favourite Aerial - Encrypted Channels Disabled')
    if not api.start():
        try:
            if not api.DVBT or not api.DVBC:
                api.updateTestResult('N/A')
            else:
                api.doFTI(api, aerial=1, cable=1, scanEncryptedChannels=0)
                api.channelSearchCompleteControl(counts=2)
                CHANNEL_LIST_SCRAMBLED = api.CHANNEL_LIST_SCRAMBLED
                CHANNEL_LIST_SCRAMBLED[len(CHANNEL_LIST_SCRAMBLED)-1] = ''
                CHANNEL_LIST_SCRAMBLED.remove('')
                api.sendKeys(['ok+10'] + CHANNEL_LIST_SCRAMBLED)
                api.testImages('PIC1-ref')
                api.sendKeys(['exit2*2/3'])
        except:
            api.printError()
        api.end(False)

