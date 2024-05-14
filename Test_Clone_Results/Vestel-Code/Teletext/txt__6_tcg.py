# DVB-S Teletext Controls

from customTime import sleep

def test(api):
    Teletext_001_001_000_new(api)
    Teletext_001_001_001(api)
    Teletext_001_001_002(api)
    Teletext_001_001_003(api)
    Teletext_001_001_004(api)
    Teletext_001_001_005(api)
    Teletext_001_001_006(api)
    Teletext_001_001_007(api)
    Teletext_001_001_008(api)
    Teletext_001_001_009(api)
    Teletext_001_002_001(api)
    Teletext_001_002_002(api)
    Teletext_001_002_003(api)
    Teletext_001_002_004(api)
    Teletext_001_002_005(api)
    Teletext_001_002_006(api)
    Teletext_001_003_001(api)
    Teletext_001_003_002(api)
    Teletext_001_003_003(api)
    Teletext_001_003_005(api)
    Teletext_001_003_006(api)
    Teletext_001_003_007(api)
    Teletext_001_003_008(api)
    Teletext_001_004_001(api)
    Teletext_001_005_001(api)
    Teletext_001_005_002(api)
    Teletext_001_005_003(api)
    Teletext_001_005_004(api)
    Teletext_001_005_005(api)
    # CH35
    Teletext_002_001_001(api)
    # CH12
    Teletext_002_001_002(api)
    # East
    Teletext_003_001_001(api)
    # Cyrilic
    Teletext_003_001_002(api)
    # Turk\Gre
    Teletext_003_001_003(api)
    # Arabic
    Teletext_003_001_004(api)
    # West
    Teletext_003_001_005(api)

def Teletext_001_001_000_new(api):
    resultArray = api.getTestCaseResult(tcID=range(1, 11))
    runPreConditions = 'FAIL' in resultArray or 'INCONCLUSIVE' in resultArray or 'SEMIAUTO' in resultArray or len(resultArray) == 0
    if runPreConditions:
        api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
        api.stopPlayStream(api, 'StreamPlayer', api.DVBS_10750_27500)
        api.sendKeys(api.MANUAL_CH_SCAN_SAT_10750FREG)
        chnNo = api.getChannelNumber(api.usingChannelName, 0)
        api.sendKeys([str(chnNo) + '+10'])

    api.setTestCaseName('Teletext_001_001_000_new')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri (Yeni)')
    if not api.start():
        try:
            # ''' Kumanda uzerinden atanmis tus ile Teletexti aciniz. (TRT1 HD) Ana sayfada iken subpage aciniz ve 5 dk bekleyiniz. Saatin guncellendigini kontrol ediniz. '''
            chnNo = api.getChannelNumber(api.usingChannelName, 0)
            if chnNo == 0:
                print('Channel not found!')
            else:
                api.sendKeys([str(chnNo)+'+10', 'text+3', '100+3'])
                api.grabImage('controlTime_', count=4, delay=30, nView=4, msg='Saatin guncellendigini kontrol ediniz. Resimler 30 saniye ara ile cekilmistir.')
                # ''' Teletext kapat. '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_001(api):
    api.setTestCaseName('Teletext_001_001_001')
    api.setTestCaseDescription('DVB-S Teletext kontrolleri 1')
    if not api.start():
        try:
            # ''' Kumanda uzerinden atanmis tus ile Teletexti aciniz. (TRT1 HD), Program Up ile 10 page ileri gidiniz. '''
            api.sendKeys(['text+5', '100+3', 'up+3*10'])
            # ''' Ilgili page"e geldiginde page sorunsuz acilmali, karakterlerde problem olmamalidir. '''
            api.testImages('TRT1HD_Teletext_Page_111-ref', mask=api.txtMask, msg='Ilgili page"e geldiginde page sorunsuz acilmali, karakterlerde problem olmamalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_002(api):
    api.setTestCaseName('Teletext_001_001_002')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 2')
    if not api.start():
        try:
            # ''' Teletext index sayfasina gidiniz, Program Down ile 10 page geri gidiniz. '''
            api.sendKeys(['text+5', '100+3', 'down+1*10'])
            # ''' Ilgili page"e geldiginde page sorunsuz acilmali, karakterlerde problem olmamalidir. '''
            api.testImages('TRT1HD_Teletext_Page_594-ref', mask=api.txtMask, msg='(Page 594) Ilgili page"e geldiginde page sorunsuz acilmali, karakterlerde problem olmamalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_003(api):
    api.setTestCaseName('Teletext_001_001_003')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 3')
    if not api.start():
        try:
            # ''' Kumanda uzerindeki numeric tuslari kullanarak bir sayfaya gidiniz.
            api.sendKeys(['text+5', '250+3'])
            # ''' Ilgili page"e geldiginde page sorunsuz acilmali, karakterlerde problem olmamalidir.
            api.testImages('TRT1HD_Teletext_Page_250-ref', mask=api.txtMask, msg='(Page 250) Ilgili page"e geldiginde page sorunsuz acilmali, karakterlerde problem olmamalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_004(api):
    api.setTestCaseName('Teletext_001_001_004')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 4')
    if not api.start():
        try:
            # ''' Bulunmayan page"e gitmeye calisiniz. '''
            api.sendKeys(['text+5', '888+3'])
            api.grabImage('controlSearch_', count=4, delay=10, nView=4, msg='Bulamayan sayfa icin surekli arayacak. Arama yapildigini kontrol ediniz.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_005(api):
    api.setTestCaseName('Teletext_001_001_005')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 5')
    if not api.start():
        try:
            # ''' Index sayfasina geri donunuz. '''
            # ''' 4 renk tusuna atanmis fonksiyonlari tek tek kontrol ediniz.(Kumanda uzerinden kirmizi, mavi, sari, yesil tuslari) '''
            # ''' Renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir. '''
            api.sendKeys(['text+5', '100+5', 'red+5'])
            api.testImages('TRT_Teletext_Gundem_red-ref', mask=api.txtMask, msg='Kirmizi, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            api.sendKeys(['100+5', 'blue+5'])
            api.testImages('TRT_Teletext_Ekonomi_blue-ref', mask=api.txtMask, msg='Mavi, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            api.sendKeys(['100+5', 'yellow+5'])
            api.testImages('TRT_Teletext_HavaYol_green-ref', mask=api.txtMask, msg='Sari, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            api.sendKeys(['100+5', 'green+5'])
            api.testImages('TRT_Teletext_Spor_yellow-ref', mask=api.txtMask, msg='Yesil, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_006(api):
    api.setTestCaseName('Teletext_001_001_006')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 6')
    if not api.start():
        try:
            # ''' Index sayfasina geri donunuz. Ilk basta right ve left imlecin otomatik hareket etmemesi icin eklendi. '''
            api.sendKeys(['text+5', '100+5', 'right+1', 'left+1'])
            # ''' Index sayfasi altindaki subpage"ler arasi sag/sol navigasyon ile dolasiniz. '''
            controlImage = []
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_IndexPage')
            api.sendKeys(['right+1'])
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_Right_1')
            api.sendKeys(['right+1'])
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_Right_2')
            api.sendKeys(['right+1'])
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_Right_3')
            api.sendKeys(['left+1'])
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_Left_1')
            api.sendKeys(['left+1'])
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_Left_2')
            api.sendKeys(['left+1'])
            controlImage += api.grabImage('TRT_Teletext_SubPageControl_Left_3')
            # ''' Subpage"ler arasi dolasimda bir problem olmamalidir. '''
            api.showImages(controlImage, nView=7, msg='Subpage"ler arasi dolasimda bir problem olmamalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_007(api):
    api.setTestCaseName('Teletext_001_001_007')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 7')
    if not api.start():
        try:
            # ''' Index sayfasina geri donunuz ve 2 page up yapiniz. '''
            api.sendKeys(['text+5', '100+5', 'progup+3*2'])
            # ''' Kumanda uzerinden Teletext tusuna basiniz. '''
            api.sendKeys(['text+5'])
            # ''' Mix teletext acilmalidir, teletext bilgisi arkaplanda kanalin goruntusu uzerine basilmalidir. '''
            api.grabImage('TRT_MixTeletext', nView=1, msg='Mix teletext acilmalidir, teletext bilgisi arkaplanda kanalin goruntusu uzerine basilmalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_008(api):
    api.setTestCaseName('Teletext_001_001_008')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 8')
    if not api.start():
        try:
            # ''' Kumanda uzerinden Teletext tusuna basiniz. Teletextten cikip mevcut kanal geri donmelidir. '''
            api.sendKeys(['text+5*3', 'info+1'])
            api.testImages('TRT_InfoBar-ref', mask=api.infoBarMask, msg='Teletextten cikip mevcut kanal geri donmelidir.')
        except:
            api.printError()
        api.end(False)

def Teletext_001_001_009(api):
    api.setTestCaseName('Teletext_001_001_009')
    api.setTestCaseDescription('DVB-S Teletext Kontrolleri 9')
    if not api.start():
        try:
            # ''' Mevcut kanalda 10 Program Up ve 10 Program Down yaparak mevcut kanala geri donunuz ve kanalda iken teletext aciniz. '''
            chnNo = api.getChannelNumber(api.usingChannelName, 0, getList=False)
            if chnNo == 0:
                print('Channel not found!')
            else:
                api.sendKeys([str(chnNo)+'+3', 'progup+3*10', 'progdown+3*10'])
                # ''' Teletext hemen acilmadigi icin araya sure eklendi. '''
                api.sendKeys(['+10', 'text+15'])
                # ''' Teletext index sayfasi acilmalidir. '''
                api.testImages('TRT_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='Teletext index sayfasi acilmalidir.')
                # ''' Teletext kapat. '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_002_001(api):
    api.setTestCaseName('Teletext_001_002_001')
    api.setTestCaseDescription('Teletext Language Karakter Kontrolleri 1')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
            # ''' Stimulation linkindeki stream"a tune olunuz ve TXT bilgisi iceren kanali aciniz. (CINE+) '''
            api.stopPlayStream(api, 'StreamPlayer', api.DVBS_10750_27500_TurkGreek)
            api.sendKeys(api.MANUAL_CH_SCAN_SAT_10750FREG)
            chnNo = api.getChannelNumber(api.usingChannelName2, 0)
            if chnNo == 0:
                print('Channel not found!')
            else:
                # ''' Teletext language"i Turk/Greek seciniz. Kanali P+/P- ile bir kez refresh yapiniz. '''
                # ''' 105. sayfa kendiliginden degismedigi icin acildi. '''
                api.sendKeys(api.LANGUAGESETTING_TXT_TURKGRE_DVBT + ['progup+3', 'progdown+3'])
                # ''' Teletext hemen acilmadigi icin eklendi. '''
                api.sendKeys(['+10', 'text+10', '105+10'])
                # ''' Teletext aciniz ve karekterleri kontrol ediniz. '''
                api.testImages('CINE_Teletext_Page_105-ref', mask=api.txtMask, msg='Teletext acilmali ve eksik ya da bozuk karakter olmamalidir.')
                # ''' Teletext kapat. '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_002_002(api):
    api.setTestCaseName('Teletext_001_002_002')
    api.setTestCaseDescription('Teletext Language Karakter Kontrolleri 2')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
            # ''' Stimulation linkindeki stream"a tune olunuz ve DVB-S Turksat uydusundan gelen TRT kanalina tune olunuz. '''
            api.stopPlayStream(api, 'StreamPlayer', api.DVBS_10750_27500)
            api.sendKeys(api.MANUAL_CH_SCAN_SAT_10750FREG)
            chnNo = api.getChannelNumber(api.usingChannelName, 0)
            if chnNo == 0:
                print('Channel not found!')
            else:
                # ''' Teletext language"in Turk/Greek oldugundan emin olunuz. TRT1 HD kanalina tune olunuz. Kanali P+/P- ile bir kez refresh yapiniz. '''
                # ''' Tekrar Turk/Gre streami oynadiginda kanal 1 secmek gerekiyor. Teletext aciniz (main page) ve karekterleri kontrol ediniz. '''
                # ''' 101. sayfa degismedigi icin acildi. '''
                api.sendKeys([str(chnNo)+'+5'] + api.LANGUAGESETTING_TXT_TURKGRE_DVBT)
                api.sendKeys(['+20', 'text+10', '101+5'])
                # ''' Teletext index sayfasi acilmalidir. '''
                api.testImages('TRT_Teletext_Page_101-ref', mask=api.txtMask, msg='Teletext sayfasinda eksik ya da bozuk karakter olmamalidir.')
                # ''' Teletext kapatilir ve Language Weste geri dondurulur '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_002_003(api):
    api.setTestCaseName('Teletext_001_002_003')
    api.setTestCaseDescription('Teletext Language Karakter Kontrolleri 3')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
            # ''' Stimulation linkindeki stream"a tune olunuz ve CTI kanalini aciniz. '''
            api.stopPlayStream(api, 'StreamPlayer', api.DVBS_10750_27500_East)
            api.sendKeys(api.MANUAL_CH_SCAN_SAT_10750FREG)
            chnNo = api.getChannelNumber('CT1', 0)
            if chnNo == 0:
                print('Channel not found!')
            else:
                # ''' Teletext language"i East seciniz. Kanali P+/P- ile bir kez refresh yapiniz. Stimulation linkindeki stream"a tune olunuz ve TXT bilgisi iceren kanali aciniz. Teletext aciniz(Page 898) ve karakterleri kontrol ediniz. '''
                api.sendKeys(api.LANGUAGESETTING_TXT_EAST_DVBT + [str(chnNo)+'+5', 'progup+5', 'progdown+15', 'text+10', '898+5'])
                api.testImages('CT1_Teletext_Page_898-ref', mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir.')
                api.doPowerCycle(api)
                api.sendKeys(['text+5', '898+15'])
                api.testImages('CT1_Teletext_AfterPowerCycle_Page_898-ref', mask=api.txtMask, msg='Power off/on sonrasi teletextde eksik ya da bozuk karakter olmamalidir.')
                # ''' Teletext kapatilir ve Language Weste geri dondurulur '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_002_004(api):
    api.setTestCaseName('Teletext_001_002_004')
    api.setTestCaseDescription('Teletext Language Karakter Kontrolleri 4')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
            # ''' Stimulation linkindeki stream"a tune olunuz ve (Nrtbin Kahan) kanalini aciniz. (Stream: CH30_DVB-T2-LONG-MOSCOW-DVBT.MPG) '''
            api.stopPlayStream(api, 'StreamPlayer', api.DVBS_10750_27500_Cyrillic)
            api.sendKeys(api.MANUAL_CH_SCAN_SAT_10750FREG)
            # ''' Teletext language"i Cyrillic seciniz. Kanali P+/P- ile bir kez refresh yapiniz. '''
            # ''' Stimulation linkindeki stream"a tune olunuz ve TXT bilgisi iceren kanali aciniz. '''
            # ''' Teletext aciniz ve karekterleri kontrol ediniz. Teletext gec acildigi icin kanala gelinince uzun bekleniyor. '''
            api.sendKeys(api.LANGUAGESETTING_TXT_CYRILLIC_DVBT + ['progup+5', 'progdown+5', 'text+60', '120+5'])
            api.testImages('NrtbinKahan_Teletext_Page_120-ref', mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir.')
            # ''' Teletext kapatilir. '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_002_005(api):
    api.setTestCaseName('Teletext_001_002_005')
    api.setTestCaseDescription('Teletext Language Karakter Kontrolleri 5')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
            # ''' Stimulation linkindeki stream"a tune olunuz ve IRIB-TV2 kanalini aciniz. (Stream: ch37-1.ts) '''
            api.stopPlayStream(api, 'StreamPlayer', api.DVBS_10750_27500_Arabic)
            api.sendKeys(api.MANUAL_CH_SCAN_SAT_10750FREG)
            chnNo = api.getChannelNumber('IRIB-TV2', 0)
            if chnNo == 0:
                print('Channel not found!')
            else:
                # ''' Teletext language"i Arabic seciniz. Kanali P+/P- ile bir kez refresh yapiniz. '''
                # ''' Stimulation linkindeki stream"a tune olunuz ve TXT bilgisi iceren kanali aciniz. '''
                # ''' Teletext aciniz ve karekterleri kontrol ediniz. Teletext bu yayinde gec aciliyor. Bu yuzden cok bekle. '''
                api.sendKeys(api.LANGUAGESETTING_TXT_ARABIC_DVBT + ['progup+5', 'progdown+5', str(chnNo)+'+15', 'text+60', '100+10'])
                api.testImages('IRIBTV2_Teletext_Page_120-ref', mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir.')
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_002_006(api):
    resultArray = api.getTestCaseResult(tcID=range(16, 24))
    runPreConditions = 'FAIL' in resultArray or 'INCONCLUSIVE' in resultArray or 'SEMIAUTO' in resultArray or len(resultArray) == 0
    if runPreConditions:
        api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
        # ''' Stream MHz._ses senkron_undifened.ts '''
        api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_474Mhz_CH21_West)
        # ''' Stimulation linkindeki DVB-T streami oynatiniz ve TF1 kanalina tune olunuz. '''
        api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH21)
        chnNo = api.getChannelNumber(api.usingChannelName3, 0)
        api.sendKeys([str(chnNo)+'+10'])

    api.setTestCaseName('Teletext_001_002_006')
    api.setTestCaseDescription('Teletext Language Karakter Kontrolleri 6')
    if not api.start():
        try:
            # ''' Teletext language"i West(Default) seciniz. Kanali P+/P- ile bir kez refresh yapiniz. Teletext aciniz(main page) ve karekterleri kontrol ediniz. '''
            api.sendKeys(api.LANGUAGESETTING_TXT + ['progup+3', 'progdown+15', 'text+10', '105+5'])
            api.testImages('TF1_Teletext_Page_105-ref', mask=api.txtMask, msg='(Page 105)Eksik ya da bozuk karakter olmamalidir.')
            # ''' Teletext kapatilir '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_001(api):
    api.setTestCaseName('Teletext_001_003_001')
    api.setTestCaseDescription('DVB-T Teletext Kontrolleri 1')
    if not api.start():
        try:
            # ''' Teletext ac Stream devam ediyor. Stream MHz._ses senkron_undifened.ts, Program Up ile 10 page ileri gidiniz. '''
            api.sendKeys(['text+10', '100+5', 'progup+3*10'])
            # ''' Ilgili page"e gelindiginde page sorunsuz acilmali, karakterlerde problem olmamalidir. '''
            api.testImages(['TF1_Teletext_Page_110-ref', 'TF1_Teletext_Page_110_2-ref'], mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir.')
            # ''' Teletext kapatilir '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_002(api):
    api.setTestCaseName('Teletext_001_003_002')
    api.setTestCaseDescription('DVB-T Teletext kontrolleri 2')
    if not api.start():
        try:
            # ''' Stream MHz._ses senkron_undifened.ts '''
            api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_474Mhz_CH21_West)
            # ''' Stimulation linkindeki DVB-T streami oynatiniz ve TF1 kanalina tune olunuz. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH21)
            chnNo = api.getChannelNumber(api.usingChannelName3, 0)
            api.sendKeys([str(chnNo)+'+10'])
            # ''' Teletext ac Stream devam ediyor. Stream MHz._ses senkron_undifened.ts, Program Up ile 10 page geri gidiniz. '''
            api.sendKeys(['text+10', '100+5', 'progdown+3*10'])
            masterImages = ['TF1_Teletext_Page_608_1-ref', 'TF1_Teletext_Page_608_2-ref', 'TF1_Teletext_Page_608_3-ref', 'TF1_Teletext_Page_608_4-ref']
            # ''' Ilgili page"e gelindiginde page sorunsuz acilmali, karakterlerde problem olmamalidir. '''
            api.testImages(masterImages, mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir. Teletext data icerigi degisti ise kontrol ediniz.')
            # ''' Teletext kapatilir '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_003(api):
    api.setTestCaseName('Teletext_001_003_003')
    api.setTestCaseDescription('DVB-T Teletext Kontrolleri 3')
    if not api.start():
        try:
            # ''' Teletext ac Stream devam ediyor. Stream MHz._ses senkron_undifened.ts, Kumanda uzerinde numeric tuslari kullanarak bir sayfaya gidiniz. '''
            api.sendKeys(['text+10', '615+5'])
            # ''' Ilgili page"e gelindiginde page sorunsuz acilmali, karakterlerde problem olmamalidir. '''
            api.testImages('TF1_Teletext_Page_615-ref', mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir. Teletext data icerigi degisti ise kontrol ediniz.')
            api.sendKeys(['750+5'])
            api.grabImage('controlSearch_', count=4, delay=10, nView=4, msg='Bulamayan sayfa icin surekli arayacak. Arama yapildigini kontrol ediniz.')
            # ''' Teletext kapatilir '''
            api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_005(api):
    api.setTestCaseName('Teletext_001_003_005')
    api.setTestCaseDescription('DVB-T Teletext Kontrolleri 5')
    if not api.start():
        try:
            # ''' Stimulation linkindeki stream"a tune olunuz ve TXT bilgisi iceren kanali aciniz. '''
            # ''' 4 renk tusuna atanmis fonksiyonlari tek tek kontrol ediniz.(Kumanda uzerinden kirmizi, mavi, sari, yesil tuslari) '''
            # ''' Renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir. '''
            api.sendKeys(['text+5', '105+5', 'red+5'])
            api.testImages('TF1_Teletext_104_red-ref', mask=api.txtPageNoMask, msg='Kirmizi, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            api.sendKeys(['blue+5'])
            api.testImages('TF1_Teletext_200_blue-ref', mask=api.txtPageNoMask, msg='Mavi, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            api.sendKeys(['yellow+5'])
            api.testImages('TF1_Teletext_210_yellow-ref', mask=api.txtPageNoMask, msg='Sari, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            api.sendKeys(['green+5'])
            api.testImages('TF1_Teletext_213_green-ref', mask=api.txtPageNoMask, msg='Yesil, renk tuslarina atanmis fonksiyonlar o tuslara basildiginda problemsiz bir sekilde calismalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2+5'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_006(api):
    api.setTestCaseName('Teletext_001_003_006')
    api.setTestCaseDescription('DVB-T Teletext kontrolleri 6')
    if not api.start():
        try:
            # ''' Index sayfasina geri donunuz. Ilk basta right ve left imlecin otomatik hareket etmemesi icin yapilmaktadir. '''
            api.sendKeys(['text+5', '100+5', 'right+1', 'left+1'])
            # ''' Index sayfasi altindaki subpage"ler arasi sag/sol navigasyon ile dolasiniz. '''
            api.sendKeys(['right+1'])
            controlImage = []
            controlImage += api.grabImage('PIC_right_1')
            api.sendKeys(['right+1'])
            controlImage += api.grabImage('PIC_right_2')
            api.sendKeys(['left+1'])
            controlImage += api.grabImage('PIC_left_1')
            api.sendKeys(['left+1'])
            controlImage += api.grabImage('PIC_left_2')
            # ''' Subpage"ler arasi dolasimda bir problem olmamalidir. '''
            api.showImages(controlImage, nView=4, msg='Subpage"ler arasi dolasimda bir problem olmamalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3*2+3'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_007(api):
    api.setTestCaseName('Teletext_001_003_007')
    api.setTestCaseDescription('DVB-T Teletext Kontrolleri 7')
    if not api.start():
        try:
            # ''' Index sayfasina geri donunuz ve 3 page up yapiniz. '''
            api.sendKeys(['text+5', '100+5', 'progup+3*3'])
            # ''' Kumanda uzerinden Teletext tusuna basiniz. '''
            api.sendKeys(['text+5'])
            # ''' Mix teletext acilmalidir, teletext bilgisi arkaplanda kanalin goruntusu uzerine basilmalidir. '''
            api.grabImage('TF1_MixTeletext', nView=1, msg='Mix teletext acilmalidir, teletext bilgisi arkaplanda kanalin goruntusu uzerine basilmalidir.')
            # ''' Teletext kapat. '''
            api.sendKeys(['text+3'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_003_008(api):
    api.setTestCaseName('Teletext_001_003_008')
    api.setTestCaseDescription('DVB-T Teletext Kontrolleri 8')
    if not api.start():
        try:
            # ''' Mevcut kanalda 10 Program Up ve 10 Program Down yaparak mevcut kanala geri donunuz ve kanalda iken teletext aciniz. '''
            api.sendKeys(['progup+3*10', 'progdown+3*10+15'])
            api.sendKeys(['text+15'])
            # ''' Teletext index sayfasi acilmalidir. '''
            api.testImages('TF1_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='Teletext index sayfasi acilmalidir.')
            # ''' Kumanda uzerinden Teletext tusuna basiniz. Teletextten cikip mevcut kanal geri donmelidir. '''
            api.sendKeys(['text+5*2', 'info+1'])
            api.testImages('TF1_InfoBar-ref', mask=api.infoBarMask, msg='Teletextten cikip mevcut kanal geri donmelidir.')
        except:
            api.printError()
        api.end(False)

def Teletext_001_004_001(api):
    api.setTestCaseName('Teletext_001_004_001')
    api.setTestCaseDescription('DVB-C Teletext Kontrolleri 1')
    if not api.start():
        try:
            # ''' Vestel RF - DVB-C 338 MHz"e manual search ile tune olunuz ve Das Erste HD kanalini aciniz. FTI"dan sonra 2. kanal '''
            # ''' Kumanda uzerinden Teletext"i acmak icin atanmis tusa basarak Teletext"e giriniz ve digit tuslari ile sayfa degistiriniz. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_CABLE_338FREG)
            chNo_DasErste = api.getChannelNumber('Das Erste HD')
            if(chNo_DasErste == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys([str(chNo_DasErste)+'+10', 'text+10'])
                # ''' Teletext acilmalidir, digit tuslari ile ilgili sayfa degisiklikleri yapilmalidir. '''
                api.testImages('text_DasErsteHD-ref', mask=api.txtPageNoMask, msg='Das Erste HD kanalinda teletext acilmalidir.')
                api.sendKeys(['101+3'])
                api.testImages('text_Channel_DasErsteHD_Page_101-ref', mask=api.txtPageNoMask, msg='Das Erste HD kanalinda teletext 101. sayfa acilmalidir.')
                api.sendKeys(['102+3'])
                api.testImages('text_Channel_DasErsteHD_Page_102-ref', mask=api.txtPageNoMask, msg='Das Erste HD kanalinda teletext 102. sayfa acilmalidir.')
                api.sendKeys(['103+3'])
                api.testImages('text_Channel_DasErsteHD_Page_103-ref', mask=api.txtPageNoMask, msg='Das Erste HD kanalinda teletext 103. sayfa acilmalidir.')
                # ''' Kumanda uzerinden Teletext tusuna basiniz. '''
                api.sendKeys(['text+5*2', 'info+1'])
                # ''' Teletextten cikip mevcut kanal geri donmelidir. '''
                api.testImages('channel_DasErsteHd-ref', mask=api.infoBarMask, msg='Teletextten cikip mevcut kanal geri donmelidir.')
        except:
            api.printError()
        api.end(False)

def Teletext_001_005_001(api):
    api.setTestCaseName('Teletext_001_005_001')
    api.setTestCaseDescription('Teletext Performans Kontrolleri 1')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI)
            # ''' Stream MHz._ses senkron_undifened.ts DVB-T '''
            api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_474Mhz_CH21_West)
            # ''' Stimulation linkindeki DVB-T streami oynatiniz ve TF1 kanalina tune olunuz. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH21)
            chNo_TF1 = api.getChannelNumber('TF1')
            chNo_TMC = api.getChannelNumber('TMC', getList=False)
            if(chNo_TF1 == 0 or chNo_TMC == 0):
                print('Kanal Bulunamadi')
            else:
                # ''' Subtitle on yapiniz ve sonra teletext acip/kapatiniz. Teletext aciniz kapayiniz. '''
                # ''' Ayni streamden gelen TMC kanalina geciniz. (TMC: 10), Teletext acmaya calisiniz. '''
                api.sendKeys([str(chNo_TF1)+'+10', 'subtitles+5', 'text+15*3', str(chNo_TMC)+'+10', 'text+0.5'])
                # ''' Teletext tusuna basildiginda no teletext uyarisi cikmali, herhangi bir crash/reset problemi gorunmemelidir. '''
                api.testImages('_noTeletextAvailable-ref', mask=api.txtNotAvailable, msg='Teletext tusuna basildiginda No Teletext Available uyarisi cikmali, herhangi bir crash/reset problemi gorunmemelidir.')
        except:
            api.printError()
        api.end(False)

def Teletext_001_005_002(api):
    api.setTestCaseName('Teletext_001_005_002')
    api.setTestCaseDescription('Teletext Performans Kontrolleri 2')
    if not api.start():
        try:
            api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_474Mhz_CH21_West)
            # ''' Stimulation linkindeki DVB-T streami oynatiniz ve TF1 kanalina tune olunuz., Tekrar TF1 kanalini aciniz. '''
            chNo_TF1 = api.getChannelNumber('TF1', getList=False)
            if(chNo_TF1 == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys([str(chNo_TF1)+'+10', 'text+15'])
                # ''' Teletext"e giriniz, data geldikten sonra RF kablosunu cekip 30 sn bekleyiniz. '''
                api.testImages('TF1_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='Teletext sayfasina datanin geldigi gorulmelidir.')
                # Rf kablosunun cekilmesi (Stream durdur) '''
                api.plugInOutRFCable(api, plugIn=False)
                api.sendKeys(['+30'])
                # ''' Teletext bilgisi ekrandan kalkmalidir, no signal durumuna gecmelidir. '''
                api.testImages('_noSignal-ref', msg='Teletext bilgisi ekrandan kalkmalidir, no signal durumuna gecmelidir.')
        except:
            api.printError()
        api.end(False)

def Teletext_001_005_003(api):
    api.setTestCaseName('Teletext_001_005_003')
    api.setTestCaseDescription('Teletext Performans Kontrolleri 3')
    if not api.start():
        try:
            # ''' RF kablosunu tekrar takiniz ve Teletext aciniz., Stream MHz._ses senkron_undifened.ts DVB-T '''
            api.plugInOutRFCable(api, plugIn=True)
            api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_474Mhz_CH21_West)
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH21)
            # ''' Tekrar TF1 kanalini aciniz. '''
            chNo_TF1 = api.getChannelNumber('TF1', getList=False)
            if(chNo_TF1 == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys([str(chNo_TF1)+'+10', 'text+15', '100+5'])
                # ''' Teletext acilmalidir. '''
                api.testImages('TF1_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='(Page 100)Rf kablosu takildiktan sonra teletext acilmalidir.')
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_005_004(api):
    api.setTestCaseName('Teletext_001_005_004')
    api.setTestCaseDescription('Teletext Performans Kontrolleri 4')
    if not api.start():
        try:
            api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_474Mhz_CH21_West)
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH21)
            chNo_TF1 = api.getChannelNumber('TF1', getList=False)
            if(chNo_TF1 == 0):
                print('Kanal Bulunamadi')
            else:
                # ''' Teletext"te iken standby off/on yapiniz ve TV acildiktan sonra tekrar Teletext"e giriniz 20 dk teletext"te bekleyiniz. '''
                api.sendKeys([str(chNo_TF1)+'+10', 'text+10', 'standby+30*2', str(chNo_TF1)+'+10', 'text+10'])
                # ''' Teletext acilmalidir, uzun sureli beklemede problem olmamalidir. '''
                api.testImages('TF1_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='Teletext acilmalidir.')
                sleep(1200)
                api.testImages('TF1_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='Uzun sureli beklemede problem olmamalidir.')
                # ''' Teletext"te iken power off/on yapiniz ve TV acildiktan sonra tekrar Teletext"e giriniz. '''
                api.doPowerCycle(api)
                api.sendKeys([str(chNo_TF1)+'+15', 'text+10'])
                # ''' Power off/on sonrasi Teletext"e girebilmelidir. '''
                api.testImages('TF1_Teletext_Page_100-ref', mask=api.txtPageNoMask, msg='Power off/on sonrasi Teletext"e girebilmelidir.')
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_001_005_005(api):
    # ''' FRACAS-1359 nedeniyle eklendi '''
    api.setTestCaseName('Teletext_001_005_005')
    api.setTestCaseDescription('Teletext Performans Kontrolleri 5 - FRACAS-1359')
    if not api.start():
        try:
            api.sendKeys(api.FTI + ['SETCOUNTRY SPAIN+1'] + api.CONFIRMFTI + api.SET_ASTRA1)
            api.stopPlayStream(api, 'StreamPlayer2', api.DVBT_698Mhz_CH49_Spanish)
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_DIGITAL_AERIAL_CH49)
            chNo_TV3 = api.getChannelNumber('TV3HD', getList=False)
            chNo_TV3 = 1
            if(chNo_TV3 == 0):
                print('Kanal Bulunamadi')
            else:
                # ''' Stimulation linkindeki stream"a tune olunuz ve TXT bilgisi iceren kanali aciniz. '''
                api.sendKeys([str(chNo_TV3)+'+5', 'progup+5', 'progdown+15', 'text+10'])
                api.testImages('TV3_Teletext_Spain-ref', mask=api.txtMask, msg='Eksik ya da bozuk karakter olmamalidir.')
                api.doPowerCycle(api)
                api.sendKeys(['text+5'])
                api.testImages('TV3_Teletext_Spain_AfterPowerCycle-ref', mask=api.txtMask, msg='Power off/on sonrasi teletextde eksik ya da bozuk karakter olmamalidir.')
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def Teletext_002_001_001(api):
    # ''' TESTE BASLAMADAN ONCE SUB PAGE LISTESINI KONTROL EDINIZ '''
    api.setTestCaseName('Teletext_002_001_001')
    api.setTestCaseDescription('Analog Teletext Pages Channel 35')
    if not api.start():
        try:
            # ''' Channel searching Analog: Bu arama yapildiginda CHANNEL 4 isimli kanal bulunur. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN35)
            # ''' 1. CH35 Analog kanala tune olunuz ve teletext acmak icin atanmis tusa basiniz. '''
            chNo = api.getChannelNumber('CHANNEL 4')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys([str(chNo)+'+10', 'text+10'])
                pages = [
                    '100', '101', '200', '250', '400', '500', '501', '502', '503', '504', '505', '510', '511', '512', '513', '700', '710', '711', 
                    '712', '800', '820', '860', '861', '862', '866', '867', '868', '869', '870', '871', '899', '872', '873', '880', '881', '882', 
                    '883', '884', '885', '886', '887', '888', '889']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_2_1_1(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_2_1_1(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_2_1_1(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i])+'+'+str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_2_1_1(pageNumber):
    try:
        return {
            '504': ['0001', '0002', '0003', '0004', '0005'], 
            '505': ['0001', '0002', '0003', '0004'], 
            '510': ['0001', '0002', '0003'], 
            '511': ['0001', '0002'], 
            '881': ['1234', '2359', 'yellow', 'blue'], 
            '882': ['1234', '2359', 'yellow', 'blue'], 
            '886': ['0001', '0002']
            }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def _multiReferans_TXT_2_1_1(pageNumber):
    try:
        return {
            '513': ['Page'+str(pageNumber)+'_FaultOff-ref', 'Page'+str(pageNumber)+'_FaultOn-ref'], 
            '883': ['Page'+str(pageNumber)+'_Subtitle_One-ref', 'Page'+str(pageNumber)+'_Subtitle_Two-ref', 'Page'+str(pageNumber)+'_Subtitle_Three-ref', 'Page'+str(pageNumber)+'_Subtitle_Four-ref', 'Page'+str(pageNumber)+'_Subtitle_Five-ref'], 
            '884': ['Page'+str(pageNumber)+'_Subtitle_One-ref', 'Page'+str(pageNumber)+'_Subtitle_Two-ref', 'Page'+str(pageNumber)+'_Subtitle_Three-ref', 'Page'+str(pageNumber)+'_Subtitle_Four-ref', 'Page'+str(pageNumber)+'_Subtitle_Five-ref'], 
            '885': ['Page'+str(pageNumber)+'_NowHere_One-ref', 'Page'+str(pageNumber)+'_NowHere_Two-ref', 'Page'+str(pageNumber)+'_NowHere_Three-ref'], 
            '887': ['Page'+str(pageNumber)+'_NewsFlashOff-ref', 'Page'+str(pageNumber)+'_NewsFlashOn-ref']
            }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def Teletext_002_001_002(api):
    api.setTestCaseName('Teletext_002_001_002')
    api.setTestCaseDescription('Analog Teletext Pages Channel 12')
    if not api.start():
        try:
            # ''' Channel searching Analog: Bu arama yapildiginda CHANNEL 4 isimli kanal bulunur. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN12)
            # ''' 1. C12 Analog kanala tune olunuz ve teletext acmak icin atanmis tusa basiniz. '''
            chNo = api.getChannelNumber('C12')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys([str(chNo)+'+10', 'text+10'])
                pages = ['600', '610', '611', '620', '621', '630', '631', '650', '651', '660', '661', '670', '671', '672', '680', '681', '682', '683']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_2_1_2(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_2_1_2(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_2_1_2(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i])+'+'+str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_2_1_2(pageNumber):
    try:
        return {'-1' : []}.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def _multiReferans_TXT_2_1_2(pageNumber):
    try:
        return {
            '651': ['Page'+str(pageNumber)+'_1_4-ref', 'Page'+str(pageNumber)+'_2_4-ref', 'Page'+str(pageNumber)+'_3_4-ref', 'Page'+str(pageNumber)+'_4_4-ref'], 
            '660': ['Page'+str(pageNumber)+'_1_2-ref', 'Page'+str(pageNumber)+'_2_2-ref'], 
            '671': ['Page'+str(pageNumber)+'_1_3-ref', 'Page'+str(pageNumber)+'_2_3-ref', 'Page'+str(pageNumber)+'_3_3-ref'], 
            '672': ['Page'+str(pageNumber)+'_1_3-ref', 'Page'+str(pageNumber)+'_2_3-ref', 'Page'+str(pageNumber)+'_3_3-ref']
            }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def Teletext_003_001_001(api):
    api.setTestCaseName('Teletext_003_001_001')
    api.setTestCaseDescription('Channel 35 Language East')
    if not api.start():
        try:
            # ''' Channel searching Analog: Bu arama yapildiginda CHANNEL 4 isimli kanal bulunur. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN35)
            # ''' 1. Language Settings menuden Teletext dilini East seciniz. '''
            chNo = api.getChannelNumber('CHANNEL 4')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys(api.LANGUAGESETTING_TXT_EAST_DVBT + [str(chNo)+'+10', 'text+10'])
                pages = ['200', '202', '204', '205', '210', '217', '218', '219', '221', '222', '252', '254', '255', '260', '267', '268', '269', '271', '272']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_3_1_1(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_3(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_3(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i])+'+'+str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_3_1_1(pageNumber):
    try:
        return {
            '202': ['0001', '0002', '0003', '0004'], 
            '204': ['0001', '0002', '0003', '0004'], 
            '205': ['0001', '0002', '0003', '0004', '0005'], 
            '210': ['0001', '0002'], 
            '217': ['0001', '0002'], 
            '218': ['0001', '0002'], 
            '219': ['0001', '0002'], 
            '221': ['0001', '0002'], 
            '222': ['0001', '0002'], 
            '252': ['0001', '0002', '0003', '0004'], 
            '254': ['0001', '0002', '0003', '0004'], 
            '255': ['0001', '0002', '0003', '0004', '0005'], 
            '260': ['0001', '0002'], 
            '267': ['0001', '0002'], 
            '268': ['0001', '0002'], 
            '269': ['0001', '0002'], 
            '271': ['0001', '0002'], 
            '272': ['0001', '0002']
        }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def Teletext_003_001_002(api):
    api.setTestCaseName('Teletext_003_001_002')
    api.setTestCaseDescription('Channel 35 Language Cyrilic')
    if not api.start():
        try:
            # ''' Channel searching Analog: Bu arama yapildiginda CHANNEL 4 isimli kanal bulunur. '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN35)
            # ''' 1. Language Settings menuden Teletext dilini CYRILLIC seciniz. '''
            chNo = api.getChannelNumber('CHANNEL 4')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys(api.LANGUAGESETTING_TXT_CYRILLIC_DVBT + [str(chNo)+'+10', 'text+10'])
                pages = ['200', '201', '204', '205', '215', '216', '218', '219', '220', '222', '251', '254', '255', '265', '266', '268', '269', '270', '272']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_3_1_2(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_3(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_3(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i])+'+'+str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_3_1_2(pageNumber):
    try:
        return {
            '201': ['0001', '0002', '0003'], 
            '204': ['0001', '0002', '0003', '0004'], 
            '205': ['0001', '0002', '0003', '0004', '0005'], 
            '215': ['0001', '0002'], 
            '218': ['0001', '0002'], 
            '219': ['0001', '0002'], 
            '220': ['0001', '0002'], 
            '222': ['0001', '0002'], 
            '251': ['0001', '0002', '0003'], 
            '254': ['0001', '0002', '0003', '0004'], 
            '255': ['0001', '0002', '0003', '0004', '0005'], 
            '265': ['0001', '0002'], 
            '266': ['0001', '0002'], 
            '268': ['0001', '0002'], 
            '269': ['0001', '0002'], 
            '270': ['0001', '0002', '0003', '0004'], 
            '272': ['0001', '0002']
        }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def Teletext_003_001_003(api):
    api.setTestCaseName('Teletext_003_001_003')
    api.setTestCaseDescription('Channel 12 Language Turk\Gre')
    if not api.start():
        try:
            # ''' Channel searching Analog '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN12)
            # ''' 1. Language Settings menuden Teletext dilini CYRILLIC seciniz. '''
            chNo = api.getChannelNumber('C12')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys(api.LANGUAGESETTING_TXT_TURKGRE_DVBT + [str(chNo)+'+10', 'text+10'])
                pages = ['200', '201', '202', '203', '205', '206', '207', '209', '211', '212', '251', '252', '253', '255', '256', '257', '259', '261', '262']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_3_1_3(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_3(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_3(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i])+'+'+str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_3_1_3(pageNumber):
    try:
        return {
            '201': ['0001', '0002', '0003'], 
            '202': ['0001', '0002', '0003', '0004'], 
            '203': ['0001', '0002', '0003', '0004'], 
            '205': ['0001', '0002', '0003', '0004', '0005'], 
            '206': ['0001', '0002', '0003'], 
            '207': ['0001', '0002', '0003', '0004'], 
            '209': ['0001', '0002', '0003', '0004'], 
            '211': ['0001', '0002', '0003'], 
            '212': ['0001', '0002'], 
            '251': ['0001', '0002', '0003'], 
            '252': ['0001', '0002', '0003', '0004'], 
            '253': ['0001', '0002', '0003', '0004'], 
            '255': ['0001', '0002', '0003', '0004', '0005'], 
            '256': ['0001', '0002', '0003'], 
            '257': ['0001', '0002', '0003', '0004'], 
            '259': ['0001', '0002', '0003', '0004'], 
            '261': ['0001', '0002', '0003'], 
            '262': ['0001', '0002', '0003', '0004']
        }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def Teletext_003_001_004(api):
    api.setTestCaseName('Teletext_003_001_004')
    api.setTestCaseDescription('Channel 35 Language Arabic')
    if not api.start():
        try:
            api.sendKeys(api.FTI + api.CONFIRMFTI + api.SET_ASTRA1)
            # ''' Channel searching Analog '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN35)
            # ''' 1. Language Settings menuden Teletext dilini ARABIC seciniz. '''
            chNo = api.getChannelNumber('CHANNEL 4')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys(api.LANGUAGESETTING_TXT_ARABIC_DVBT + [str(chNo)+'+10', 'text+10'])
                pages = ['200', '201', '202', '208', '223', '224', '251', '252', '258', '273', '274']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_3_1_4(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_3(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_3(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i]) + '+' + str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_3_1_4(pageNumber):
    try:
        return {
            '201': ['0001', '0002', '0003'], 
            '202': ['0001', '0002', '0003', '0004'], 
            '208': ['0001', '0002', '0003', '0004', '0005', '0006'], 
            '223': ['0001', '0002'], 
            '251': ['0001', '0002', '0003'], 
            '252': ['0001', '0002', '0003', '0004'], 
            '258': ['0001', '0002', '0003', '0004', '0005', '0006'], 
            '273': ['0001', '0002']
        }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def Teletext_003_001_005(api):
    api.setTestCaseName('Teletext_003_001_005')
    api.setTestCaseDescription('Channel 12 Language West')
    if not api.start():
        try:
            # ''' Channel searching Analog '''
            api.sendKeys(api.MANUAL_CHANNEL_SCAN_ANALOGUE_BANDC_SYSBG_CHN12)
            # ''' 1. Language Settings menuden Teletext dilini WEST seciniz. '''
            chNo = api.getChannelNumber('C12')
            if(chNo == 0):
                print('Kanal Bulunamadi')
            else:
                api.sendKeys(api.LANGUAGESETTING_TXT + [str(chNo)+'+10', 'text+10'])
                pages = ['200', '201', '202', '203', '205', '206', '207', '209', '211', '213', '251', '252', '253', '255', '256', '257', '259', '261', '263']
                sleepTimePerPage = 10
                for pageIndex in range(0, len(pages)):
                    currentPage = pages[pageIndex]
                    goPage = currentPage+'+'+str(sleepTimePerPage)
                    api.sendKeys(['teletext_index+3', goPage])
                    curPgSubPgCount = _subPageCount_TXT_3_1_5(currentPage)
                    if(len(curPgSubPgCount) == 0):
                        referancesImages = []
                        if (len(_multiReferans_TXT_3(currentPage)) == 0):
                            referancesImages.append('Page'+str(currentPage)+'-ref')
                        else:
                            referancesImages = _multiReferans_TXT_3(currentPage)
                        api.testImages(referancesImages, mask=api.txtMask, grabName=None, limit=80, timeout=10)
                    else:
                        # ''' Eger sayfada subpage varsa burada subpageleri kontrol edilir. Bu bilgi fonksiyondan gelir. '''
                        for i in range(0, len(curPgSubPgCount)):
                            goSubPage = str(curPgSubPgCount[i])+'+'+str(sleepTimePerPage)
                            api.sendKeys(['teletext_index+2', goPage, 'teletext_subpage+1', goSubPage])
                            api.testImages('Page'+str(currentPage)+'_Subpage_P'+str(curPgSubPgCount[i])+'-ref', mask=api.txtMask, limit=80, timeout=5)
                            sleep(sleepTimePerPage/2)
                        sleep(sleepTimePerPage)
                # ''' Teletext kapatilir '''
                api.sendKeys(['text+3*2'])
        except:
            api.printError()
        api.end(False)

def _subPageCount_TXT_3_1_5(pageNumber):
    try:
        return {
            '201': ['0001', '0002', '0003'], 
            '202': ['0001', '0002', '0003', '0004'], 
            '203': ['0001', '0002', '0003', '0004'], 
            '205': ['0001', '0002', '0003', '0004', '0005'], 
            '206': ['0001', '0002', '0003'], 
            '207': ['0001', '0002', '0003', '0004'], 
            '209': ['0001', '0002', '0003', '0004'], 
            '211': ['0001', '0002', '0003'], 
            '251': ['0001', '0002', '0003'], 
            '252': ['0001', '0002', '0003', '0004'], 
            '255': ['0001', '0002', '0003', '0004', '0005'], 
            '256': ['0001', '0002', '0003'], 
            '257': ['0001', '0002', '0003', '0004'], 
            '259': ['0001', '0002', '0003', '0004'], 
            '261': ['0001', '0002', '0003']
            }.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

def _multiReferans_TXT_3(pageNumber):
    try:
        return {'-1' : []}.get(pageNumber, []) # ''' Default olarak 0 dondurur. Bulunamazsa '''
    except:
        api.printError()

