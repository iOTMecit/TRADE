# ParentalRating Germany Control - AgeOff

from customTime import sleep

def init(api, country):
    try:
        global ftiCompleted
        api.doPowerCycle(api)
        api.doFTI(api, countryName=country)
        ftiCompleted = 1
    except:
        api.printError()

def test(api):
    try:
        global ftiCompleted
        ftiCompleted = 0

        ParentalRating_01_01(api) # GERMANY
        ParentalRating_02_01(api) # TURKEY
        ParentalRating_03_01(api) # AUSTRALIA
        ParentalRating_04_01(api) # FRANCE
        ParentalRating_05_01(api) # SPAIN
        ParentalRating_06_01(api) # SWEDEN
        ParentalRating_07_01(api) # AUSTRIA
        ParentalRating_08_01(api) # BELGIUM
        ParentalRating_09_01(api) # UK
        ParentalRating_10_01(api) # ITALY
    except:
        api.printError()

def ParentalRating_01_01(api): # GERMANY
    # GERMANY
    # 3- BR-alpha - Rate 0
    global ftiCompleted
    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_01_01')
    api.setTestCaseDescription('ParentalRating Germany Control - AgeOff')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. BR-alpha kanalini aciniz (Rate - 0) '''
            api.sendKeys(['3+5'])
            # ''' 2. Maturity Lock 'Age 4 ile 18 ' herhangi birini seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. Enter PIN sorgusuna dusmemelidir. Audio ve Video"da bir problem olmamalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(0, 0, 8), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 4. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_02')
    api.setTestCaseDescription('ParentalRating Germany Control - Age 4')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB) 
            # ''' 1. EinsPlus kanalini aciniz. '''
            api.sendKeys(['5+5'])
            # ''' 2. Maturity Lock 'Age 4' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE4)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey+'+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_03')
    api.setTestCaseDescription('ParentalRating Germany Control - Age 10')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Einsfestival kanalini aciniz. '''
            api.sendKeys(['4+5'])
            # ''' 2. Maturity Lock 'Age 10' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE10)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(3, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_04')
    api.setTestCaseDescription('ParentalRating Germany Control - Age 12')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. tagesschau24 kanalini aciniz. '''
            api.sendKeys(['7+5'])
            # ''' 2. Maturity Lock 'Age 10' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE12)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(0, 0, 10), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_05')
    api.setTestCaseDescription('ParentalRating Germany Control - Age 16')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. arte kanalini aciniz. '''
            api.sendKeys(['2+2'])
            # ''' 2. Maturity Lock 'Age 16' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE16)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_06')
    api.setTestCaseDescription('ParentalRating Germany Control - Age 17')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Das Erste HD kanalini aciniz. '''
            api.sendKeys(['1+2'])
            # ''' 2. Maturity Lock 'Age 17' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE17)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_07')
    api.setTestCaseDescription('ParentalRating Germany Control - Age 18')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_08')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Standby Off/On Scart Out Connect TV')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Standby off/on yapiniz. '''
            # ''' 2. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            # ''' 3. Enter PIN sorgusu ekranda iken, scart out"tan goruntu almak icin scart"tan TV"ye baska bir TV"yi baglayiniz. '''
            # ''' 4. Scart out"tan audio-video alinmamalidir. '''
            # ''' 5. Default PIN '0000' giriniz. '''
            # ''' 6. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_09')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Standby Off/On HeadPhone')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Standby off/on yapiniz. '''
            # ''' 2. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            # ''' 3. Enter PIN sorgusu ekranda iken, headphone takiniz. '''
            # ''' 4. Main ses alinmamalidir. '''
            # ''' 5. Default PIN '0000' giriniz. '''
            # ''' 6. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_10')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Power Off/On Scart Out Connect TV')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Power off/on yapiniz. '''
            # ''' 2. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            # ''' 3. Enter PIN sorgusu ekranda iken, scart out"tan goruntu almak icin scart"tan TV"ye baska bir TV"yi baglayiniz. '''
            # ''' 4. Scart out"tan audio-video alinmamalidir. '''
            # ''' 5. Default PIN '0000' giriniz. '''
            # ''' 6. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_11')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Power Off/On HeadPhone')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Power off/on yapiniz. '''
            # ''' 2. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            # ''' 3. Enter PIN sorgusu ekranda iken, headphone takiniz. '''
            # ''' 4. Main ses alinmamalidir. '''
            # ''' 5. Default PIN '0000' giriniz. '''
            # ''' 6. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_12')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After Manuel Search')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 0. ***ONEMLI*** Bu case baslangicinda Maturity 18 secilmeli ve Phoenix kanali izleniyor olmalidir. '''
            api.sendKeys(['6+10'])
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18 + ['0000+10'])
            # ''' 1. Mevcut kanalin bulundugu mux"a manuel search ile tekrar tune olunuz ve mevcut kanali aciniz. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 2. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+15'])
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+10'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_13')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After YouTube')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken Mybtn1 ile youtube giris yapmaya calisiniz. '''
            api.sendKeys(['mybutton+20'])
            controlImage = []
            controlImage.append(api.grabImage('youTubeMainPage')[0])
            # ''' 4. Herhangi bir video"yu play ediniz ve 30 sn sonra exit ile cikip kanala geri donunuz. '''
            api.sendKeys(['ok+10*2', 'ok+0.5']) # Video"yu baslat, Info banner ac
            controlImage.append(api.grabImage('youTubeFirstVideoPlay')[0])
            api.showImages(controlImage, nView=2, msg='Youtube uygulamasina giris yapilabilmelidir ve video oynatilabilmelidir.')
            api.sendKeys(['exit2*2+15'])
            # ''' 5. Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 6. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+10'])
            # ''' 7. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 8. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_14')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After Portal')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken Portal"a giris yapmaya calisiniz. '''
            api.sendKeys(['pippap+50', 'down*40', 'ok+10*3'])
            # ''' 4. Portal"a giris yapilabilmelidir. '''
            controlImage = []
            controlImage.append(api.grabImage('portalMainPage')[0])
            # ''' 4. EXIT tusu ile Portal"dan cikin. '''
            api.sendKeys(['exit2*2+10'])
            # ''' 5. Kanala geri donuldugunde PIN sorgusu ekranda olmalidir, kanalda audio/video olmamalidir. '''
            api.testImages('_enterPin-ref', msg='Kanala geri donuldugunde PIN sorgusu ekranda olmalidir. Video olmamalidir.')
            api.checkAudio(expectMatch=False, msg='Kanalda audio olmamalidir.')
            # ''' 6. Open Browser ve herhangi bir uygulama aciniz ve 40 sn sonra Exit ile kanala geri donunuz. '''
            api.sendKeys(['pippap+50', 'blue+3', 'right+5', 'ok+40'])
            controlImage.append(api.grabImage('firstApplicationInPortal')[0])
            api.showImages(controlImage, nView=2, msg='1:Portal"a giris yapilabilmelidir. 2:Herhangi bir uygulama acilmalidir.')
            # ''' 7. EXIT tusu ile Portal"dan cikin. '''
            api.sendKeys(['exit2*2+20'])
            # ''' 8. Kanala geri donuldugunde PIN sorgusu ekranda olmalidir, kanalda audio/video olmamalidir. '''
            api.testImages('_enterPin-ref', msg='Kanala geri donuldugunde PIN sorgusu ekranda olmalidir. Video olmamalidir.')
            api.checkAudio(expectMatch=False, msg='Kanalda audio olmamalidir.')
            # ''' 9. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 10. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_15')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Wrong Password')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken yanlis PIN(88888) olacak sekilde 4"ten fazla digit girmeye calisiniz. '''
            api.sendKeys(['88888+1'])
            # ''' 4. 4"ten fazla digit girilmesine izin verilmemelidir. Sifrenin yanlis girildigine dair uyari mesaji vermelidir. '''
            api.testImages('_wrongPin-ref', msg='4"ten fazla digit girilmesine izin verilmemelidir. Sifrenin yanlis girildigine dair uyari mesaji vermelidir.')
            # ''' 5. Default PIN '0000' giriniz. '''
            api.sendKeys(['exit2*2+5', '0000+2']) # Wrong Pin OSD"si varsa kaldirilir.
            # ''' 6. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 7. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_16')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Opening Teletext')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken TEXT tusu ile Teletext acmaya calisiniz. '''
            api.sendKeys(['text+20'])
            # ''' 4. Teletext acilmamalidir. '''
            api.testImages('_enterPin-ref', msg='Teletext acilmamalidir.')
            # ''' 5. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 6. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 7. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_17')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Opening HBBTV')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken RED tusu ile HBBTV acmaya calisiniz. '''
            api.sendKeys(['red+20'])
            # ''' 4. HBBTV acilmamalidir. '''
            api.testImages('_enterPin-ref', msg='HBBTV acilmamalidir.')
            # ''' 5. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 6. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 7. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_18')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After Changing TV Source')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB+['ok+7'])
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken Source tusu ile source degistiriniz ve tekrar mevcut kanala geri donunuz. '''
            api.selectSource(source='EXT1')
            # ''' 4. Source degisikligi yapilabilmelidir. '''
            api.sendKeys(['exit2*2', 'aux+1'])
            api.testImages('_sourceList_Ext1-ref', msg='Source listesi gorunmelidir.')
            api.sendKeys(['exit2*2+8', 'info+0.5'])
            api.testImages('source_EXT1-ref', msg='Source degisikligi yapilabilmelidir. ( EXT1 )')
            # ''' 5. Tekrar mevcut kanala geri donunuz. '''
            api.sendKeys(['6+10'])
            # ''' 6. Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Enter PIN sorgu ekrani cikmalidir.')
            # ''' 7. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 8. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 9. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_19')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Opening Picture/Sound Menu + EPG')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken Menu tusu ile Picture-Sounde menulerini aciniz ve menulerden cikiniz. '''
            api.sendKeys(api.PICTURE_MENU)
            api.testImages('pictureMenu-ref', msg='PIN sorgu ekraninda iken Picture Menu acilabilmelidir.')
            api.sendKeys(api.SOUND_MENU)
            api.testImages('soundMenu-ref', msg='PIN sorgu ekraninda iken Sound Menu acilabilmelidir.')
            # ''' 4. PIN sorgu ekrani ekranda iken rcguide tusu ile EPG acmaya calisiniz. '''
            api.sendKeys(['exit2*2+1', 'guide+20'])
            # ''' 5. EPG acilmamalidir. '''
            api.testImages('_enterPin-ref', msg='EPG acilmamalidir.')
            api.sendKeys(['exit2*2+5'])
            # ''' 6. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+10'])
            # ''' 7. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 8. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_20')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - Program Up/Down On Pin Screen')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. PIN sorgusu ekranda iken, touchpad ile Program Up ve Program Down yaparak mevcut kanala geri donunuz. '''
            # ''' 2. Ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_21')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After Standby Search (Pin Screen)')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Standby search"u on yapiniz ve PIN sorgusu ekranda iken, standby off/on yapiniz. '''
            # ''' 2. Standby search sonunda TV acildiginda Enter PIN sorgusu gelmelidir. Maturity lock korunmalidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_22')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After Standby Search')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Standby search"u on yapiniz ve PIN sorgusu girilmis halde audio-video alinir durumdayken, standby off/on yapiniz. '''
            # ''' 2. Standby search sonunda TV acildiginda Enter PIN sorgusu gelmelidir. Maturity lock korunmalidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_23')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - After Changing TV Source (HDMI)')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'GERMANY')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_722FREG_6900SYMB)
            # ''' 1. Phoenix kanalini aciniz. '''
            api.sendKeys(['6+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AGE18)
            # ''' 3. PIN sorgu ekrani ekranda iken Source tusu ile source degistiriniz ve tekrar mevcut kanala geri donunuz. '''
            api.selectSource(source='HDMI1')
            # ''' 4. Source degisikligi yapilabilmelidir '''
            api.sendKeys(['exit2*2', 'aux+1'])
            api.testImages('source_HDMI1-ref', msg='Source degisikligi yapilabilmelidir.')
            # ''' 5. Tekrar mevcut kanala geri donunuz. '''
            api.sendKeys(['exit2*2+1', '6+15'])
            # ''' 6. Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Enter PIN sorgu ekrani cikmalidir. Goruntu alinmamalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 7. PIN sorgusu ekranda iken iki kez MUTE tusuna basiniz '''
            # ''' 8. Mute kontrolunde ses alinmamalidir. '''
            api.sendKeys(['mute+2'])
            api.checkAudio(expectMatch=False, msg='Mute kontrolunde ses alinmamalidir.')
            api.sendKeys(['mute+2'])
            api.checkAudio(expectMatch=False, msg='Mute kontrolunde ses alinmamalidir.')
            # ''' 9. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 10. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_24')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - System Broadcast - Changing Sources')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Vestel DVB-T sistem yayinina auto search ile tune olunuz. '''
            # '''    Rai Sport piu kanalina maturity lock 'age 4' kurunuz. '''
            # '''    HDMI, SCART, Media Browser, YPbPr ve PC source "lar arasinda gecis yapiniz. '''
            # ''' 2. Rai Sport piu kanalina tekrar gectiginde Enter PIN sorgusu cikmalidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_25')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - System Broadcast - DVB-C/S and Analog Channels')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. DVB-C-S ve Analag kanallar arasinda gecis yapiniz. '''
            # ''' 2. Rai Sport piu kanalina tekrar gectiginde Enter PIN sorgusu cikmalidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_01_26')
    api.setTestCaseDescription('ParentalRating Germany Control (Other) - System Broadcast - Zapping Test')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Zapping testi yapiniz. (Program Up/Down, kanal listesinden navigation Up/Down-OK ve Swap tusu ile) '''
            # ''' 2. Rai Sport piu kanalina her gecisinde Enter PIN sorgusu ekrana gelmelidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

def ParentalRating_02_01(api): # TURKEY
    global ftiCompleted
    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_02_01')
    api.setTestCaseDescription('ParentalRating Turkey Control - D_Smart Age')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Ulkeyi Turkey seciniz. '''
            # ''' D-Smart kurulumu yapiniz ve D-Smart modulunu takip kanallarin cozulmesini bekleyiniz. '''
            # ''' Age bilgisi gelen ve subtitle bilgisi olan bir MOVIE kanalini aciniz. (Age 4-18 arasi) '''
            # ''' Maturity Lock 'Age 4' seciniz. '''
            # ''' 2. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            # ''' 3. Default PIN '0000' giriniz. '''
            # ''' 4. Audio-Video problemsiz alinmalidir. '''
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_02_02')
    api.setTestCaseDescription('ParentalRating Turkey Control - D_Smart Subtitle')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Subtitle on yapiniz. '''
            # ''' 2. Audio-Video-Subtitle problemsiz alinmalidir. '''
            # ''' 3. Program Up yapiniz ve Program Down yaparak mevcut kanala geri donunuz. '''
            # ''' 4. Pin sorgu ekrani cikmali, audio-video alinamamali, subtitle gorulmemelidir. '''
        except:
            api.printError()
        api.end(False)

def ParentalRating_03_01(api): # AUSTRALIA
    # ''' 73800 6875 '''
    # ''' AUSTRALIA '''
    # ''' 2-ABC1-P '''
    # ''' 21-ABC1-G '''
    # ''' 22-ABC2/ABC4-C '''
    # ''' 23-ABC3-PG '''
    # ''' 24-ABC Nevs 24- AV '''
    # ''' 200-ABC Dig Music-M '''
    # ''' 201-ABC Jazz - MA '''

    # ''' 74600 6875 '''
    # ''' AUSTRALIA '''
    # ''' 2-ABC1- M '''
    # ''' 21-ABC1-AV '''
    # ''' 22-ABC2/ABC4-MA '''
    # ''' 23-ABC3- R '''
    # ''' 24-ABC Nevs 24- '''
    # ''' 200-ABC Dig Music- P '''
    # ''' 201-ABC Jazz - C '''
    global ftiCompleted
    ftiCompleted = 0

    api.setTestCaseName('ParentalRating_03_01')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock C')
    if not api.start():
        try:
            # ''' 0. FTI yapiniz, ulkeyi Australia set ediniz. '''
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'C' olan kanali aciniz. (ABC JAZZ) '''
            api.sendKeys(['201+5'])
            # ''' 2. Maturity Lock 'C' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_C)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(8, 0, 8), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_02')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock M')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'M' olan kanali aciniz. (ABC1) '''
            api.sendKeys(['2+2'])
            # ''' 2. Maturity Lock 'M' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_M)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 5, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_03')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock MA')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'MA' olan kanali aciniz. (ABC2 ABC4) '''
            api.sendKeys(['22+2'])
            # ''' 2. Maturity Lock 'MA' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_MA)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_04')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock AV')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'AV' olan kanali aciniz. (ABC1_2) '''
            api.sendKeys(['21+2'])
            # ''' 2. Maturity Lock 'AV' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_AV)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_05')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock R')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'R' olan kanali aciniz. (ABC3) '''
            api.sendKeys(['23+2'])
            # ''' 2. Maturity Lock 'R' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_R)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_06')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock P')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'P' olan kanali aciniz. (ABC Dig Music) '''
            api.sendKeys(['200+2'])
            # ''' 2. Maturity Lock 'P' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_P)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_07')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock Off')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_746FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Off' olan kanali aciniz. (ABC News 24) '''
            api.sendKeys(['24+2'])
            # ''' 2. Maturity Lock 'P-C-G-M-MA-AV-R ya da PG' herhangi birini seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_P)
            # ''' 3. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 4. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir. Pin sorgusu cikmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 7. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir. Pin sorgusu cikmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 8. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_03_08')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock PG')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_738FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'PG' olan kanali aciniz. (ABC3) '''
            api.sendKeys(['23+2'])
            # ''' 2. Maturity Lock 'PG' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_PG)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_03_09')
    api.setTestCaseDescription('ParentalRating Australia Control - Maturity Lock G')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'AUSTRALIA')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_738FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'G' olan kanali aciniz. (ABC1). 2 tane ABC1 kanali var DIKKAT* '''
            api.sendKeys(['21+2'])
            # ''' 2. Maturity Lock 'G' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_G)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys(['0000+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_04_01(api): # FRANCE
    # ''' FRANCE '''
    # ''' 8-D8- Age 10 '''
    # ''' 14-France 4- Age 16 '''
    # ''' 15-BFM TV- Age12 '''
    # ''' 16-i>TELE- Age 16 '''
    # ''' 17-D17- Age 18 '''
    # ''' 18-Gulli-Parental_No_Age '''
    global ftiCompleted
    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_04_01')
    api.setTestCaseDescription('ParentalRating France Control - Age 18')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'FRANCE')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_730FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 18' olan kanali aciniz. (D17) '''
            # api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE18)
            api.sendKeys(['8+5', '17+8'])
            # ''' 2. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 3. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 4. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 5. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 6. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 7. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 8. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 9. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 10. Parental Maturity Age 18 yap. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE18)
            # ''' 11. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_04_02')
    api.setTestCaseDescription('ParentalRating France Control - Age 10')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'FRANCE')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_730FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 10' olan kanali aciniz. (D8) '''
            api.sendKeys(['8+2'])
            # ''' 2. Maturity Lock"u '10' set ediniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE10)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 11. Parental Maturity Age 18 yap. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE18)
            # ''' 12. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_04_03')
    api.setTestCaseDescription('ParentalRating France Control - Age 12')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'FRANCE')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_730FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 12' olan kanali aciniz. (BFM TV) '''
            api.sendKeys(['15+2'])
            # ''' 2. Maturity Lock"u '12' set ediniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE12)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 11. Parental Maturity Age 18 yap. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE18)
            # ''' 12. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_04_04')
    api.setTestCaseDescription('ParentalRating France Control - Age 16')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'FRANCE')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_730FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 16' olan kanali aciniz. (ITELE) '''
            api.sendKeys(['14+2'])
            # ''' 2. Maturity Lock"u '16' set ediniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE16)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 11. Parental Maturity Age 18 yap. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE18)
            # ''' 12. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_04_05')
    api.setTestCaseDescription('ParentalRating France Control - Parental Approval')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'FRANCE')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_730FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 16' olan kanali aciniz. (TMC) '''
            api.sendKeys(['16+2'])
            # ''' 2. Maturity Lock"u 'PARENTALAPPROVAL' set ediniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_PARENTALAPPROVAL)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            # ''' 11. Parental Maturity Age 18 yap. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD1111_AGE18)
            # ''' 12. FTI sirasinda belirlediginiz PIN"i giriniz. Default '1111' '''
            api.sendKeys([api.defaultParentKey_France + '+2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_05_01(api): # SPAIN
    # ''' SPAIN '''
    # ''' 1-Telecinco HD- Age 13 '''
    # ''' 2-Boing- Age 7 '''
    # ''' 3-MTV- Age 18 '''
    # ''' 4-Paramount Channel- parental x rated '''
    global ftiCompleted
    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_05_01')
    api.setTestCaseDescription('ParentalRating Spain Control - Age 13')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SPAIN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 13' olan kanali aciniz. (Telecinco HD) '''
            api.sendKeys(['1+2'])
            # ''' 2. Maturity Lock 'Age 13' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_AGE13)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_05_02')
    api.setTestCaseDescription('ParentalRating Spain Control - Age 18')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SPAIN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 18' olan kanali aciniz. (MTV) '''
            api.sendKeys(['3+2'])
            # ''' 2. Maturity Lock 'Age 18' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_AGE18)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_05_03')
    api.setTestCaseDescription('ParentalRating Spain Control - X-Rated')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SPAIN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'X-Rated' olan kanali aciniz. (Paramount Channel) '''
            api.sendKeys(['4+2'])
            # ''' 2. Maturity Lock 'X-Rated' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_XRATED)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_05_04')
    api.setTestCaseDescription('ParentalRating Spain Control - Age 7')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SPAIN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Age 7' olan kanali aciniz. (Boing) '''
            api.sendKeys(['2+2'])
            # ''' 2. Maturity Lock 'Age 7' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SPAIN_AGE7)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_06_01(api): # SWEDEN
    # ''' SWEDEN '''
    # ''' 1-SVT1- Age 12 (Adult) '''
    # ''' 2-SVT2- Age 3 (Adult) '''
    # ''' 4-TV4- Children 7 (Children) '''
    # ''' 125-Kunskapskanalen - Age 14 (Adult) '''
    # ''' 153- SVTB/SVT24- Age 16 (Adult) '''
    # ''' 450-Loakalkanal 1- No information '''
    # ''' 701-SVT1 talande text- Age 11 (Youth) '''
    # ''' 702-SVT1 talande text - Age 8 (Youth) '''
    global ftiCompleted
    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_06_01')
    api.setTestCaseDescription('ParentalRating Sweden Control - Youth')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SWEDEN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_690FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Youth' olan kanali aciniz. (SVT1 TALANDE TEXT), Bu kanalda ses yok. Bu yuzden fail veriyor. '''
            api.sendKeys(['702+2'])
            # ''' 2. Maturity Lock 'Youth' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SWEDEN_YOUTH)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_06_02')
    api.setTestCaseDescription('ParentalRating Sweden Control - Adult')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SWEDEN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_690FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Adult' olan kanali aciniz. (SVTBSVT24) '''
            api.sendKeys(['153+2'])
            # ''' 2. Maturity Lock 'Adult' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SWEDEN_ADULT)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_06_03')
    api.setTestCaseDescription('ParentalRating Sweden Control - Children')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'SWEDEN')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_690FREG_6875SYMB)
            # ''' 1. Parental Rating"i 'Children' olan kanali aciniz. (TV4) '''
            api.sendKeys(['4+2'])
            # ''' 2. Maturity Lock 'Children' seciniz. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_SWEDEN_CHILDREN)
            # ''' 3. Audio-Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir. '''
            api.testImages('_enterPin-ref', msg='Video kesilmelidir, Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Audio kesilmelidir.')
            # ''' 4. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 5. Audio ve Video problemsiz alinmalidir. '''
            api.videoAnalysis(duration=(20, 0, 20), tolerance=(5, 0, 5), msg='Video"da bir problem olmamalidir.')
            api.checkAudio(msg='Audio"da bir problem olmamalidir.')
            # ''' 6. Standby off/on yapiniz. '''
            api.doStandByCycle(api)
            # ''' 7. Standby on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Standby on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Standby on sonrasi audio alinmamalidir.')
            # ''' 8. Power off/on yapiniz. '''
            api.doPowerCycle(api)
            # ''' 9. Power on sonrasi ekranda PIN sorgusu cikmali, audio-video alinmamalidir. '''
            api.testImages('_enterPin-ref', msg='Power on sonrasi video alinmamalidir. Enter PIN sorgu ekrani cikmalidir.')
            api.checkAudio(expectMatch=False, msg='Power on sonrasi audio alinmamalidir.')
            # ''' 10. Default PIN '0000' giriniz. '''
            api.sendKeys([api.defaultParentKey + '+2'])
            # ''' 11. Parental Maturity kapatilir. '''
            api.sendKeys(api.PARENTALMENU_MATURITY_PSWRD0000_OFF)
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_07_01(api): # AUSTRIA
    api.setTestCaseName('ParentalRating_07_01')
    api.setTestCaseDescription('ParentalRating Austria Control - Default Parental Rating')
    if not api.start():
        try:
            init(api, 'AUSTRIA')
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_738FREG_6875SYMB)
            # ''' 1. FTI yapiniz, ulkeyi Austria set ediniz. '''
            api.sendKeys(['ok*3+2'])
            # ''' 2. Parental Settings menuyu kontrol ediniz. '''
            api.sendKeys(api.PARENTAL_MENU + [api.defaultParentKey + '+1'])
            api.testImages('parentalSettings-ref', mask=api.parentMaturityMask, msg='Ulke Austria icin default parental rating 18 gelmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_08_01(api): # BELGIUM
    api.setTestCaseName('ParentalRating_08_01')
    api.setTestCaseDescription('ParentalRating Belgium Control - Default Parental Rating')
    if not api.start():
        try:
            # ''' 1. FTI yapiniz, ulkeyi Belgium set ediniz. '''
            init(api, 'BELGIUM')
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB)
            api.sendKeys(['ok*3+2'])
            # ''' 2. Parental Settings menuyu kontrol ediniz. '''
            api.sendKeys(api.PARENTAL_MENU + [api.defaultParentKey_France + '+1'])
            api.testImages('parentalSettings-ref', mask=api.parentMaturityMask, msg='Ulke Belgium icin default parental rating 17 gelmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_09_01(api): # UK
    global ftiCompleted
    ftiCompleted = 0
    api.setTestCaseName('ParentalRating_09_01')
    api.setTestCaseDescription('ParentalRating UK Control - Default Parental Rating')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'UK')
                # ''' \\manrdswfile\DesignVerification\MBT_Streams\ParentalRating\UK\Guidance\si18_21c_2k_64qam_cr23_gi32_7_a0.ts oynat '''
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_706FREG_6875SYMB)
            # ''' 1. FTI yapiniz, ulkeyi UK set ediniz. '''
            # ''' 2. Parental Settings menuyu kontrol ediniz. '''
            api.sendKeys(api.PARENTAL_MENU + [api.defaultParentKey + '+1'])
            api.testImages('parentalSettings-ref', mask=api.parentMaturityMask, msg='Ulke UK icin parental rating uygulamasi yoktur.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('ParentalRating_09_02')
    api.setTestCaseDescription('ParentalRating UK Control - EPG Extended Info')
    if not api.start():
        try:
            if not ftiCompleted:
                init(api, 'UK')
                api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_706FREG_6875SYMB)
            # ''' 1. Channel 8i aciniz, EPG, den Extended Info"yu kontrol ediniz. '''
            api.sendKeys(['8+2'])
            api.sendKeys(['exit2*2+2', 'mheg_epg+5', 'info+5'])
            api.testImages('SIT8_guidance_extendedInfo-ref', mask=api.guidanceMhegEpgMask, msg='Extended Info"da guidance bilgisi gorulmelidir.')
            api.sendKeys(['info+5', 'exit2*2+2', '1+2', 'mheg_epg+5', 'info+5'])
            api.testImages('SIT1_guidance_extendedInfo-ref', mask=api.guidanceMhegEpgMask, msg='Extended Info"da guidance bilgisi olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def ParentalRating_10_01(api): # ITALY
    api.setTestCaseName('ParentalRating_10_01')
    api.setTestCaseDescription('ParentalRating Italy Control - Default Parental Rating')
    if not api.start():
        try:
            # ''' 1. FTI yapiniz, ulkeyi Italy set ediniz. '''
            init(api, 'ITALY')
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_698FREG_6875SYMB)
            # ''' 2. Parental Settings menuyu kontrol ediniz. '''
            api.sendKeys(api.PARENTAL_MENU + [api.defaultParentKey_France + '+1'])
            api.testImages('parentalSettings-ref', mask=api.parentMaturityMask, msg='Ulke Italy icin default parental rating 18 gelmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

