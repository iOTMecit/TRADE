# EPG Test Suite

from customTime import sleep

def test(api):
    try:
        EPG_TC01(api)
        EPG_TC02(api)
        EPG_TC03(api)
        EPG_TC04(api)
        EPG_TC06(api)
    except:
        api.printError()

def doFTI_ImportChList(api, c):
    try:
        global ftiCompleted
        api.doPowerCycle(api)
        api.doFTI(api)
        api.sendKeys(api.IMPORT_CHANNEL_LIST)
        ftiCompleted = 1
    except:
        api.printError()

def EPG_TC01(api):
    global ftiCompleted
    ftiCompleted = 0

    api.setTestCaseName('EPG_TC01_01')
    api.setTestCaseDescription('EPG - Enter/Exit - MHEG to EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-T CH49 BBC ONE) kanalini aciniz. '''
            api.sendKeys(['1+10'])
            # ''' 2. MHEG aciniz. (red) '''
            api.sendKeys(['red+5'])
            api.testImages('BbcOne_MHEG-ref', msg='BBC ONE MHEG acildigi gorulmelidir.')
            # ''' 3. EPG'ye giriniz. (mheg_epg) '''
            api.sendKeys(['mheg_epg+3'])
            api.testImages('BbcOne_EPG-ref', mask=api.EPGChannelNameMask, msg='EPG ye girebilmelidir, Mheg kapanmalidir.')
            # ''' 4. EPG'den cikiniz. '''
            api.sendKeys(['mheg_epg+10', 'info+0.5'])
            # ''' 5. Mevcut kanala geri donmelidir, ses ve goruntude problem olmamalidir, MHEG acik olmamalidir ancak tekrar acilabilir olmalidir. '''
            api.testImages('_BbcOne-ref', mask=api.infoBarMask, msg='Mevcut kanala geri donmelidir. MHEG acik olmamalidir.')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            # ''' 6. MHEG tekrar acilabilir olmalidir. (red) '''
            api.sendKeys(['red+3'])
            api.testImages('BbcOne_MHEG-ref', msg='BBC ONE MHEG acildigi gorulmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_02')
    api.setTestCaseDescription('EPG - Enter/Exit - Subtitle On to EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-T CH49 BBC ONE) kanalini aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Subtitle aciniz. (subtitles) '''
            api.sendKeys(['subtitles+15'])
            api.grabImage('BbcOne_SubtitleOn', delay=5, count=3, nView=3, msg='Subtitle acildigi gorulmelidir.')
            # ''' 3. EPG'ye giriniz. (mheg_epg) '''
            api.sendKeys(['mheg_epg+3'])
            api.grabImage('BbcOne_EPG_NoSubtitle', delay=5, count=3, nView=3, msg='EPG ye girmelidir, subtitle EPG uzerine dokulmemelidir.')
            # ''' 4. EPG'den cikiniz. '''
            api.sendKeys(['mheg_epg+10', 'info+0.5'])
            # ''' 5. Mevcut kanala geri donmelidir, ses ve goruntude problem olmamalidir, Subtitle acik olmamalidir ve ekranda gorulmelidir. '''
            api.testImages('_BbcOne-ref', mask=api.infoBarMask, msg='Mevcut kanala geri donmelidir')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.grabImage('BbcOne_SubtitleOn', delay=5, count=3, nView=3, msg='Subtitle acik olmali ve ekranda gorulmelidir.')
            # ''' 6. Subtitle kapat '''
            api.sendKeys(['subtitles+3'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_03')
    api.setTestCaseDescription('EPG - Enter/Exit - Teletext to EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-S2 Arte HD) kanalini aciniz. '''
            api.sendKeys(['817+7'])
            # ''' 2. Teletext aciniz. (text) '''
            api.sendKeys(['text+3'])
            api.testImages('Arte_Teletext-ref', msg='Arte kanalinda teletext acildigi gorulmelidir.')
            # ''' 3. EPG'ye giriniz. (mheg_epg) '''
            api.sendKeys(['mheg_epg+3'])
            api.testImages('Arte_Teletext1-ref', msg='Teletext sayfasi gorulmelidir, EPG acilmamalidir.')
            # ''' 4. Teletext'ten cikiniz. '''
            api.sendKeys(['text+1*2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_04')
    api.setTestCaseDescription('EPG - Enter/Exit - Record to EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-T CH54 Channel 4) kanalini aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Record baslatiniz. (record) '''
            api.sendKeys(['record+7', 'ok+5', 'info+1'])
            api.testImages('BbcOne_Record-ref', mask=api.infoBarMask, msg='Channel 4 kanalinda record yapildigi gorulmelidir.')
            # ''' 3. EPG'ye girmeye calisiniz. (mheg_epg) '''
            api.sendKeys(['mheg_epg+3'])
            api.testImages('BbcOne_EPG-ref', mask=api.EPGChannelNameMask, msg='EPG ye girebilmelidir.')
            # ''' 4. EPG'den cikiniz. Kaydi durdurun. '''
            api.sendKeys(['exit2+2 ', 'stop+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_05')
    api.setTestCaseDescription('EPG - Enter/Exit - Timeshift to EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-T CH54 Channel 4) kanalini aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Record baslatiniz. (record) '''
            api.sendKeys(['stop+5', 'pause+15', 'info+1'])
            api.testImages('BbcOne_Timeshift-ref', mask=api.timeshiftInfoBar, msg='Channel 4 kanalinda timeshift yapildigi gorulmelidir.')
            # ''' 3. EPG'ye girmeye calisiniz. (mheg_epg) '''
            api.sendKeys(['info+1', 'mheg_epg+0.5'])
            api.testImages('BbcOne_NoEPGBecauseTimeshift-ref', mask=api.timeshiftNotAvailable, msg='EPG ye girememelidir.')
            # ''' 4. Timeshift durdurun. '''
            api.sendKeys(['exit2+2*2', 'stop+6'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_06')
    api.setTestCaseDescription('EPG - Enter/Exit - Fluke to EPG')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Source listesini aciniz. '''
            # ''' 2. FLUKE'un bagli oldugu SCART source'u seciniz '''
            # ''' 3. RGB set ediniz '''
            # ''' 4. EPG acmak icin kumandadan EPG tusuna basiniz. '''
            # ''' 5. EPG acilmalidir. '''
            # ''' 6. EPG'den cikiniz. '''
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_07')
    api.setTestCaseDescription('EPG - Enter/Exit - Astro to EPG')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Source listesini aciniz. '''
            # ''' 2. ASTRO cihazinin bagli oldugu HDMI source'u seciniz '''
            # ''' 3. 1080p cozunurluk veriniz '''
            # ''' 4. EPG acmak icin kumandadan EPG tusuna basiniz. '''
            # ''' 5. EPG acilmalidir. '''
            # ''' 6. EPG'den cikiniz. '''
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_08')
    api.setTestCaseDescription('EPG - Enter/Exit - Wait HBBTV Red icon for EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-S2 Das Erste HD) kanalini aciniz. Red icon'u bekleyiniz, red icon ekranda goruldugunde '''
            api.sendKeys(['816+7'])
            # ''' 2. EPG'ye giriniz. (mheg_epg) '''
            api.sendKeys(['mheg_epg+3'])
            api.testImages('DasErsteHD_EPG-ref', mask=api.EPGChannelNameMask, msg='EPG ye girmelidir.')
            # ''' 3. EPG'den cikiniz. '''
            api.sendKeys(['exit2+2*2+10', 'info+0.5'])
            # ''' 4. Mevcut kanala geri donmelidir, ses ve goruntude problem olmamalidir. '''
            api.testImages('_DasErsteHd-ref', mask=api.infoBarMask, msg='Das Erste HD kanalina geri donmelidir.')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_09')
    api.setTestCaseDescription('EPG - Enter/Exit - HBBTV to EPG')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. (DVB-S2 Das Erste HD) kanalini aciniz. '''
            api.sendKeys(['816+10'])
            # ''' 2. HBBTV aciniz '''
            api.sendKeys(['red+3'])
            api.testImages('DasErsteHD_HBBTV-ref', msg='HBBTV acilmalidir.')
            # ''' 2. EPG'ye giriniz. (mheg_epg) '''
            api.sendKeys(['mheg_epg+3'])
            api.testImages('DasErsteHD_EPG-ref', mask=api.EPGChannelNameMask, msg='EPG ye girmelidir.')
            # ''' 3. EPG'den cikiniz. '''
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_10')
    api.setTestCaseDescription('EPG - Enter/Exit - Astro to EPG')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Source listesini aciniz. '''
            # ''' 2. ASTRO cihazinin bagli oldugu HDMI source'u seciniz '''
            # ''' 3. 1080p cozunurluk veriniz '''
            # ''' 4. EPG acmak icin kumandadan EPG tusuna basiniz. '''
            # ''' 5. EPG acilmalidir. '''
            # ''' 6. EPG'den cikiniz. '''
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_11')
    api.setTestCaseDescription('EPG - Enter/Exit - Portal to EPG')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_12')
    api.setTestCaseDescription('EPG - Enter/Exit - Analog Channel EPG')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. Source listesini aciniz. '''
            # ''' 2. FLUKE'un bagli oldugu SCART source'u seciniz '''
            # ''' 3. RGB set ediniz '''
            # ''' 4. EPG acmak icin kumandadan EPG tusuna basiniz. '''
            # ''' 5. EPG acilmalidir. '''
            # ''' 6. EPG'den cikiniz. '''
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_13')
    api.setTestCaseDescription('EPG - Enter/Exit - Unplug RF Cable')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            api.sendKeys(['5+10'])
            # ''' 1. RF kablosunu cekiniz ve TV'nin No Signal durumunda oldugundan emin olunuz. No signal durumunda 1 dk bekleyiniz. '''
            api.sendKeys(['RFSIGNALOFF', 'exit2+2*2'])
            api.testImages('_noSignal-ref', msg='TV, No Signal durumunda olmalidir.')
            # ''' 2. EPG'ye giriniz. (mheg_epg) '''
            api.sendKeys(['exit2+2*2+60', 'mheg_epg+5'])
            api.testImages('_noSignal-ref', msg='EPG ye girmemelidir. Tv, No Signal durumunda olmalidir.')
            # ''' 3. RF kablosunu tak. '''
            api.sendKeys(['exit2+2*2', 'RFSIGNALON', 'progup+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC01_14')
    api.setTestCaseDescription('EPG - Enter/Exit - Only Analog Channel')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' 1. FTI yapip tum kanallari siliniz, manual search ile sadece analog kanal C12'ye tune olunuz. '''
            # ''' 2. EPG'ye giriniz. (mheg_epg) '''
            # ''' 3. Kanal listesinde sadece analog kanal varken EPG'ye girmemelidir. '''
        except:
            api.printError()
        api.end(False)

def EPG_TC02(api):
    global ftiCompleted
    ftiCompleted = 1

    api.setTestCaseName('EPG_TC02_01')
    api.setTestCaseDescription('EPG Type - Now-Next - Right/Left Operations')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle.(mheg_epg) '''
            # ''' 3. Now-Next gorunumunu sec (red) '''
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 4. Mevcut kanalda Current Event/Next Event arasinda sag/navigasyon yap. '''
            controlImage = []
            api.testImages('Mheg_CurrentEvent-ref', limit=80, msg='Current Event secili olmalidir.')
            api.sendKeys(['right+1'])
            api.testImages('Mheg_NextEvent-ref', limit=80, msg='Next Event secili olmalidir.')
            api.sendKeys(['left+1'])
            api.testImages('Mheg_CurrentEvent-ref', limit=80, msg='Current Event secili olmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_02')
    api.setTestCaseDescription('EPG Type - Now-Next - Down/Up Operations')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle.(mheg_epg) '''
            # ''' 3. Now-Next gorunumunu sec (red) '''
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 4. Mevcut kanaldan 15 kanal asagiya in ve daha sonra 5 kanal yukariya cik. '''
            api.testImages('Mheg_1-ref', limit=80, msg='Dogrudan secili olan kanal EPG de gorulmelidir.')
            api.sendKeys(['down+1*15'])
            api.testImages('Mheg_2-ref', limit=80, msg='Mevcut kanaldan 15 kanal asagi inilmelidir.')
            api.sendKeys(['up+1*5'])
            api.testImages('Mheg_3-ref', limit=80, msg='5 kanal yukari cikilmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_03')
    api.setTestCaseDescription('EPG Type - Now-Next - Now-Next to List Schedule')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle.(mheg_epg) '''
            # ''' 3. Now-Next gorunumunu sec (red) '''
            api.sendKeys(['mheg_epg+3', 'red+10'])
            api.testImages('Mheg_NowNext-ref', limit=80, msg='Now-Next gorunumu gorulmelidir.')
            # ''' 4. List Schedule gorunumunu sec (green) '''
            api.sendKeys(['green+10'])
            api.testImages('Mheg_ListSchedule-ref', limit=80, msg='List Schedule gorunumu gorulmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_04')
    api.setTestCaseDescription('EPG Type - Now-Next - Now-Next to Timeline Schedule')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle. (mheg_epg) '''
            # ''' 3. Now-Next gorunumunu sec (red) '''
            api.sendKeys(['mheg_epg+3', 'red+10'])
            api.testImages('Mheg_NowNext-ref', limit=80, msg='Now-Next gorunumu gorulmelidir.')
            # ''' 4. Timeline Schedule gorunumunu sec '''
            api.sendKeys(['yellow+10'])
            api.testImages('Mheg_Timeline-ref', limit=65, msg='Timeline gorunumu gorulmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_05')
    api.setTestCaseDescription('EPG Type - Now-Next - Event Details')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle. (mheg_epg) '''
            # ''' 3. Now-Next gorunumunu sec (red) '''
            # ''' 4. Event Detais ac. (info) '''
            api.sendKeys(['mheg_epg+3', 'red+10', 'info+3'])
            api.testImages('EventDetails-ref', limit=80, msg='Ekranin yukarisinda program ile ilgili detaylar acilmali.')
            api.sendKeys(['info+3'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_06')
    api.setTestCaseDescription('EPG Type - Now-Next - Close Event Details')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle.(mheg_epg) '''
            # ''' 3. Now-Next gorunumunu sec (red) '''
            # ''' 4. Event Detais ac/kapa. (info) '''
            api.sendKeys(['mheg_epg+3', 'red+10', 'info+3*2'])
            api.testImages('NowNext-ref', limit=80, msg='Event Detaylari yukarida acilan kisimdan kaybolmali, Now And Next EPG gorunumune donmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_07')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Radio Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Radio only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', tvRadio='Radio Only')
            # ''' 4. EPG'de sadece Radio kanallari gorunmelidir. '''
            api.testImages(['EPG_RadioOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_08')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Text Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Text only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', tvRadio='Text Only')
            # ''' 4. EPG'de text kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TextOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de text kanallari varsa sadece onlar gorunmelidir, yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_09')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / TV Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. TV only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', tvRadio='TV Only')
            # ''' 4. EPG'de TV kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TVOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de text kanallari varsa sadece onlar gorunmelidir, yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_10')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / All')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Tekrar Filter'i ac ve 'All' sec, 'exit' e atanmis tus ile EPG'ye geri don. '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', tvRadio='All')
            # ''' 4. Tum digital kanallar EPG listesinde gorunur olmalidir, (TV -Radio ve varsa Text) '''
            api.testImages(['EPG_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Tum digital kanallar EPG listesinde gorunur olmalidir, (TV -Radio ve varsa Text)')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_11')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Encrypted')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Encrypted sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', freeCas='Encrypted')
            # ''' 4. EPG'ye geri donmelidir, ve listede sadece Encrypted kanallar bulunmalidir. '''
            api.testImages(['EPG_Encrypted-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de Encrypted kanallari varsa sadece onlar gorunmelidir, yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_12')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Free')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Free sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', freeCas='Free')
            # ''' 4. EPG'ye geri donmelidir, ve listede sadece Free kanallar bulunmalidir. '''
            api.testImages(['EPG_Free-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece Free kanallar bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_13')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / All')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Free sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', freeCas='All')
            # ''' 4. EPG'ye geri donmelidir, ve listede sadece Encrypted kanallar bulunmalidir. '''
            api.testImages(['EPG_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir ve hem Free hem de Encrypted kanallar listede bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_14')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Numeric')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Numeric siralamayi seciniz ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz. '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', sort='Numeric')
            # ''' 4. EPG'ye geri donmelidir, ve listedeki kanallar numerik siralanmis olmalidir. '''
            api.testImages(['EPG_Numeric-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listedeki kanallar numerik siralanmis olmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_15')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Alphabetic')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Alphabetic siralamayi seciniz, ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz. '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', sort='Alphabetic')
            # ''' 4. EPG'ye geri donmelidir, ve listede sadece Encrypted kanallar bulunmalidir. '''
            api.testImages(['EPG_Alphabetic-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir ve hem Free hem de Encrypted kanallar listede bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_16')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / SD')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. SD seciniz ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', hdsd='Sd')
            # ''' 4. EPG'ye geri donmelidir, ve listede sadece SD kanallar bulunmalidir. '''
            api.testImages(['EPG_SD-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece SD kanallar bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_17')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / HD')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. HD seciniz ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', hdsd='Hd')
            # ''' 4. EPG'ye geri donmelidir, ve listede sadece HD kanallar bulunmalidir. '''
            api.testImages(['EPG_HD-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece HD kanallar bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_18')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / HD/SD (All)')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. Tekrar Filter'i aciniz ve 'All' a atanmis tusa basiniz, EPG'ye geri donmek icin ise 'Exit'e atanmis tusa basiniz. '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', hdsd='All')
            # ''' 4. EPG'ye geri donmelidir, ve listede tum kanallar hd ve sd bulunmalidir. '''
            api.testImages(['EPG_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede tum kanallar hd ve sd bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_19')
    api.setTestCaseDescription('EPG Type - Now-Next - Filter / Z')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. Filter'i aciniz. '''
            # ''' 3. A-Z filtresinden 'A' harfini seciniz ve EPG listesine geri donunuz '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='NowNext', az='Z')
            # ''' 4. B harfi ile baslayan kanallar siralanmis olmalidir. '''
            api.testImages(['EPG_AZ_Z-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='B harfi ile baslayan kanallar siralanmis olmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_20')
    api.setTestCaseDescription('EPG Type - Now-Next - Timer / Timer Conflict')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 2. 3 kanal asagiya inin, Next Event'a gelin. '''
            api.sendKeys(['down+1*3', 'right+1'])
            api.testImages('EPG_NextEvent-ref', msg='EPG de Next Event secili olmalidir.')
            # ''' 3. Next Event'e timer kurun, timers menuden kurulan timer'in olup olmadigini kontrol edin. '''
            api.sendKeys(['ok+1', 'up+1', 'ok+1'])
            api.testImages('EPG_NextEvent_SetTimer-ref', msg='EPG de Next Event icin timer kuruldugu gorulmelidir.')
            api.sendKeys(api.TIMERS)
            api.testImages('TimerMenu_Timers-ref', mask=api.TimerMask, msg='Timer Menu de timer kuruldugu gorulmelidir.')
            # ''' 4. Daha once timer kurdugunuz zaman diliminde next event bilgisi olan bir baska kanalin next event'ine timer ekleyiniz. '''
            api.sendKeys(['exit2+2*2', 'mheg_epg+3', 'red+10', 'down+1*2', 'right+1'])
            api.sendKeys(['ok+1', 'up+1', 'ok+1'])
            # ''' 5. Cakisma oldugunu gosteren sayfa acilmalidir. '''
            api.testImages('EPG_TimerConflict-ref', msg='Cakisma oldugunu gosteren sayfa acilmalidir.')
            # ''' 6. Kurulan timeri sil. '''
            # api.sendKeys(['ok+1', 'down+1', 'ok+1', 'up+1', 'ok+1'])
            api.sendKeys(['red+1', 'down+1', 'red+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_21')
    api.setTestCaseDescription('EPG Type - Now-Next - Record Next Event')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3', 'red+10'])
            # ''' 3. Mevcut kanalda Next Event'e record kurun '''
            api.sendKeys(['right+1', 'ok+1', 'down+1', 'ok+10'])
            # ''' 4. Record kurulan event EPG listesinde isaretlenmeli, zamani geldiginde record kurulan yayina gidip kayda baslamali. '''
            api.testImages('EPG_RecordNextEvent-ref', limit=90, msg='Record kurulan event EPG listesinde isaretlenmeli, zamani geldiginde record kurulan yayina gidip kayda baslamali.')
            # ''' 5. Record kaydini sil. '''
            api.sendKeys(['ok+1', 'down+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_22')
    api.setTestCaseDescription('EPG Type - Now-Next - Select Channel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle, '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. 3 kanal asagiya inin, Next Event'a gelin. '''
            # ''' 4. Options'tan 'select channel' secin. '''
            api.sendKeys(['down+1*3', 'right+1', 'ok+1*2', 'exit+10', 'info+0.5'])
            # ''' 4. Numarasi yazilan kanali EPG'de listede gostermeli. Kanala ait event bilgileri gorunmelidir. '''
            api.testImages('_ZdfNeo-ref', mask=api.infoBarMask, msg='Secilen kanala gitmeli')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_23')
    api.setTestCaseDescription('EPG Type - Now-Next - Record Current Event')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Now-Next gorunumune geri don. '''
            api.sendKeys(['mheg_epg+3', 'red+3'])
            # ''' 3. Mevcut kanalda Current Event'e record kurun '''
            api.sendKeys(['ok+1', 'up+1', 'ok*3+10', 'info+0.8'])
            # ''' 4. Record kurulan yayina gitmeli, record baslamali. '''
            api.testImages('Zdf_Record-ref', mask=api.infoBarMask, limit=95, msg='Record kurulan yayina gitmeli, record baslamali.')
            # ''' 5. Delete record '''
            api.sendKeys( api.TIMERS + ['down+1', 'ok+1', 'red+1', 'ok+1'])
            # ''' *** Bu bolum onemli. Eger record isleminde record yapilan kanala gidilmezse kanal info yerine, epg info aciliyor. Bu yuzden diger caseler yanlis gidiyor. Bu bolum bunu kontrol edip duzeltir. '''
            api.sendKeys(['exit2+2*2', 'mheg_epg+3'])
            if api.testImages('EPGInfoOpen-ref', recordResults=False, limit=50)[0]:
                api.sendKeys(['info+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC02_24')
    api.setTestCaseDescription('EPG Type - Now-Next - Exit EPG with Return or Back')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar List Schedule gorunumune geri don. '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. EPG'den Return ya da Back kumanda komutlari ile cik. '''
            api.sendKeys(['back+10', 'info+0.5'])
            # ''' 4. Mevcut kanala geri donmeli, kanalda goruntu ve ses kontrol edilmeli, bir problem olmamali. '''
            api.testImages('_ZdfNeo-ref', mask=api.infoBarMask, limit=95, msg='Secilen kanala gitmeli')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(8, 0, 8), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def EPG_TC03(api):
    global ftiCompleted
    ftiCompleted = 1

    api.setTestCaseName('EPG_TC03_01')
    api.setTestCaseDescription('EPG Type - List - 3 Days Later')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            # ''' 3. List Schedule gorunumunu sec. (green) '''
            # ''' 4. Mevcut kanalda 3 gün ilerisine git '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'progup+1*3'])
            api.testImages('EPG_3DaysLater-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 3 gun sonraki program bilgileri gorunur olmali.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_02')
    api.setTestCaseDescription('EPG Type - List - 1 Day Before')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. 1 onceki gune git (progdown) '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'progdown+1'])
            # ''' 3. Event bilgileri degisikligi olmali. Geri gidilen gune ait program bilgileri gorunur olmali. '''
            api.testImages('EPG_1DaysBefore-ref', msg='Event bilgileri degisikligi olmali. Geri gidilen gune ait program bilgileri gorunur olmali.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_03')
    api.setTestCaseDescription('EPG Type - List - Event Details')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Event Details'i acin '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'right+1', 'down+1', 'info+1'])
            # ''' 3. Ekranin yukarisinda program ile ilgili detayla acilmali. '''
            api.testImages('EPG_EventDetails-ref', msg='Ekranin yukarisinda program ile ilgili detayla acilmali.')
            api.sendKeys(['info+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_04')
    api.setTestCaseDescription('EPG Type - List - Event Details More')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. More Event Info icin Program Up ve Program Down tusunu kullanin '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'right+1', 'down+1', 'info+1', 'progdown+1*2'])
            api.testImages('EPG_EventDetails_Down-ref', msg='More Event Info icin Program Up ve Program Down tusunu kullanin')
            api.sendKeys(['progup+1'])
            api.testImages('EPG_EventDetails_Up-ref', msg='More Event Info icin Program Up ve Program Down tusunu kullanin')
            # ''' 3. Event Details'i kapatin '''
            # ''' 4. Event Detaylari yukarida acilan kisimdan kaybolmali, List Schedule EPG gorunumune donmeli. '''
            api.sendKeys(['info+1'])
            api.testImages('EPG_EventDetails-ref', msg='Event Detaylari yukarida acilan kisimdan kaybolmali, List Schedule EPG gorunumune donmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_05')
    api.setTestCaseDescription('EPG Type - List - Timer')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. 3 kanal asagiya inin, Next Event'a gelin. '''
            # ''' 3. Next Event'e timer kurun, timers menuden kurulan timer'in olup olmadigini kontrol edin. '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'down+1*3', 'right+1', 'down+1*2', 'ok+1', 'up+1', 'ok+1'])
            # ''' 4. Timer kurulmali, timer kurulan event EPG'de belli olmali, timers menuden gorunmeli, zamani geldiginde kayda baslamali. '''
            api.testImages('EPG_SetTimer-ref', msg='Timer kurulmali, timer kurulan event EPG de belli olmali.')
            api.sendKeys(api.TIMERS)
            api.testImages('EPG_TimerMenu-ref', mask=api.TimerMask, msg='Timer kurulmali, timers menuden gorunmeli, zamani geldiginde kayda baslamali.')
            api.sendKeys(['down+1', 'red+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_06')
    api.setTestCaseDescription('EPG Type - List - Timer Conflict')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Daha once timer kurdugunuz zaman diliminde next event bilgisi olan bir baska kanalin next event'ine timer ekleyiniz. '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'right+1', 'ok+1', 'up+1', 'ok+1', 'exit2+3'])
            # ''' 3. Cakisma oldugunu gosteren sayfa acilmalidir. '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'down+1', 'right+1', 'ok+1', 'up+1', 'ok+1'])
            api.testImages('EPG_NoMoreTimer-ref', msg='Cakisma oldugunu gosteren sayfa acilmalidir.')
            # ''' 4. Timeri kaldir. '''
            api.sendKeys( ['ok+1'] + api.TIMERS + ['down+1', 'red+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_07')
    api.setTestCaseDescription('EPG Type - List - Record Next Event')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Mevcut kanalda Next Event'e record kurun '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'right+1', 'down+1*2', 'ok+1', 'up+1', 'ok+1'])
            # ''' 3. Record kurulan event EPG listesinde isaretlenmeli, zamani geldiginde record kurulan yayina gidip kayda baslamali. '''
            api.testImages('EPG_Record-ref', msg='Record kurulan event EPG listesinde isaretlenmeli.')
            api.sendKeys(api.TIMERS + ['down+1'])
            forceBreak = 0
            while True:
                forceBreak += 1
                if api.testImages('EPG_RecordStart-ref', recordResults=False, msg='Zamani geldiginde record kurulan yayina gidip kayda baslamali.')[0]:
                    api.updateTestResult('PASS')
                    break
                elif forceBreak == 10:
                    api.updateTestResult('FAIL')
                    break
                else:
                    api.sendKeys(['+5'])
            api.sendKeys(api.TIMERS + ['down+1', 'red+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_08')
    api.setTestCaseDescription('EPG Type - List - Select Channel Option')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Kaydi durdurun ve tekrar EPG'yi acin. '''
            # ''' 3. 3 kanal asagiya inin, Next Event'a gelin. '''
            # ''' 4. Options'tan 'select channel' secin. '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'down+1*3', 'right+1', 'down+1*2', 'ok+1*2', '+10', 'info+0.5'])
            # ''' 5. Secilen kanala gitmeli, kanalda ses ve goruntu olmali. '''
            api.testImages('_ZdfNeo-ref', mask=api.infoBarMask, msg='Secilen kanala gitmelidir.')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_09')
    api.setTestCaseDescription('EPG Type - List - Filter / Radio Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Filter'i aciniz. '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Radio only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='List', tvRadio='Radio Only')
            # ''' 3. EPG'de sadece Radio kanallari gorunmelidir. Radio kanali yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_RadioOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_10')
    api.setTestCaseDescription('EPG Type - List - Filter / Text Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Text only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='List', tvRadio='Text Only')
            # ''' 4. EPG'de text kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TextOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_11')
    api.setTestCaseDescription('EPG Type - List - Filter / TV Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Text only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='List', tvRadio='Tv Only')
            # ''' 4. EPG'de tv kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TvOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_12')
    api.setTestCaseDescription('EPG Type - List - Filter / All')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Text only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='List', tvRadio='All')
            # ''' 4. EPG'de tv kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_13')
    api.setTestCaseDescription('EPG Type - List - Filter / Encrypted')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Encrypted sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='Digital Cable Only', fromView='List', freeCas='Encrypted')
            # ''' 4. EPG'de Encrypted kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_Encrypted-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_14')
    api.setTestCaseDescription('EPG Type - List - Filter / Free')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Free sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', freeCas='Free')
            # ''' 4. EPG'de Free kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_Free-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_15')
    api.setTestCaseDescription('EPG Type - List - Filter / All')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Free sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', freeCas='All')
            # ''' 4. EPG'de Free kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_16')
    api.setTestCaseDescription('EPG Type - List - Filter / Numeric')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Filter Numeric sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', sort='Numeric')
            # ''' 4. EPG'de Free kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_Numeric-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_17')
    api.setTestCaseDescription('EPG Type - List - Filter / Alphabetic')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Filter Alphabetic sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', sort='Alphabetic')
            # ''' 4. EPG'de Alphabetic kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_Alphabetic-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_18')
    api.setTestCaseDescription('EPG Type - List - Filter / SD')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Filter SD sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', hdsd='SD')
            # ''' 4. EPG'de Alphabetic kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_SD-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_19')
    api.setTestCaseDescription('EPG Type - List - Filter / HD')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Filter HD sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', hdsd='HD')
            # ''' 4. EPG'de HD kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_HD-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_20')
    api.setTestCaseDescription('EPG Type - List - Filter / Z')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Filter Z sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='List', az='Z')
            # ''' 4. EPG'de Z kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_AZ_Z-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_21')
    api.setTestCaseDescription('EPG Type - List - Select Channel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Filter'i aciniz '''
            # ''' 3. EPG'de event bilgileri gormek istediginiz kanalin numarasini kumanda uzerindeki digit tuslarini kullanarak giriniz. '''
            api.sendKeys(['mheg_epg+3', 'green+3', '9+3'])
            # ''' 4. Numarasi yazilan kanali EPG'de listede gostermeli. Kanala ait event bilgileri gorunmelidir. '''
            api.testImages('EPG_Channel9-ref', msg='9 numarali kanali EPG de listede gostermeli. Kanala ait event bilgileri gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_22')
    api.setTestCaseDescription('EPG Type - List - Changing Navigation')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Mevcut kanaldan 6 kanal asagiya in ve daha sonra 5 kanal yukariya cik. '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'down+1*6', 'up+1*5'])
            # ''' 3. Asagi iniste sayfa degisikligi olmali, degisen sayfadaki kanallara ait event'ler gorunmeli. Navigasyon yapilabilmeli. '''
            api.testImages('EPG_Navigation-ref', msg='Asagi iniste sayfa degisikligi olmali, degisen sayfadaki kanallara ait event ler gorunmeli. Navigasyon yapilabilmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_23')
    api.setTestCaseDescription('EPG Type - List - Next Time Slice')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Mevcut kanalda 3 zaman dilimi ilerisine git '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'green+1'])
            # ''' 3. Event bilgileri degisikligi olmali. Kanala ait 3 zaman dilimi sonrasinin program bilgileri gorunur olmali. '''
            api.testImages('EPG_ListSch_NextTimeSlice1-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 1 zaman dilimi sonrasinin program bilgileri gorunur olmali.')
            api.sendKeys(['green+1'])
            api.testImages('EPG_ListSch_NextTimeSlice2-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 2 zaman dilimi sonrasinin program bilgileri gorunur olmali.')
            api.sendKeys(['green+1'])
            api.testImages('EPG_ListSch_NextTimeSlice3-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 3 zaman dilimi sonrasinin program bilgileri gorunur olmali.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_24')
    api.setTestCaseDescription('EPG Type - List - Previous Time Slice')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Mevcut kanalda 3 zaman dilimi ilerisine git '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'green+1'])
            # ''' 3. Event bilgileri degisikligi olmali. Kanala ait 3 zaman dilimi sonrasinin program bilgileri gorunur olmali. '''
            api.testImages('EPG_ListSch_NextTimeSlice1-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 1 zaman dilimi sonrasinin program bilgileri gorunur olmali.')
            api.sendKeys(['green+1'])
            api.testImages('EPG_ListSch_NextTimeSlice2-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 2 zaman dilimi sonrasinin program bilgileri gorunur olmali.')
            api.sendKeys(['red+1'])
            api.testImages('EPG_ListSch_PreviousTimeSlice1-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 1 zaman dilimi sonrasinin program bilgileri gorunur olmali.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_25')
    api.setTestCaseDescription('EPG Type - List - List to Now-Next Schedule')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Now-Next gorunumunu sec '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'blue+3'])
            # ''' 3. Now-Next gorunumune gecmeli, List Schedule gorunumunde event'leri gorunen kanallarin event bilgileri Now-Next gorunumunde de gorulmeli. '''
            api.testImages('EPG_TimetoNowNext-ref', msg='Now-Next gorunumune gecmeli, List Schedule gorunumunde event leri gorunen kanallarin event bilgileri Now-Next gorunumunde de gorulmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_26')
    api.setTestCaseDescription('EPG Type - List - Record Current Event')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar List Schedule gorunumune geri don. '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. Mevcut kanalda Current Event'e record kurun '''
            api.sendKeys(['right+1', 'down+1', 'ok+1', 'up+1', 'ok*3+10', 'info+0.8'])
            # ''' 4. Record kurulan yayina gitmeli, record baslamali. '''
            api.testImages('EPG_GoChannel-ref', mask=api.infoBarMask, msg='Record kurulan yayina gitmeli, record baslamali.')
            # ''' 5. Delete record '''
            api.sendKeys( api.TIMERS + ['down+1', 'ok+1', 'red+1', 'ok+1'])
            # ''' *** Bu bolum onemli. Eger record isleminde record yapilan kanala gidilmezse kanal info yerine, epg info aciliyor. Bu yuzden diger caseler yanlis gidiyor. Bu bolum bunu kontrol edip duzeltir. '''
            api.sendKeys(['exit+1*2', 'mheg_epg+3'])
            if api.testImages('EPGInfoOpen-ref', recordResults=False, limit=50)[0]:
                api.sendKeys(['info+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_27')
    api.setTestCaseDescription('EPG Type - List - List to Now-Next Schedule')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Timeline Schedule gorunumunu sec '''
            api.sendKeys(['mheg_epg+3', 'green+3', 'yellow+3'])
            # ''' 3. Timeline gorunumune gecmeli, List Schedule gorunumunde event'leri gorunen kanallarin event bilgileri Timeline gorunumunde de gorulmeli. '''
            api.testImages('EPG_ListtoTimeLine-ref', limit=70, msg='Timeline gorunumune gecmeli, List Schedule gorunumunde event leri gorunen kanallarin event bilgileri Timeline gorunumunde de gorulmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC03_28')
    api.setTestCaseDescription('EPG Type - List - Exit EPG with Return or Back')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar List Schedule gorunumune geri don. '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. EPG'den Return ya da Back kumanda komutlari ile cik. '''
            api.sendKeys(['back+10', 'info+0.5'])
            # ''' 4. Mevcut kanala geri donmeli, kanalda goruntu ve ses kontrol edilmeli, bir problem olmamali. '''
            api.testImages('EPG_GoChannel-ref', mask=api.infoBarMask, msg='Mevcut kanala geri donmeli, kanalda goruntu ve ses kontrol edilmeli, bir problem olmamali.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def EPG_TC04(api):
    global ftiCompleted
    ftiCompleted = 1

    api.setTestCaseName('EPG_TC04_01')
    api.setTestCaseDescription('EPG Type - Timeline - 3 Days Later')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            # ''' 3. Mevcut kanalda 3 gun ilerisine git. '''
            api.sendKeys(['mheg_epg+3', 'progup+1*3'])
            # ''' 4. Event bilgileri degisikligi olmali. Kanala ait 3 gun sonraki program bilgileri gorunur olmali. '''
            api.testImages('EPG_3DaysLater-ref', msg='Event bilgileri degisikligi olmali. Kanala ait 3 gun sonraki program bilgileri gorunur olmali.')
            # ''' 5. 3 gun ilerisinde iken 1 onceki gune git '''
            api.sendKeys(['progdown+1'])
            # ''' 6. Event bilgileri degisikligi olmali. Geri gidilen gune ait program bilgileri gorunur olmali. '''
            api.testImages('EPG_1DayBefore-ref', msg='Event bilgileri degisikligi olmali. Geri gidilen gune ait program bilgileri gorunur olmali.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_02')
    api.setTestCaseDescription('EPG Type - Timeline - Event Details')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle ''' 
            # ''' 3. Event Details'i acin '''
            api.sendKeys(['mheg_epg+3', 'info+1'])
            # ''' 4. Ekranin yukarisinda program ile ilgili detayla acilmali. '''
            api.testImages('EPG_TimelineSchedule_EventDetails-ref', msg='Ekranin yukarisinda program ile ilgili detayla acilmali.')
            api.sendKeys(['info+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_03')
    api.setTestCaseDescription('EPG Type - Timeline - Event Details More')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+5', 'info+3'])
            # ''' 3. More Event Info icin Program Down ve Program Up tusunu kullanin '''
            api.sendKeys(['progdown+2'])
            api.testImages('EPG_EventDetailsMore_Down-ref', msg='More Event Info icin Program down tusunu kullanin')
            api.sendKeys(['progup+2'])
            api.testImages('EPG_EventDetailsMore_Up-ref', msg='More Event Info icin Program up tusunu kullanin')
            # ''' 4. Event Details'i kapatin '''
            api.sendKeys(['info+3'])
            # ''' 5. Event Detaylari yukarida acilan kisimdan kaybolmali, Timeline Schedule EPG gorunumune donmeli. '''
            api.testImages('EPG_TimelineSchedule-ref', limit=75, msg='Event Detaylari yukarida acilan kisimdan kaybolmali, Timeline Schedule EPG gorunumune donmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_04')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Radio Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle ''' 
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Filter'i aciniz.
            # ''' 4. Radio only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', tvRadio='Radio Only')
            # ''' 5. EPG'de sadece Radio kanallari gorunmelidir. Uygun kanal yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TimelineSchedule_RadioOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de sadece Radio kanallari gorunmelidir. Uygun kanal yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_05')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Text Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz
            # ''' 4. Text only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', tvRadio='Text Only')
            # ''' 5. EPG'de text kanallari varsa sadece onlar gorunmelidir, yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TimelineSchedule_TextOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de text kanallari varsa sadece onlar gorunmelidir, yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_06')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / TV Only')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle ''' 
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz '''
            # ''' 4. TV only sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', tvRadio='TV Only')
            # ''' 5. EPG listesinde sadece TV kanallari gorunmelidir. '''
            api.testImages(['EPG_TimelineSchedule_TVOnly-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de tv kanallari varsa sadece onlar gorunmelidir, yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_07')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / All')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle ''' 
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i ac ve 'All' sec, 'exit'e atanmis tus ile EPG'ye geri don. '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', tvRadio='All')
            # ''' 4. Tum digital kanallar EPG listesinde gorunur olmalidir, (TV -Radio ve varsa Text) '''
            api.testImages(['EPG_TimelineSchedule_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG de butun kanallar gorunmelidir, yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_08')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Encrypted')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle ''' 
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Filter'i aciniz. '''
            # ''' 4. Encrypted sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', freeCas='Encrypted')
            # ''' 5. EPG'ye geri donmelidir, ve listede sadece Encrypted kanallar bulunmalidir. Uygun kanal yoksa 'no channels match filter' uyarisi gorunmelidir. '''
            api.testImages(['EPG_TimelineSchedule_Encyrpted-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece Encrypted kanallar bulunmalidir. Uygun kanal yoksa "no channels match filter" uyarisi gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_09')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Free')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz. '''
            # ''' 4. Free sec ve 'Exit' tusuna atanmis tus ile EPG listesine geri don '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', freeCas='Free')
            # ''' 5. EPG'ye geri donmelidir, ve listede sadece Free kanallar bulunmalidir. '''
            api.testImages(['EPG_TimelineSchedule_Free-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece Free kanallar bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_10')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / All')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz ve 'All' a atanmis tusa basiniz, EPG'ye geri donmek icin ise 'Exit'e atanmis tusa basiniz. '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', freeCas='All')
            # ''' 4. EPG'ye geri donmelidir ve hem Free hem de Encrypted kanallar listede bulunmalidir. '''
            api.testImages(['EPG_TimelineSchedule_All-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir ve hem Free hem de Encrypted kanallar listede bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_11')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Numeric')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Filter'i aciniz. '''
            # ''' 4. Numeric siralamayi seciniz ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz. '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', sort='Numeric')
            # ''' 5. EPG'ye geri donmelidir, ve listedeki kanallar numerik siralanmis olmalidir. '''
            api.testImages(['EPG_TimelineSchedule_SortNumeric-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listedeki kanallar numerik siralanmis olmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_12')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Alphabetic')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz. '''
            # ''' 4. Alphabetic siralamayi seciniz, ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz. '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', sort='Alphabetic')
            # ''' 5. EPG'ye geri donmelidir, ve listedeki kanallar numerik siralanmis olmalidir. '''
            api.testImages(['EPG_TimelineSchedule_SortAlphabetic-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listedeki kanallar numerik siralanmis olmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_13')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / SD')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Filter'i aciniz. '''
            # ''' 4. SD seciniz ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', hdsd='SD')
            # ''' 5. EPG'ye geri donmelidir, ve listede sadece SD kanallar bulunmalidir '''
            api.testImages(['EPG_TimelineSchedule_SD-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece SD kanallar bulunmalidir')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_14')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / HD')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz. '''
            # ''' 4. HD seciniz ve 'Exit' tusuna atanmis tus ile EPG listesine geri donunuz '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', hdsd='HD')
            # ''' 5. EPG'ye geri donmelidir, ve listede sadece HD kanallar bulunmalidir. '''
            api.testImages(['EPG_TimelineSchedule_HD-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='EPG ye geri donmelidir, ve listede sadece HD kanallar bulunmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_15')
    api.setTestCaseDescription('EPG Type - Timeline - Filter / Z')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Tekrar Filter'i aciniz ve 'All' a atanmis tusa basiniz, EPG'ye geri donmek icin ise 'Exit'e atanmis tusa basiniz. '''
            # ''' 4. Filter'i aciniz. '''
            # ''' 5. A-Z filtresinden 'Z' harfini seciniz ve EPG listesine geri donunuz '''
            api.setEPGFilter(api, networkType='digital cable only', fromView='Timeline', az='z')
            # ''' 6. Z harfi ile baslayan kanallar siralanmis olmalidir. '''
            api.testImages(['EPG_TimelineSchedule_Z-ref', '_epgNoChannelsMatchFilter-ref'], mask=api.EPGChannelListMask, limit=90, msg='Z harfi ile baslayan kanallar siralanmis olmalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_16')
    api.setTestCaseDescription('EPG Type - Timeline - Timer')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. 3 kanal asagiya inin, Next Event'a gelin. '''
            # ''' 4. Next Event'e timer kurun, timers menuden kurulan timer'in olup olmadigini kontrol edin. '''
            api.sendKeys(['down+1*3', 'right+1', 'ok+1', 'up+1', 'ok+1'])
            api.testImages('EPG_TimelineSchedule_EPGTimer-ref', limit=70, msg='Next Event e timer kurun, timers menuden kurulan timer in olup olmadigini kontrol edin.')
            # ''' 5. Timer kurulmali, timer kurulan event EPG'de belli olmali, timers menuden gorunmeli. '''
            api.sendKeys(api.TIMERS)
            api.testImages('EPG_TimelineSchedule_Timers-ref', mask=api.TimerMask, limit=70, msg='Next Event e timer kurun, timers menuden kurulan timer in olup olmadigini kontrol edin.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_17')
    api.setTestCaseDescription('EPG Type - Timeline - Timer Conflict')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            # ''' 3. Daha once timer kurdugunuz zaman diliminde next event bilgisi olan bir baska kanalin next event'ine timer ekleyiniz. '''
            api.sendKeys(['mheg_epg+3'])
            api.sendKeys(['down+1*2', 'right+1*3', 'ok+1', 'up+1', 'ok+1*2'])
            # ''' 4. Cakisma oldugunu gosteren sayfa acilmalidir. '''
            api.testImages('EPG_TimelineSchedule_TimerConflict-ref', limit=70, msg='Cakisma oldugunu gosteren sayfa acilmalidir.')
            api.sendKeys(['ok+1'] + api.TIMERS + ['down+1', 'red+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_18')
    api.setTestCaseDescription('EPG Type - Timeline - Record Next Event')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Mevcut kanalda Next Event'e record kurun '''
            api.sendKeys(['right+1', 'ok+1', 'down*2+1', 'ok+10'])
            # ''' 4. Record kurulan event EPG listesinde isaretlenmeli, zamani geldiginde record kurulan yayina gidip kayda baslamali. '''
            api.testImages('EPG_GuideSearch_RecordNextEvent-ref', limit=70, msg='Record kurulan event EPG listesinde isaretlenmeli, zamani geldiginde record kurulan yayina gidip kayda baslamali.')
            api.sendKeys(['ok+1', 'down+1', 'ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_19')
    api.setTestCaseDescription('EPG Type - Timeline - Select Channel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            # ''' 3. Kaydi durdurun ve tekrar EPG'yi acin. '''
            # ''' 4. 3 kanal asagiya inin, Next Event'a gelin. '''
            # ''' 5. Options'tan 'select channel' secin. '''
            api.sendKeys(['mheg_epg+3', 'down+1*3', 'right+1', 'ok+1*2', '+10', 'info+0.8'])
            # ''' 6. Secilen kanala gitmeli, kanalda ses ve goruntu olmali. '''
            api.testImages('_ZdfNeo-ref', mask=api.infoBarMask, msg='Secilen kanala gitmeli')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_20')
    api.setTestCaseDescription('EPG Type - Timeline - Select Channel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. EPG'de event bilgileri gormek istediginiz kanalin numarasini kumanda uzerindeki digit tuslarini kullanarak giriniz. '''
            api.sendKeys(['9+10'])
            # ''' 4. Numarasi yazilan kanali EPG'de listede gostermeli. Kanala ait event bilgileri gorunmelidir. '''
            api.testImages('EPG_Channel9-ref', msg='Numarasi yazilan kanali EPG de listede gostermeli. Kanala ait event bilgileri gorunmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_21')
    api.setTestCaseDescription('EPG Type - Timeline - Swap Now')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Sag yon tusu ile mevcut zaman diliminden 4 saat sonraya gidiniz '''
            api.sendKeys(['right+1*12'])
            api.testImages('EPG_TimelineSchedule_Next4Hour-ref', msg='Sag yon tusu ile mevcut zaman diliminden 4 saat sonraya gidiniz')
            # ''' 4. Simdiki zamana geri donmek icin atanmis tusa basiniz (SWAP-Now) '''
            api.sendKeys(['previous+1'])
            # ''' 5. Sistem saatinin oldugu zaman dilimine geri donmelidir. '''
            api.testImages('EPG_TimelineSchedule_SwapNow-ref', limit=70, msg='Sistem saatinin oldugu zaman dilimine geri donmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_22')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Saturday Contains L')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Search'e giriniz. '''
            # ''' 4. From-Until araligini Today-Saturday seciniz. '''
            # ''' 5. Search By'dan Name Match'i secip, Match on satirindan -L- harfini seciniz ve search' basiniz. '''
            api.sendKeys(['text+1', 'down+1*2', 'right+1*4', 'down+1', 'right+1', 'down+1', '5+1*4', 'down+1', 'ok+1'])
            # ''' 6. Icerisinde -L- harfi gecen tum programlar listelenmelidir. '''
            api.testImages('EPG_GuideSearch_TodaySaturdayContains_L-ref', msg='Icerisinde -L- harfi gecen tum programlar listelenmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_23')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Children')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Search By'dan Genre'yi secip, Match on'dan genre secimi(Children) yapiniz ve search'e basiniz. '''
            api.sendKeys(['text+1', 'up+1*2', 'ok+1', 'down+1*2'])
            api.testImages('EPG_GuideSearch_MatchOn_Children-ref', msg='Search By dan Genre yi secip, Match on dan genre secimi(Children) yapiniz ve search e basiniz.')
            api.sendKeys(['ok+1', 'down+1', 'ok+5'])
            # ''' 4. Secilen genre'ye(sports) uygun programlar listelenmelidir. '''
            api.testImages('EPG_GuideSearch_ResultChildren-ref', msg='Secilen genre ye (Children) uygun programlar listelenmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_24')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Saturday')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Bulundugunuz arayuzden search ekranina geri donunuz ve bir once yaptiginiz degisiklikleri default/ilk haline getiriniz. '''
            # ''' 4. From-Until araligini Today-Saturday seciniz. '''
            # ''' 5. Single channel seciniz ve channel'i da channel satirinda default gelen kanal birakiniz, search'e basiniz. '''
            api.sendKeys(['text+1', 'right+1', 'down+1*3', 'right+1*4', 'down+1*2', 'ok+1', 'down+1*2', 'ok+1', 'down+1', 'ok+5'])
            # ''' 6. Today-Saturday arasindaki tum TV kanallarini listelemelidir. '''
            api.testImages('EPG_GuideSearch_TodaySaturday-ref', msg='Today-Saturday arasindaki tum TV kanallarini listelemelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_25')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Saturday-AllChannel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. All channels seciniz ve search'e basiniz. '''
            api.sendKeys(['text+1', 'left+1*3', 'down+1*2', 'right+1*4', 'down+1*2', 'ok+1', 'down+1*2', 'ok+1', 'down+1', 'ok+5'])
            # ''' 4. Today-Saturday arasindaki tum kanallari ve programlari listelemelidir. '''
            api.testImages('EPG_GuideSearch_TodaySaturday_AllChannel-ref', msg='Today-Saturday arasindaki tum kanallari ve programlari listelemelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_26')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Saturday-AllTvChannel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. All TV channels seciniz ve search'e basiniz. '''
            api.sendKeys(['text+1', 'left+1*2', 'down+1*2', 'right+1*4', 'down+1*2', 'ok+1', 'down+1*2', 'ok+1', 'down+1', 'ok+5'])
            # ''' 4. Today-Saturday arasindaki tum TV kanallarini ve programlari listelemelidir. '''
            api.testImages('EPG_GuideSearch_TodaySaturday_AllTvChannel-ref', msg='Today-Saturday arasindaki tum TV kanallarini ve programlari listelemelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_27')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Saturday-AllRadioChannel')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle, '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. All radio channels seciniz ve search'e basiniz. '''
            api.sendKeys(['text+1', 'left+1', 'down+1*2', 'right+1*4', 'down+1*2', 'ok+1', 'down+1*2', 'ok+1', 'down+1', 'ok+5'])
            # ''' 4. Today-Saturday arasindaki tum Radio kanallarini ve programlari listelemelidir. '''
            api.testImages('EPG_GuideSearch_TodaySaturday_AllRadioChannel-ref', msg='Today-Saturday arasindaki tum Radio kanallarini ve programlari listelemelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_28')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Saturday-Current Channel List')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Current channel list seciniz ve search'e basiniz. '''
            api.sendKeys(['text+1', 'down+1*2', 'right+1*4', 'down+1*2', 'ok+1', 'down+1*2', 'ok+1', 'down+1', 'ok+5'])
            # ''' 4. Today-Saturday arasindaki mevcut kanal listesindeki kanallari listelemelidir. '''
            api.testImages('EPG_GuideSearch_TodaySaturday_CurrentChannelList-ref', msg='Today-Saturday arasindaki mevcut kanal listesindeki kanallari listelemelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_29')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Today-Tuesday-Current Channel List')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Bulundugunuz arayuzden search ekranina geri donunuz ve bir once yaptiginiz degisiklikleri default/ilk haline getiriniz. '''
            # ''' 4. Mevcut kanal listesi secili iken From-Until secimi icin, From'u today seciniz. '''
            # ''' 5. From-Until secimi icin, Until'iTuesday seciniz ve search yapiniz. '''
            api.sendKeys(['text+1', 'down+1*2', 'left+1', 'down+1*2', 'ok+1', 'down+1*2', 'ok+1', 'down+1', 'ok+5'])
            # ''' 4. Mevcut kanal listesindeki kanallarda Today-Tuesday arasi bulunan tum programlar listelenmelidir. '''
            api.testImages('EPG_GuideSearch_TodayTuesday_CurrentChannelList-ref', msg='Mevcut kanal listesindeki kanallarda Today-Tuesday arasi bulunan tum programlar listelenmelidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_30')
    api.setTestCaseDescription('EPG Type - Timeline - Guide Search / Tuesday-Sunday-WarningScreen')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. EPG ac ve kanal program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. Bulundugunuz arayuzden search ekranina geri donunuz ve bir once yaptiginiz degisiklikleri default/ilk haline getiriniz. '''
            # ''' 4. Mevcut kanal listesi secili iken, From-Until secimi icin, From'u bugunden daha once bir gun seciniz(Sol navigasyon ile secilebilir) '''
            # ''' 5. From-Until secimi icin, Until'i Sunday seciniz ve search yapiniz. '''
            api.sendKeys(['text+1', 'down+1', 'left+1', 'down+1', 'left+1*3', 'down+1*3', 'ok+5'])
            # ''' 4. Arama kritlerine uyarak tekrar search yapiniz uyarisi gelmelidir. '''
            api.testImages('EPG_GuideSearch_TodayTuesday_CurrentChannelList-ref', msg='Arama kritlerine uyarak tekrar search yapiniz uyarisi gelmelidir.')
            api.sendKeys(['ok+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_31')
    api.setTestCaseDescription('EPG Type - Timeline - Timeline Schedule to Now-Next Schedule')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Now-Next gorunumunu sec '''
            api.sendKeys(['mheg_epg+3', 'red+3'])
            # ''' 3. Now-Next gorunumune gecmeli, Timeline Schedule gorunumunde event'leri gorunen kanallarin event bilgileri Now-Next gorunumunde de gorulmeli. '''
            api.testImages('EPG_TimeLinetoNowNext-ref', msg='Now-Next gorunumune gecmeli, Timeline Schedule gorunumunde event leri gorunen kanallarin event bilgileri Now-Next gorunumunde de gorulmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_32')
    api.setTestCaseDescription('EPG Type - Timeline - Record Current Event')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Mevcut kanalda Current Event'e record kurun '''
            api.sendKeys(['mheg_epg+3', 'ok+1', 'up+1', 'ok+10', 'exit+5', 'info+0.8'])
            # ''' 3. Record kurulan yayina gitmeli, record baslamali. '''
            api.testImages('EPG_TimelineSchedule_RecordCurrentEvent-ref', mask=api.infoBarMask, msg='Record kurulan yayina gitmeli, record baslamali.')
            # ''' *** Bu bolum onemli. Eger record isleminde record yapilan kanala gidilmezse kanal info yerine, epg info aciliyor. Bu yuzden diger caseler yanlis gidiyor. Bu bolum bunu kontrol edip duzeltir. '''
            api.sendKeys(['exit2+2*2', 'mheg_epg+3'])
            if api.testImages('EPGInfoOpen-ref', recordResults=False, limit=50)[0]:
                api.sendKeys(['info+1'])
            api.sendKeys(['ok+1', 'down+1', 'ok+1*2'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_33')
    api.setTestCaseDescription('EPG Type - Timeline - Timeline Schedule to List Schedule')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. List Schedule gorunumunu sec '''
            api.sendKeys(['mheg_epg+3', 'green+3'])
            # ''' 3. List Schedule gorunumune gecmeli, Timeline Schedule gorunumunde event'leri gorunen kanallarin event bilgileri List Schedule gorunumunde de gorulmeli. '''
            api.testImages('EPG_TimeLinetoList-ref', msg='List Schedule gorunumune gecmeli, Timeline Schedule gorunumunde event leri gorunen kanallarin event bilgileri List Schedule gorunumunde de gorulmeli.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC04_34')
    api.setTestCaseDescription('EPG Type - Timeline - Exit EPG with Return or Back')
    if not api.start():
        try:
            if not ftiCompleted: 
                doFTI_ImportChList(api, 'GERMANY')
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1+7'])
            # ''' 2. Tekrar Timeline Schedule gorunumune geri don. '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. EPG'den Return ya da Back kumanda komutlari ile cik. '''
            api.sendKeys(['back+10', 'info+0.5'])
            # ''' 4. Mevcut kanala geri donmeli, kanalda goruntu ve ses kontrol edilmeli, bir problem olmamali. '''
            api.testImages('EPG_GoChannel-ref', mask=api.infoBarMask, msg='Mevcut kanala geri donmeli, kanalda goruntu ve ses kontrol edilmeli, bir problem olmamali.')
            api.videoAnalysis(duration=(20, 0, 30), tolerance=(5, 0, 5), msg='Goruntude problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

def EPG_TC06(api):
    api.setTestCaseName('EPG_TC06_01')
    api.setTestCaseDescription('EPG - Day Mode - Check 21 Days EPG Data')
    if not api.start():
        try:
            api.doFTI(api)
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH25)
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(['1008+7'])
            # ''' 2. EPG ac ve kanallarin program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. EPG'de kanala ait 21 gunluk EPG datasini kontrol et. '''
            for i in range(21):
                api.testImages('EPG_Day_'+str(i)+'-ref')
                api.sendKeys(['progup+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

    api.setTestCaseName('EPG_TC06_02')
    api.setTestCaseDescription('EPG Day Mode - Check 14 Days EPG Data')
    if not api.start():
        try:
            api.doFTI(api)
            # ''' 1. Genel kullanilan kanali aciniz. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH26)
            api.sendKeys(['1000+7'])
            # ''' 2. EPG ac ve kanallarin program bilgilerinin gelmesini bekle '''
            api.sendKeys(['mheg_epg+3'])
            # ''' 3. EPG'de kanala ait 14 gunluk EPG datasini kontrol et. '''
            for i in range(14):
                api.testImages('EPG_Day_'+str(i)+'-ref')
                api.sendKeys(['progup+1'])
            api.sendKeys(['exit2*2'])
        except:
            api.printError()
        api.end(False)

