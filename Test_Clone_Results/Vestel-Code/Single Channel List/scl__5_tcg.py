# Single Channel List Test Suite

from customTime import sleep

def test(api):
    try:
        Case01(api)	# ''' LIGHT CHANNEL LIST '''
        Case02(api)	# ''' ADVANCE CHANNEL LIST '''
        Case03(api)	# ''' ADVANCE CHANNEL LIST MULTIFAV FILTER '''
        Case04(api)	# ''' ADVANCE CHANNEL LIST FILTER '''
    except:
        api.printError()

def Case01(api): # LIGHT CHANNEL LIST 
    api.setTestCaseDescription('Init')
    api.setTestCaseName('Init')
    if not api.start():
        try:
            # ''' FTI yapiniz. '''
            api.doFTI(api)
            api.sendKeys(api.IMPORT_CHANNEL_LIST_FTI)
            api.updateTestResult('PASS')
        except:
            api.printError()
        api.end(False)
    Light_Chlist_Control(api)
    Light_Chlist_FilterControl1(api)
    Light_Chlist_FilterFavourite(api)
    Light_Chlist_FilterControl2(api)
    Light_Chlist_FilterControl3(api)
    Light_Chlist_FilterControl4(api)

def Case02(api): # ADVANCE CHANNEL LIST 
    Advance_Chlist_Watch(api)
    Advance_Chlist_Delete(api)
    Advance_Chlist_EditChannelName(api)
    Advance_Chlist_Lock(api)
    Advance_Chlist_Move(api)
    Advance_Chlist_TagUntagAll(api)
    Advance_Chlist_TagUntag(api)
    Advance_Chlist_Jump(api)

def Case03(api): # ADVANCE CHANNEL LIST MULTIFAV FILTER
    Advance_Chlist_MultiFav(api)
    Advance_Chlist_MultiFav_Filter_Network(api)
    Advance_Chlist_MultiFav_Filter_TV_Radio(api)
    Advance_Chlist_MultiFav_Filter_Free_CAS(api)
    Advance_Chlist_MultiFav_Filter_Sort(api)
    Advance_Chlist_MultiFav_Filter_HD_SD(api)
    Advance_Chlist_MultiFav_Filter_Satellite(api)
    Advance_Chlist_MultiFav_Filter_A_Z(api)
    Advance_Chlist_MultiFav_Filter_Combination(api)

def Case04(api): # ADVANCE CHANNEL LIST FILTER
    Advance_Chlist_Filter_Network(api)
    Advance_Chlist_Filter_TV_Radio(api)
    Advance_Chlist_Filter_Free_CAS(api)
    Advance_Chlist_Filter_Sort(api)
    Advance_Chlist_Filter_HD_SD(api)
    Advance_Chlist_Filter_Favourite(api)
    Advance_Chlist_Filter_SatelliteList(api)
    Advance_Chlist_Filter_A_Z(api)
    Advance_Chlist_Filter_Combination1(api)
    Advance_Chlist_Filter_Combination2(api)

def Light_Chlist_Control(api):
    api.setTestCaseName('Light_Chlist_Control')
    api.setTestCaseDescription('Light Channel List Control')
    if not api.start():
        try:
            chNo = api.getChannelNumber('ATV', 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' OK ile light kanal listesini aciniz. '''
            api.sendKeys(['ok+3'])
            api.testImages('pic01-ref', mask=api.lightChannelListMask, msg='Light kanal listesi acilmalidir.')
            # ''' Program Up yapiniz. '''
            api.sendKeys(['progup+3'])
            api.testImages('pic02-ref', mask=api.lightChannelListMask, msg='Sayfa ilerlemelidir/degismelidir.')
            # ''' Program Down yapiniz. '''
            api.sendKeys(['progdown+3'])
            api.testImages('pic03-ref', mask=api.lightChannelListMask, msg='Sayfa geriye gitmelidir/degismelidir.')
            # ''' Yukari navigasyon tusu ile kanal listesinde onceki kanallara gidiniz '''
            api.sendKeys(['up*5+3'])
            api.testImages('pic04-ref', mask=api.lightChannelListMask, msg='Daha onceki kanallarin isimleri kanal listesinde gorulmelidir. Navigasyon sirasinda bir problem olmamalidir.')
            api.testImages('blackScreen-ref', mask=api.blackScreenMask, expectMatch=False, msg='Goruntude bir problem olmamalidir.')
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(10, 0, 10), msg='Goruntude bir problem olmamalidir.')
            api.checkAudio(msg='Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.')
            # ''' Asagi navigasyon tusu ile kanal listesinde sonraki kanallara gidiniz '''
            api.sendKeys(['ok+3', 'down*7+3'])
            api.testImages('pic05-ref', mask=api.lightChannelListMask, msg='Daha sonraki kanallarin isimleri kanal listesinde gorulmelidir. Navigasyon sirasinda bir problem olmamalidir.')
            api.testImages('blackScreen-ref', mask=api.blackScreenMask, expectMatch=False, msg='Goruntude bir problem olmamalidir.')
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(10, 0, 10), msg='Goruntude bir problem olmamalidir.')
            api.checkAudio(msg='Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.')
            # ''' OK ile navigasyon ile gectiginiz kanalda izleme yapiniz. '''
            api.sendKeys(['ok+7', 'down*7+3', 'ok+7', 'info+1'])
            api.testImages('pic06-ref', mask=api.infoBarMask, msg='Kanala tune olundu.')
            api.testImages('blackScreen-ref', mask=api.blackScreenMask, expectMatch=False, msg='Izlemek icin kanal listesinden secilen kanal acilmalidir.')
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(5, 0, 5), msg='Izlemek icin kanal listesinden secilen kanalda goruntude bir problem olmamalidir.')
            api.checkAudio(msg='Izlemek icin kanal listesinden secilen kanalda seste bir problem olmamalidir.')
            # ''' OK ile light kanal listesini aciniz. '''
            api.sendKeys(['ok+3'])
            api.testImages('pic07-ref', mask=api.lightChannelListMask, msg='Light kanal listesini acildigi gorulmelidir.')
        except:
            api.printError()
        api.end(False)

def Light_Chlist_FilterControl1(api):
    api.setTestCaseName('Light_Chlist_FilterControl1')
    api.setTestCaseDescription('Light Channel List - Filter - Single 1')
    if not api.start():
        try:
            api.sendKeys(['1+10'])
            # ''' Filter aciniz. '''
            # ''' Network Type Satellite only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + ['+3'])
            api.testImages('SatalliteOnly-ref', mask=api.filterChannelListMask, msg='Network Type Satellite only secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            pageUpCnt = 0
            for i in range(1, 9):
                if i%3 != 0:
                    api.testImages('SatalliteOnly_pageUp'+str(pageUpCnt).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Kanal listesinde sadece Satellite kanallar gorunmelidir.')
                    api.sendKeys(['progup+0.5'])
                    pageUpCnt += 1
                else:
                    api.sendKeys(['progup+0.5*60'])
                    pageUpCnt += 60
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Network Type Digital Aerial only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY + ['+3'])
            api.testImages('DigitalAerialOnly-ref', mask=api.filterChannelListMask, msg='Network Type Digital Aerial only secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(4):
                api.testImages('DigitalAerialOnly_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede Sadece Aerial kanallar olmali')
                api.sendKeys(['progup+1'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Network Type Digital Cable only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_CABLE_ONLY + ['+3'])
            api.testImages('DigitalCableOnly-ref', mask=api.filterChannelListMask, msg='Network Type Cable only secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(4):
                api.testImages('DigitalCableOnly_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede Sadece Cable kanallar olmali')
                api.sendKeys(['progup+1'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Network Type Analogue seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_ANALOGUE_TV_ONLY + ['+3'])
            api.testImages('AnalogOnly-ref', mask=api.filterChannelListMask, msg='Network Type Analog only secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(1):
                api.testImages('AnalogOnly_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede Sadece Analog kanallar olmali')
                api.sendKeys(['progup+1'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz, Network Type secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_ALL + ['+3'])
            api.testImages('NetworkTypeAll-ref', mask=api.filterChannelListMask, msg='Network Type All secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            pageUpCnt = 0
            for i in range(1, 9):
                if i%3 != 0:
                    api.testImages('NetworkTypeAll_pageUp'+str(pageUpCnt).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Tum kanallar kanal listesinde gorunur olmalidir.(Analog, DVB-T, DVB-C, DVB-S-All satellites)')
                    api.sendKeys(['progup+0.5'])
                    pageUpCnt += 1
                else:
                    api.sendKeys(['progup+0.5*60'])
                    pageUpCnt += 60
            api.sendKeys(['back+2'])
            # ''' Filter aciniz. '''
            # ''' TV/Radio'dan Radio only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_RADIOONLY + ['+3'])
            api.testImages('RadioOnly-ref', mask=api.filterChannelListMask, msg='TV/Radio, Radio Only secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('RadioOnly_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede Sadece Radio kanallar olmali')
                api.sendKeys(['progup+0.5*6'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' TV/Radio'dan TV only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_TVONLY + ['+3'])
            api.testImages('TvOnly-ref', mask=api.filterChannelListMask, msg='TV/Radio, Tv Only secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('TvOnly_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede Sadece TV kanallar olmali')
                api.sendKeys(['progup+0.5*30'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz, TV/Radio secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.FILTER_CHLIST_TVRADIOALL + ['+3'])
            api.testImages('TvRadioAll-ref', mask=api.filterChannelListMask, msg='TV/Radio, Tv/Radio All secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('TvRadioAll_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede tum TV/Radyo kanallar olmali')
                api.sendKeys(['progup+0.5*30'])
            api.sendKeys(['back+2'])
            # ''' Filter aciniz. '''
            # ''' Free/CAS'tan Encrypted seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_ENCRYPTED + ['+3'])
            api.testImages('Encrypted-ref', mask=api.filterChannelListMask, msg='Free/CAS, Encrypted secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('Encrypted_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede sadece Encrypted kanallar olmali')
                api.sendKeys(['progup+0.5'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Free/CAS'tan Free seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_FREE + ['+3'])
            api.testImages('Free-ref', mask=api.filterChannelListMask, msg='Free/CAS, Free secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('Free_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Listede sadece Free kanallar olmali')
                api.sendKeys(['progup+0.5'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz, Free/CAS secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.FILTER_CHLIST_FREECAS_ALL + ['+3'])
            api.testImages('FreeCasAll-ref', mask=api.filterChannelListMask, msg='Free/CAS, All secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            pageUpCnt = 0
            for i in range(1, 9):
                if i%3 != 0:
                    api.testImages('FreeCasAll'+str(pageUpCnt).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Tum kanallar kanal listesinde gorunur olmalidir.(Free ve Encrypted)')
                    api.sendKeys(['progup+0.5'])
                    pageUpCnt += 1
                else:
                    api.sendKeys(['progup+0.5*60'])
                    pageUpCnt += 60
            api.sendKeys(['back+2'])
            # ''' Sort'tan Alphabetic seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_SORT_ALPH + ['+3'])
            api.testImages('Alphabetic-ref', mask=api.filterChannelListMask, msg='Sort, Alphabetic secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('Alphabetic_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Kanal listesi alfabetik siralanmis olmalidir.')
                api.sendKeys(['progup+0.5'])
            api.sendKeys(['back+2'])
            # ''' Filter aciniz. '''
            # ''' Sort'tan Numeric seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_SORT_NUM + ['+3'])
            api.testImages('Numeric-ref', mask=api.filterChannelListMask, msg='Sort, numeric secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('Numeric_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Kanal listesi numeric siralanmis olmalidir.')
                api.sendKeys(['progup+0.5'])
            api.sendKeys(['back+2'])
            # ''' Filter aciniz. '''
            # ''' HD/SD seciminden SD seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_HDSD_SD + ['+3'])
            api.testImages('SD-ref', mask=api.filterChannelListMask, msg='HDSD, SD secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('SD_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Kanal listesinde sadece SD kanallar olmalidir.')
                api.sendKeys(['progup+0.5'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' HD/SD seciminden HD seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_HDSD_HD + ['+3'])
            api.testImages('HD-ref', mask=api.filterChannelListMask, msg='HDSD, HD secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(5):
                api.testImages('HD_pageUp'+str(i).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Kanal listesinde sadece HD kanallar olmalidir.')
                api.sendKeys(['progup+0.5'])
            api.sendKeys(['back+2'])
            # ''' Tekrar Filter'i aciniz, HD/SD secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.FILTER_CHLIST_HDSD_ALL + ['+3'])
            api.testImages('HDSDAll-ref', mask=api.filterChannelListMask, msg='HDSD, HD secilmelidir.')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            pageUpCnt = 0
            for i in range(1, 9):
                if i%3 != 0:
                    api.testImages('HDSDAll'+str(pageUpCnt).rjust(3, '0')+'-ref', mask=api.lightChannelListMask, msg='Tum kanallar kanal listesinde gorunur olmalidir.(HD ve SD)')
                    api.sendKeys(['progup+0.5'])
                    pageUpCnt += 1
                else:
                    api.sendKeys(['progup+0.5*60'])
                    pageUpCnt += 60
            api.sendKeys(['back+2'])
        except:
            api.printError()
        api.end(False)

def Light_Chlist_FilterFavourite(api):
    api.setTestCaseName('Light_Chlist_FilterFavourite')
    api.setTestCaseDescription('Light Channel List - Filter - Favourite')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Kanal listesindeki ilk kanali Favourite 1 listesine '''
            api.sendKeys(api.EDIT_FAVOURITE + ['gofirstitem', 'right', 'exit2*2+3'])
            # ''' ikinci kanali Favourite 2 listesine, '''
            api.sendKeys(['progup'])
            api.sendKeys(api.EDIT_FAVOURITE+ ['down', 'gofirstitem', 'right', 'exit2*2+3'])
            # ''' ucuncu kanali Favourite 3 listesine, '''
            api.sendKeys(['progup'])
            api.sendKeys(api.EDIT_FAVOURITE+ ['down*2', 'gofirstitem', 'right', 'exit2*2+3'])
            # ''' dorduncu kanali ise Favourite4 listesine Q. Menuden atiniz. '''
            api.sendKeys(['progup'])
            api.sendKeys(api.EDIT_FAVOURITE+ ['down*3', 'gofirstitem', 'right', 'exit2*2+3'])
            # ''' Favourites seciminden Favourite list 4 seciniz ve kanal listesine geri donunuz '''
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST)
            api.testImages('picChList-ref', mask=api.advanceChannelListMask, msg='Favorite kanallar eklenmeli')
            api.sendKeys(api.FILTER_CHLIST_FAVOURITE_4)
            api.testImages('picFav4-ref', mask=api.lightChannelListMask, msg='Favorite List 4 secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic1-ref', mask=api.lightChannelListMask, msg='Listede Favorite List 4teki kanallar olmali')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Favourites seciminden Favourite list 2 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_FAVOURITE_2)
            api.testImages('picFav2-ref', mask=api.lightChannelListMask, msg='Favorite List 2 secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic2-ref', mask=api.lightChannelListMask, msg='Listede Favorite List 2deki kanallar olmali')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Favourites seciminden Favourite list 3 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_FAVOURITE_3)
            api.testImages('picFav3-ref', mask=api.lightChannelListMask, msg='Favorite List 3 secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic3-ref', mask=api.lightChannelListMask, msg='Listede Favorite List 3teki kanallar olmali')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Favourites seciminden Favourite list 1 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_FAVOURITE_1)
            api.testImages('picFav1-ref', mask=api.lightChannelListMask, msg='Favorite List 1 secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic4-ref', mask=api.lightChannelListMask, msg='Listede Favorite List 1deki kanallar olmali')
            # ''' Tekrar Filter'i aciniz, Favorites secenegini 'None' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.FILTER_CHLIST_FAVOURITE_NONE)
            api.testImages('picFavNone-ref', mask=api.lightChannelListMask, msg='Favorite List None secilmeli')
            api.sendKeys(['back+2'])
            for i in range(5, 12):
                api.testImages('pic'+str(i)+'-ref', mask=api.lightChannelListMask, msg='Listede tum kanallar olmali')
                api.sendKeys(['progup+1'])
            api.sendKeys(['exit2*2+2'])
            # ''' Birinci, ikinci, ucuncu ve dorduncu kanallari daha once set ettiginiz favourite listelerinden kaldiriniz.(Kanallarin hicbiri, herhangi bir favourite listesinde olmayacak) '''
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Kanal listesindeki ilk kanali Favourite 1 listesine '''
            api.sendKeys(api.EDIT_FAVOURITE + ['gofirstitem', 'exit2*2+3'])
            # ''' ikinci kanali Favourite 2 listesine, '''
            api.sendKeys(['progup'])
            api.sendKeys(api.EDIT_FAVOURITE+ ['down', 'gofirstitem', 'exit2*2+3'])
            # ''' ucuncu kanali Favourite 3 listesine, '''
            api.sendKeys(['progup'])
            api.sendKeys(api.EDIT_FAVOURITE+ ['down*2', 'gofirstitem', 'exit2*2+3'])
            # ''' dorduncu kanali ise Favourite 4 listesine Q. Menuden atiniz. '''
            api.sendKeys(['progup'])
            api.sendKeys(api.EDIT_FAVOURITE+ ['down*3', 'gofirstitem', 'exit2*2+3'])
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST)
            api.testImages('picChListLast-ref', mask=api.advanceChannelListMask, msg='Favourite kanallar silinmeli')
        except:
            api.printError()
        api.end(False)

def Light_Chlist_FilterControl2(api):
    api.setTestCaseName('Light_Chlist_FilterControl2')
    api.setTestCaseDescription('Light Channel List - Filter - Single 2')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Filter aciniz. '''
            # ''' Network Type Satellite only seciniz. '''
            # ''' Satellite List'ten Astra seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_ASTRA)
            api.testImages('picAstra-ref', mask=api.lightChannelListMask, msg='Satellite Only ve Astra secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic1-ref', mask=api.lightChannelListMask, msg='Listede Astra1 kanallari olmali')
            api.sendKeys(['clearosd+5'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Satellite List'ten Turksat seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_TURKSAT)
            api.testImages('picTurksat-ref', mask=api.lightChannelListMask, msg='Satellite Only ve Turksat secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic2-ref', mask=api.lightChannelListMask, msg='Listede Astra1 kanallari olmali')
            api.sendKeys(['clearosd+5'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Satellite List'ten Hotbird seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_HOTBIRD)
            api.testImages('picHotbird-ref', mask=api.lightChannelListMask, msg='Satellite Only ve Hotbird secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic3-ref', mask=api.lightChannelListMask, msg='Listede Astra1 kanallari olmali')
            api.sendKeys(['clearosd+5'])
            # ''' Tekrar Filter'i aciniz '''
            # ''' Satellite List'ten Eutelsat seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_EUTELSAT)
            api.testImages('picEutelsat-ref', mask=api.lightChannelListMask, msg='Satellite Only ve Eutelsat secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic4-ref', mask=api.lightChannelListMask, msg='Listede Astra1 kanallari olmali')
            api.sendKeys(['clearosd+5'])
            # ''' Tekrar Filter'i aciniz, 'Network Type:All', 'Satellite List:All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_ALL)
            api.testImages('picSatAll-ref', mask=api.lightChannelListMask, msg='Satellite Only ve ALL secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic5-ref', mask=api.lightChannelListMask, msg='Listede tum Satellite kanallari olmali')
            api.sendKeys(['clearosd+5'])
            # ''' Filter aciniz. '''
            # ''' A-Z filtresinden 'A' harfini seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_CHLIST_A_Z_A)
            api.testImages('picA-ref', mask=api.lightChannelListMask, msg='Alphabetic A secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic6-ref', mask=api.lightChannelListMask, msg='Listede A ile baslayan kanallar olmali')
            api.sendKeys(['clearosd+5'])
            # ''' Tekrar Filter'i aciniz, A-Z secenegini 'All'seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.FILTER_CHLIST_A_Z_ALL)
            api.testImages('picAlphAll-ref', mask=api.lightChannelListMask, msg='Alphabetic All secilmeli')
            api.sendKeys(['back+2'])
            api.testImages('pic7-ref', mask=api.lightChannelListMask, msg='Listede tum kanallar olmali')
            api.sendKeys(['clearosd+5'])
        except:
            api.printError()
        api.end(False)

def Light_Chlist_FilterControl3(api):
    api.setTestCaseName('Light_Chlist_FilterControl3')
    api.setTestCaseDescription('Light Channel List - Filter - Combination 1')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Filter aciniz. '''
            # ''' Network Type 'Satellite only' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_SATELLITE_ONLY)
            api.testImages('picSatOnly-ref', mask=api.filterChannelListMask, msg='Satellite Only secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece satellite kanallar bulunmalidir. '''
            for i in range(1, 8):
                api.testImages('pic'+str(i)+'-ref', mask=api.lightChannelListMask, msg='Listede Satellite kanallari olmali')
                api.sendKeys(['progup+1'])
            # ''' Tekrar Filter aciniz ve TV/Radio only'i 'TV' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue+1', 'down+1', 'gofirstitem+1', 'right+1'])
            api.testImages('picSATTVOnly-ref', mask=api.filterChannelListMask, msg='TV Only secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece satellite TV kanallari bulunmalidir. '''
            for i in range(8, 12):
                api.testImages('pic'+str(i)+'-ref', mask=api.lightChannelListMask, msg='Kanal listesinde sadece satellite TV kanallari bulunmalidir.')
                api.sendKeys(['progup+1'])
            # ''' Tekrar Filter aciniz ve Free/CAS'tan' Encrypted' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue+1', 'down+1*2', 'gofirstitem+1', 'right*2+1'])
            api.testImages('picSATTVEncOnly-ref', mask=api.filterChannelListMask, msg='Free/CAStan Encrypted secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece encrypted satellite TV kanallari bulunmalidir. '''
            api.testImages('pic12-ref', mask=api.lightChannelListMask, msg='Listede encrypted satellite TV kanallari olmali')
            # ''' Tekrar Filter aciniz ve HD/SD'yi 'HD' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue+1', 'down+1*5', 'gofirstitem+1', 'right+1*2'])
            api.testImages('picSATTVEncHDOnly-ref', mask=api.filterChannelListMask, msg=' HD/SDyi HD seciniz')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece encrypted satellite HD TV kanallari bulunmalidir. '''
            api.testImages('pic13-ref', mask=api.lightChannelListMask, msg='Encrypted satellite HD TV kanallari bulunmalidir')
            # ''' Tekrar Filter aciniz ve A-Z'den 'D' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue+1', 'down+1*3', 'gofirstitem+1', 'right+2*4'])
            api.testImages('picSATTVEncHDDOnly-ref', mask=api.filterChannelListMask, msg='A-Zden D secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'D' harfi ile baslayan encrypted satellite HD TV kanallari bulunmalidir. '''
            api.testImages('pic14-ref', mask=api.lightChannelListMask, msg='D harfi ile baslayan encrypted satellite HD TV kanallari bulunmalidir.')
            # ''' Tekrar Filter aciniz ve Sort'tan Alphabetic seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue+1', 'down+1*4', 'gofirstitem+2', 'right+2'])
            api.testImages('picSATTVEncHDDAlphOnly-ref', mask=api.filterChannelListMask, msg='Sort tan Alphabetic secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'D' harfi ile baslayan encrypted satellite HD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir. '''
            api.testImages('pic15-ref', mask=api.lightChannelListMask, msg='D harfi ile baslayan encrypted satellite HD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir.')
            # ''' Tekrar Filter aciniz ve Satellite List'ten 'Eutelsat' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue', 'down*7', 'gofirstitem+2', 'right+2'])
            api.testImages('picSATTVEncHDDAlphEutelOnly-ref', mask=api.filterChannelListMask, msg='Satellite Listten Eutelsat seciniz secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'D' harfi ile baslayan encrypted Eutelsat satellite HD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir. '''
            api.testImages('pic16-ref', mask=api.lightChannelListMask, msg='D harfi ile baslayan encrypted Eutelsat satellite HD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir.')
            # ''' Kanal listesinde filtrelenen kanallardan birini acarak izleyiniz ya da eger kanal listesi bossa kanal listesinden cikiniz. '''
            api.sendKeys(['ok+10', 'info+0.5'])
            api.testImages('pic17-ref', mask=api.infoBarMask, msg='Kanalda problem olmamali')
            sleep(7)
            # ''' Kanal listesini ve ardindan Filter aciniz. '''
            api.sendKeys(api.LIGHTCHLIST + ['blue+2'])
            # ''' Tekrar Filter acildiginda yapilan eski filtreleme saklanmamis olmalidir, default Filter secenekleri gorulmelidir. '''
            api.testImages('pic18-ref', mask=api.filterChannelListMask, msg='eski filtreleme saklanmamis olmalidir')
            # ''' Daha once filtreleme secenekleri kullanilarak filtrelenen kanallar degil tum kanallar listelenmelidir, filter default degerlere geri donmelidir.(Network type:All, TV/Radio:All, Free/CAS:All, A-Z:All, Sort:Numeric, HD/SD:All, Favourites:None) '''
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(19, 26):
                api.testImages('pic'+str(i)+'-ref', mask=api.lightChannelListMask, msg='Kanal listesinde tum kanallar bulunmalidir.')
                api.sendKeys(['progup+1'])
            api.sendKeys(['clearosd+5'])
        except:
            api.printError()
        api.end(False)

def Light_Chlist_FilterControl4(api):
    api.setTestCaseName('Light_Chlist_FilterControl4')
    api.setTestCaseDescription('Light Channel List - Filter - Combination 2')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Network Type 'Digital Aerial only' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.CHANNEL_LIST_FILTER_DIGITAL_AERIAL_ONLY)
            api.testImages('picSatOnly-ref', mask=api.filterChannelListMask, msg='Aerial Only secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece digital aerial kanallar bulunmalidir. '''
            for i in range(1, 3):
                api.testImages('pic'+str(i)+'-ref', mask=api.lightChannelListMask, msg='Listede Aerial kanallari olmali')
                api.sendKeys(['progup+1'])
            # ''' Tekrar Filter aciniz ve TV/Radio secenegini 'Radio' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(['blue+1', 'down+1', 'gofirstitem+1', 'right+1*2'])
            api.testImages('picAerRadOnly-ref', mask=api.filterChannelListMask, msg='Radio Only secilmeli')
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Eger yayinda varsa, kanal listesinde sadece digital aerial Radio kanallari bulunmalidir, eger yayinda yoksa, kanal listesinde kanalin bulunamadigina dair uyari olmalidir. '''
            api.testImages('pic3-ref', mask=api.lightChannelListMask, msg='Listede Aerial Radio kanallari olmali')
            # ''' Kanal listesinde filtrelenen kanallardan birini acarak izleyiniz ya da eger kanal listesi bossa kanal listesinden cikiniz. '''
            api.sendKeys(['ok+10', 'info+0.5'])
            api.testImages('pic4-ref', mask=api.infoBarMask, msg='Kanalda problem olmamali')
            api.checkAudio(msg='Mevcut radyo kanalinin sesinde bir problem olmamalidir.')
            # ''' Kanal listesini ve ardindan Filter aciniz. '''
            api.sendKeys(api.LIGHTCHLIST + ['blue+2'])
            # ''' Tekrar Filter acildiginda yapilan eski filtreleme saklanmamis olmalidir, default Filter secenekleri gorulmelidir. '''
            api.testImages('pic5-ref', mask=api.filterChannelListMask, msg='eski filtreleme saklanmamis olmalidir')
            # ''' Daha once filtreleme secenekleri kullanilarak filtrelenen kanallar degil tum kanallar listelenmelidir, filter default degerlere geri donmelidir.(Network type:All, TV/Radio:All, Free/CAS:All, A-Z:All, Sort:Numeric, HD/SD:All, Favourites:None) '''
            api.sendKeys(['back+2'] + api.GOFIRSTCHANNELOFLIST)
            for i in range(6, 13):
                api.testImages('pic'+str(i)+'-ref', mask=api.lightChannelListMask, msg='Kanal listesinde tum kanallar bulunmalidir.')
                api.sendKeys(['progup+1'])
            # ''' Advanced Channel List'e gecis yapiniz. (light kanal listesinde iken, bu gecis icin atanmis kisayol renk tusu ile) '''
            api.sendKeys(['green+2'])
            api.testImages('pic13-ref', mask=api.advanceChannelListMask, msg='Advanced kanal listesi acilmalidir.')
            # ''' Exit(cikis) icin atanmis tusa basarak channel list'ten cikiniz. '''
            api.sendKeys(['exit2+7', 'info+0.5'])
            # ''' Channel list dialog'undan cikip mevcut kanala geri donmelidir, kanalda ses ve goruntude bir problem olmamalidir. '''
            api.testImages('pic14-ref', mask=api.lightChannelListMask, msg='Light kanal listesine geri donus olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Watch(api):
    api.setTestCaseName('Advance_Chlist_Watch')
    api.setTestCaseDescription('Advance Channel List - Watch')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Ana menuden advanced kanal listesini aciniz. '''
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Ana menuden advanced kanal listesini acilmalidir.')
            # ''' Program Up yapiniz. '''
            api.sendKeys(['progup+1*8'])
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg='Sayfa ilerlemelidir/degismelidir.')
            # ''' Program Down yapiniz. '''
            api.sendKeys(['progdown+1*4'])
            api.testImages('pic2-ref', mask=api.advanceChannelListMask, msg='Sayfa geriye gitmelidir/degismelidir.')
            # ''' Yukari navigasyon tusu ile kanal listesinde onceki kanallara gidiniz '''
            api.sendKeys(['up+1*5'])
            # ''' Daha onceki kanallarin isimleri kanal listesinde gorulmelidir. Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.Navigasyon sirasinda bir problem olmamalidir. '''
            api.testImages('pic3-ref', mask=api.advanceChannelListMask, msg='Navigasyon sirasinda bir problem olmamalidir.')
            api.testImages('blackScreen-ref', mask=api.blackScreenMask, expectMatch=False, msg='Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            # ''' Asagi navigasyon tusu ile kanal listesinde sonraki kanallara gidiniz '''
            # ''' Daha sonraki kanallarin isimleri kanal listesinde gorulmelidir. Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.Navigasyon sirasinda bir problem olmamalidir. '''
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST + ['down+1*8'])
            api.testImages('pic4-ref', mask=api.advanceChannelListMask, msg='Navigasyon sirasinda bir problem olmamalidir.')
            api.testImages('blackScreen-ref', mask=api.blackScreenMask, expectMatch=False, msg='Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.')
            api.checkAudio(msg='Seste bir problem olmamalidir.')
            # ''' Options-Watch ile navigasyon ile gectiginiz kanalda izleme yapiniz. '''
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST + ['down+1', 'ok+1*4', 'clearosd+10', 'info+0.5'])
            api.testImages('picf-ref', mask=api.infoBarMask, msg='Navigasyon sirasinda bir problem olmamalidir.')
            # ''' Izlemek icin kanal listesinden secilen kanalda ses ve goruntude bir problem olmamalidir. '''
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(10, 0, 10), msg='Mevcut kanalin goruntusunde bir problem olmamalidir.')
            api.checkAudio(msg='Mevcut kanalin sesinde bir problem olmamalidir.')
            # ''' Advanced kanal listesini aciniz. '''
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys(['clearosd+5'])
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Delete(api):
    api.setTestCaseName('Advance_Chlist_Delete')
    api.setTestCaseDescription('Advance Channel List - Channel Delete/Move')
    if not api.start():
        try:
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo = api.getChannelNumber(api.deleteChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            # ''' Kanali listenin ortasina al '''
            api.sendKeys(api.ADVANCECHLIST_MENU + ['up+1*5', 'down+1*5'])
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Kanal listesinin ortasinda bulunan kanali Options-Delete ile siliniz. '''
            # ''' Kanal silinmelidir, silinen kanalin yerine asagida bulunan diger kanallar sayisal olarak da sirayla birer yukari tasinmalidir. '''
            api.sendKeys(api.ADD_CHEDIT_DEL + ['ok+4'])
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg='Kanal silinmelidir, silinen kanalin yerine asagida bulunan diger kanallar sayisal olarak da sirayla birer yukari tasinmalidir.')
            # ''' Kanal listesindeki bir kanali kendi broadcast blogu icerisinde silinen kanal yerine Options-Move ile tasiyiniz. '''
            # ''' Kanal belirtilen siraya tasinmalidir. '''
            chNoMove = api.getChannelNumber(api.moveChannelName, 1)
            api.sendKeys([str(chNoMove)+'+2'] + api.ADD_CHEDIT_MOVE + ['1256+2', 'ok+2*2+5'])
            api.testImages('pic2-ref', mask=api.advanceChannelListMask, msg='Kanal belirtilen siraya tasinmalidir.')
            # ''' Kanal listesindeki bir kanalda iken Options-Delete seciniz. Silinme sorgusunu hayir olarak seciniz. '''
            # ''' Kanal listesine geri donmelidir. Kanal silinmemelidir. '''
            api.sendKeys(api.ADD_CHEDIT_DEL + ['right+0.5'])
            api.testImages('pic3-ref', mask=api.advanceChannelListMask, msg='Kanal listesindeki bir kanalda iken Options-Delete seciniz. Silinme sorgusunu hayir olarak seciniz.')
            api.sendKeys(['ok+1'])
            api.testImages('pic4-ref', mask=api.advanceChannelListMask, msg='Kanal listesine geri donmelidir. Kanal silinmemelidir.')
            api.sendKeys(['exit2*2+10', 'info+0.5'])
            # ''' Daha onceki kanallarin isimleri kanal listesinde gorulmelidir. Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.Navigasyon sirasinda bir problem olmamalidir. '''
            api.testImages('pic5-ref', mask=api.infoBarMask, msg='Navigasyon sirasinda bir problem olmamalidir.')
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(10, 0, 10), msg='Mevcut kanalin goruntusunde bir problem olmamalidir.')
            api.checkAudio(msg='Mevcut kanalin sesinde bir problem olmamalidir.')
            api.sendKeys(api.IMPORT_CHANNEL_LIST)	# ''' Kanal listesini tekrar import et. '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_EditChannelName(api):
    api.setTestCaseName('Advance_Chlist_EditChannelName')
    api.setTestCaseDescription('Advance Channel List - Edit Channel Name')
    if not api.start():
        try:
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo = api.getChannelNumber(api.moveChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Kanal listesindeki bir kanalin ismini Options-Edit name ile, +!). olarak degisitiriniz ve OK ile confirm edip kontrol ediniz. '''
            api.sendKeys(api.ADD_CHEDIT_EDIT + ['1*3', 'right', '1*6', 'right', '1*9', 'right', '1*8', 'down'] + [(['right', '0*2'], '*3')] + ['ok+5'])
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg='Kanalin ismi, +!) olarak degismis olmalidir.')
            # ''' Kanal listesindeki bir kanalin ismini Options-Edit name ile 32 karakter girecek sekilde degistiriniz ve OK ile confirm edip kontrol ediniz. '''
            api.sendKeys(api.ADD_CHEDIT_EDIT)
            for i in range(1, 33):
                api.sendKeys([str(i % 10), 'right'])
            api.testImages('pic2-ref', mask=api.advanceChannelListMask, limit=100, msg='32 karekter girilebilmeli, kanal listesinde yapilan degisiklik gorulmelidir.')
            api.sendKeys(['ok+5'])
            api.testImages('pic3-ref', mask=api.advanceChannelListMask, limit=100, msg='32 karekter girilebilmeli, kanal listesinde yapilan degisiklik gorulmelidir.')
            # ''' Kanal listesindeki bir kanalin ismini Options-Edit name ile 33 karakter girecek sekilde degistiriniz. '''
            api.sendKeys(api.ADD_CHEDIT_EDIT)
            # ''' 33 karekter girilememelidir, en fazla 32 karekter girilebilir. '''
            for i in range(1, 34):
                api.sendKeys([str(i % 10), 'right'])
            api.testImages('pic4-ref', mask=api.advanceChannelListMask, limit=100, msg='32 karekter girilebilmeli, kanal listesinde yapilan degisiklik gorulmelidir.')
            api.sendKeys(['ok+5'])
            api.testImages('pic5-ref', mask=api.advanceChannelListMask, limit=100, msg='Girilen 33. karekteri 32. karekterin uzerine yazmali yine en fazla 32 karekter olmalidir.')
            # ''' Kanal listesindeki bir kanalda iken Options-Edit name seciniz. Edit name dialogu varken Back ile kanal listesine donunuz. '''
            api.sendKeys(api.ADD_CHEDIT_EDIT + ['back+2'])
            api.testImages('pic6-ref', mask=api.advanceChannelListMask, msg='Kanal listesine geri donmelidir.')
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Lock(api):
    api.setTestCaseName('Advance_Chlist_Lock')
    api.setTestCaseDescription('Advance Channel List - Lock Channel')
    if not api.start():
        try:
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Kanal listesindeki en basta bulunan iki kanali Options-Lock/Unlock ile kilitleyiniz. '''
            # ''' Enter PIN sorgusu cikmalidir. '''
            api.sendKeys(api.ADD_CHEDIT_LOCKUNLOCK + [api.lockPassword + '+3'])	# Ilk kanal kilitleme
            api.sendKeys(['down+1'] + api.ADD_CHEDIT_LOCKUNLOCK)	# Ikinci kanal kilitleme
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg=api.lockPassword + ' sifresi girildikten sonra kanal listesinde kilitlenen kanalin satirinda Lock ikonu cikmalidir.')
            # ''' Kilitlediginiz ilk kanali Options-Watch ile izlemek icin aciniz, main speaker'i dinleyiniz. '''
            # ''' Kanalda ses ve goruntu olmamalidir, Enter PIN sorgusu ekrana gelmelidir, sifre '0000' girildikten sonra kanalda goruntu ve ses gelmelidir. '''
            api.sendKeys(['ok+1*2'])
            api.testImages('pic2-ref', mask=api.blackScreenMask, msg='Kanalda ses ve goruntu olmamalidir, Enter PIN sorgusu ekrana gelmelidir')
            api.checkAudio(msg='Enter pin ekraninda kanalin sesi olmamalidir.', expectMatch=False)
            api.sendKeys([api.lockPassword + '+5', 'ok*2+7'])
            # ''' Program Up/Down yaparak kilitli kanaldan baska bir kanala gecip tekrar kilitli kanala geliniz. '''
            # #, sifre '0000' girildikten sonra kanalda goruntu ve ses gelmelidir. '''
            api.sendKeys(['progup+1*3', 'progdown+1*3+10'])
            api.testImages('pic3-ref', mask=api.enterPINWithoutInfoBar, msg='Kanalda ses ve goruntu olmamalidir, Enter PIN sorgusu ekrana gelmelidir')
            api.checkAudio(msg='Enter pin ekraninda kanalin sesi olmamalidir.', expectMatch=False)
            api.sendKeys([api.lockPassword + '+3'])
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(10, 0, 10), msg='Goruntude bir problem olmamalidir.')
            api.checkAudio(msg='Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.')
            # ''' Advanced kanal listesini acarak kilitlediginiz 1. kanaldaki kilidi Options-Lock/Unlock ile kaldiriniz. '''
            api.sendKeys(api.ADVANCECHLIST_MENU + [str(chNo)+'+3'] + api.ADD_CHEDIT_LOCKUNLOCK + [api.lockPassword + '+3'])
            # ''' Kanal listesinde o kanal uzerindeki kilit ikonu kalkmalidir. '''
            api.testImages('pic4-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde o kanal uzerindeki kilit ikonu kalkmalidir.')
            # ''' Kilidini kaldirdiniz kanali Options-Watch ile izlemek icin aciniz. '''
            # ''' Kanalda goruntu ve ses alinmalidir. '''
            api.sendKeys(['ok+1*4+10', 'info+0.5'])
            api.testImages('pic5-ref', mask=api.infoBarMask, msg='Kanalda goruntu ve ses alinmalidir.')
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(10, 0, 10), msg='Goruntude bir problem olmamalidir.')
            api.checkAudio(msg='Mevcut kanalin goruntu ve sesinde bir problem olmamalidir.')
            # ''' Kanal listesindeki bir kanalda iken Options-Lock/Unlock seciniz. Enter PIN sorgusu varken Back ile kanal listesine donunuz. '''
            # ''' Kanal kilitlenmemelidir, Enter PIN sorgusu ekrandan kalkmalidir. '''
            api.sendKeys(api.ADVANCECHLIST_MENU + api.ADD_CHEDIT_LOCKUNLOCK)
            api.testImages('pic6-ref', mask=api.advanceChannelListMask, msg='Kanali kilitlemek icin pin sorgu ekrani gelmelidir.')
            api.sendKeys(['back+3'])
            api.testImages('pic7-ref', mask=api.advanceChannelListMask, msg='Kanal kilitlenmemelidir, Enter PIN sorgusu ekrandan kalkmalidir.')
            api.sendKeys(['clearosd+4'])
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Move(api):
    api.setTestCaseName('Advance_Chlist_Move')
    api.setTestCaseDescription('Advance Channel List - Move Channel')
    if not api.start():
        try:
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Kanal listesindeki 1 numarali kanali kendi broadcast blogu icerisindeki var olan bir kanalin bulundugu siraya Options-Move ile tasiyiniz. '''
            # ''' Kanal istenilen siraya tasinmalidir, orada var olan kanal da bir satir yukari kaymalidir.Tasindgi yerden onceki kanallar da birer satir yukari kaymalidir. '''
            api.sendKeys(api.ADD_CHEDIT_MOVE + ['8+3', 'ok+3'])
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg='Kanal istenilen siraya tasinmalidir')
            # ''' Kanal listesindeki 2 numarali kanali kendi broadcast blogu icerisinde olmayan bir numaraya Options-Move ile tasimaya calisiniz. '''
            # ''' Kanal tasinmamaldir, kendi broadcast blogunda yer almayan bir numaraya tasinmak istedigine dair uyari vermelidir. '''
            api.sendKeys(['2+5'] + api.ADD_CHEDIT_MOVE + ['3880+3', 'ok+2'])
            api.testImages('pic2-ref', mask=api.advanceChannelListMask, msg='Kendi broadcast blogunda yer almayan bir numaraya tasinmak istedigine dair uyari vermelidir.')
            # ''' Kanal listesindeki bir kanalda iken Options-Move aciniz. Yeni sira numarasi girilecek dialog varken Back ile kanal listesine donunuz. '''
            # ''' Kanal listesine geri donmelidir. '''
            api.sendKeys(api.ADD_CHEDIT_MOVE + ['back+4'])
            api.testImages('pic3-ref', mask=api.advanceChannelListMask, msg='Kanal listesine geri donmelidir.')
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_TagUntagAll(api):
    api.setTestCaseName('Advance_Chlist_TagUntagAll')
    api.setTestCaseDescription('Advance Channel List - Tag / Untag All Channel')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Tag/Untag all tusu ile tum kanallari isaretleyiniz. Options-Lock/Unlock ile tum kanallari kilitleyiniz. Enter PIN sorgusundan sonra tum kanallarin kilitlenmelidir, kanal listesinde tum kanallarin yaninda kilit ikonu cikmalidir. '''
            # ''' # Tag/Untag all tusu ile tum kanallari isaretleyiniz. Options-Lock/Unlock ile tum kanallarin kilidini kaldiriniz. '''
            # ''' Tag/Untag all tusu ile tum kanallari isaretleyiniz. Options-Delete ile tum kanallari siliniz. '''
            # ''' # Tum kanallari Export channel list ile geri yukleyiniz. Tum kanallar geri gelmelidir. '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_TagUntag(api):
    api.setTestCaseName('Advance_Chlist_TagUntag')
    api.setTestCaseDescription('Advance Channel List - Tag/Untag Channel')
    if not api.start():
        try:
            api.doFTI(api, countryName='UK')
            api.sendKeys(api.IMPORT_CHANNEL_LIST_FTI)
            chNo1 = api.getChannelNumber(api.DVBT_CHN1, 1)
            chNo2 = api.getChannelNumber(api.DVBT_CHN2, 2, getList = False)
            api.sendKeys([str(chNo1)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Tag/Untag tusu ile 2 farkli broadcast blogunda bulunan 4 kanal isaretleyiniz.(2 DVB-T, 2 DVB-C olabilir) '''
            api.sendKeys([str(chNo1)+'+3', 'yellow+1'])
            api.sendKeys([str(chNo2)+'+3', 'yellow+1', str(chNo1)+'+2'])
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg='Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretlenmelidir.')
            # ''' Isaretlenmis kanallari Options-Move secenegi ile kendi broadcast blogu icerisinde olmayan bir siraya tasimaya calisiniz.(Analog bloguna tasinmaya calisilabilir) '''
            api.sendKeys(api.ADD_CHEDIT_MOVE_MULTI + ['8+2', 'ok+5'])
            api.testImages('pic2-ref', mask=api.advanceChannelListMask, msg='Kanallarin ikiside tasinmalidir.')
            # ''' Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretleyiniz. '''
            chNo1 = api.getChannelNumber(api.DVBT_CHN1, 8)
            chNo2 = api.getChannelNumber(api.DVBT_CHN2, 9, getList = False)
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys([str(chNo1)+'+3', 'yellow+1'])
            api.sendKeys([str(chNo2)+'+3', 'yellow+1', str(chNo1)+'+2'])
            api.testImages('pic3-ref', mask=api.advanceChannelListMask, msg='Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretlenmelidir.')
            # ''' Isaretlenmis kanallari Options-Move secenegi ile kendi broadcast blogu icerisinde ve girilen sayi o broadcast blogunda son kanalin bulundugu sira olacak sekilde bir siraya tasimaya calisiniz. '''
            api.sendKeys(api.ADD_CHEDIT_MOVE_MULTI + ['1033+3', 'ok+5'])
            api.testImages('pic4-ref', mask=api.advanceChannelListMask, msg='Kanallar tasinmamalidir.')
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo1 = api.getChannelNumber(api.DVBT_CHN1, 1)
            chNo2 = api.getChannelNumber(api.DVBT_CHN2, 2, getList = False)
            chNo3 = api.getChannelNumber(api.DVBC_CHN1, 1101, getList = False)
            chNo4 = api.getChannelNumber(api.DVBC_CHN2, 1102, getList = False)
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys([str(chNo1)+'+3', 'yellow+1'])
            api.sendKeys([str(chNo2)+'+3', 'yellow+1', str(chNo1)+'+2'])
            api.testImages('pic5-ref', mask=api.advanceChannelListMask, msg='Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretlenmelidir.')
            api.sendKeys([str(chNo3)+'+3', 'yellow+1'])
            api.sendKeys([str(chNo4)+'+3', 'yellow+1', str(chNo3)+'+2'])
            api.testImages('pic6-ref', mask=api.advanceChannelListMask, msg='Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretlenmelidir.')
            api.sendKeys(api.ADD_CHEDIT_MOVE_MULTI + ['903+1', 'ok+3'])
            api.testImages('pic7-ref', mask=api.advanceChannelListMask, msg='Kanallar tasinmamalidir.')
            # ''' Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretleyiniz. '''
            # ''' Options-Lock/Unlock ile isaretlenen kanallari kilitleyiniz. '''
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo1 = api.getChannelNumber(api.DVBT_CHN1, 1)
            chNo2 = api.getChannelNumber(api.DVBT_CHN2, 2, getList = False)
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys([str(chNo1)+'+2', 'yellow+1'])
            api.sendKeys([str(chNo2)+'+2', 'yellow+1', str(chNo1)+'+2'])
            api.testImages('pic5-ref', mask=api.advanceChannelListMask, msg='Tag/Untag tusu ile ayni broadcast blogu icerisinde 2 kanal isaretlenmelidir.')
            api.sendKeys(api.ADV_CHLIST_LOCKUNLOCKALLCHANNEL + [str(api.lockPassword)+'+3'])
            api.testImages('pic8-ref', mask=api.advanceChannelListMask, msg='Options-Lock/Unlock ile isaretlenen kanallari kilitleyiniz.')
            # ''' Tag/Untag tusu ile kilitli olan kanallari isaretleyiniz. '''
            # ''' Options-Lock/Unlock ile isaretlenen kanallardaki kilidi kaldiriniz. '''
            # ''' Isaretli olan kanallarda kilit ikonu artik gorulmemelidir. '''
            chNo1 = api.getChannelNumber(api.DVBT_CHN1, 1, getList = False)
            chNo2 = api.getChannelNumber(api.DVBT_CHN2, 2, getList = False)
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys([str(chNo1)+'+2', 'yellow+1'])
            api.sendKeys([str(chNo2)+'+2', 'yellow+1', str(chNo1)+'+2'])
            api.sendKeys(api.ADV_CHLIST_LOCKUNLOCKALLCHANNEL + [str(api.lockPassword)+'+2'])
            api.testImages('pic9-ref', mask=api.advanceChannelListMask, msg='Isaretli olan kanallarda kilit ikonu artik gorulmemelidir.')
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo1 = api.getChannelNumber(api.DVBT_CHN1, 1)
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys([str(chNo1)+'+2'] + [(['yellow+1', 'down+1'], '*5')] + ['up+1'] + api.ADD_FAV1_SELECTEDCHANNELS)
            api.testImages('pic10-ref', mask=api.advanceChannelListMask, msg='Ilk 5 kanal Fav1 listesine kaydedilmelidir.')
            api.sendKeys(api.QUICKMENU_SELECT_FAVLIST + ['right+2'])
            api.testImages('pic11-ref', mask=api.quickMenuMask, msg='Quick menuden Fav List 1 secilmelidir.')
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.testImages('pic12-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde favorite set edilen kanallar gorulmelidir, kanallarin numaralarinda kayma olmamalidir.')
            api.sendKeys(api.QUICKMENU_SELECT_FAVLIST + ['left+2'])
            api.testImages('pic13-ref', mask=api.quickMenuMask, msg='Favorite List None set edilmelidir.')
            api.sendKeys(['back+1'])
            # ''' Tag/Untag tusu ile 2 kanal isaretleyiniz. '''
            # ''' Options-Delete ile isaretli kanallari siliniz.Isaretli kanallar kanal listesinden kalkmalidir, silinen kanallarin yerine asagidaki kanallar yukari tasinmalidir. '''
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.sendKeys(['1+3', 'yellow', 'down', 'yellow', 'ok+1', 'down', 'ok+2*2+5'])
            api.testImages('pic14-ref', mask=api.advanceChannelListMask, msg=' silinen kanallarin yerine asagidaki kanallar yukari tasinmalidir.')
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Jump(api):
    api.setTestCaseName('Advance_Chlist_Jump')
    api.setTestCaseDescription('Advance Channel List - Jump')
    if not api.start():
        try:
            api.sendKeys(api.IMPORT_CHANNEL_LIST)
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Kanal listesinde bulunan bir kanala gitmek icin digit tuslarini kullaniniz. (Orn;7. kanala gitmek icin 7'ye basiniz.) '''
            # ''' Digit ile girilen kanalin bulundugu siraya gitmelidir. '''
            api.sendKeys(['7+5'])
            api.testImages('pic1-ref', mask=api.advanceChannelListMask, msg='Digit ile girilen kanalin bulundugu siraya gitmelidir.')
            # ''' Digit tuslari ile kanal listesinde olmayan bir kanal numarasi giriniz. '''
            # ''' Girilen digit tusuna atanmis bir kanal olmadigindan girilen digit numarasina en yakin numarali kanalin bulundugu satira gitmelidir. '''
            api.sendKeys(['6000+5'])
            api.testImages('pic2-ref', mask=api.advanceChannelListMask, msg='girilen digit numarasina en yakin numarali kanalin bulundugu satira gitmelidir.')
            api.sendKeys(['clearosd+4'])
        except:
            api.printError()
        api.end(False)
 
def Advance_Chlist_MultiFav(api):
    api.setTestCaseName('Advance_Chlist_MultiFav')
    api.setTestCaseDescription('Advance Channel List - MultiFav')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Options-Add/Remove Favourites seciniz. Kanal listesinde highlight edilen kanali Favourite List1'e ekleyiniz ve kanal listesine geri donunuz. '''
            # ''' Advanced kanal listesinde iken Filter'dan Favourites'i Favourite 1 olarak seciniz. '''
            # ''' Kanal listesinden cikarak mevcut kanala geri donunuz ve kanalda iken OK ile Light channel list aciniz. '''
            # ''' Light kanal listesinden cikiniz ve Q.Menu'den Favourites'i None seciniz. Advanced kanal listesini kontrol ediniz. '''
            # ''' Advanced kanal listesinde Favourite1'e eklediginiz kanal highlight iken kanali Favourite List2'ye ekleyiniz ve kanal listesine geri donunuz. '''
            # ''' Advanced kanal listesinde Favourite1 ve Favourite2'ye eklediginiz kanal highlight iken kanali bu kez de Favourite List3'e ekleyiniz ve kanal listesine geri donunuz. Kanal listesinde Favourite3'e eklenen kanalda +1 ve +2 ikonunun solunda +3 ikonu cikmalidir. '''
            # ''' Advanced kanal listesinde Favourite1, Favourite2 ve Favourite3'e eklediginiz kanal highlight iken kanali bu kez de Favourite List4'e ekleyiniz ve kanal listesine geri donunuz. '''
            # ''' Tag/Untag channel ile 3. ve 4. kanallari List3 ve List4 favourite listelerine ekleyiniz ve kanal listesine geri donunuz. '''
            # ''' Advanced kanal listesinde iken Filter'dan Favourites'i Favourite 4 olarak seciniz. '''
            # ''' Kanal listesinden cikarak mevcut kanala geri donunuz P+/- ile kanal degistiriniz. '''
            # ''' Kanal listesinden cikarak mevcut kanala geri donunuz ve kanalda iken OK ile Light channel list aciniz. '''
            # ''' Light kanal listesinden cikiniz ve Q.Menu'den Favourites'i None seciniz. Advanced kanal listesini kontrol ediniz. '''
            # ''' Tag/Untag All ile kanal listesindeki tum kanallari isaretleyiniz ve Add/Remove Favourites'ten List2'yi kapatiniz. '''
            # ''' Tag/Untag All ile kanal listesindeki tum kanallari isaretleyiniz ve tum isaretli kanallari Add/Remove Favourites'ten List2'ye ekleyiniz. '''
            # ''' Advanced kanal listesinde iken Filter'dan Favourites'i Favourite 4 olarak seciniz. '''
            # ''' Kanal listesinden cikarak mevcut kanala geri donunuz ve tekrar advanced kanal listesini aciniz. Advanced kanal listesinde OK-Add/Remove Favourites ile Favourite kanal listesini acarak +4 olan tum kanallardaki favourite 4'leri kaldiriniz. '''
            # ''' Exit ile dialogu kapayip kanala geri donunuz ve mevcut kanalda advanced kanal listesi aciniz. '''
            # ''' Q.Menuden Favourites satirini kontrol ediniz. Q.Menuden Favourites satirini Favourite4 set etmeye calisiniz. '''
            # ''' Mevcut kanala geri donunuz ve tekrar Q.Menu acip bu kez favourites satirini Favourites2 seciniz, Light kanal listesi acarak kanallari kontrol ediniz. '''
            # ''' Q.Menuden Favourites satirini 'None' seciniz, Light kanal listesi acarak kanallari kontrol ediniz. '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_Network(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_Network')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter Network')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Kanal listesindeki tum kanallari Favourite1, Favourite2, Favourite3 ve Favourite4 listesinde gorunecek sekilde Add/Remove Favourites'ten ayarlayiniz. '''
            # ''' Advanced kanal listesinde iken filter aciniz. Network Type Satellite only seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Satellite kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Network Type Digital Aerial only seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Digital Aerial kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Network Type Digital Cable only seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Digital Cable kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Network Type Analogue seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Analog kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz, Network Type secenegini'All' seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' Tum kanallar 4 favori listesinde de gorunur olmalidir.(Analog, DVB-T, DVB-C, DVB-S-All satellites) '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_TV_Radio(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_TV_Radio')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter TV/Radio')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. TV/Radio'dan Radio only seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Radio kanallari gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz '''
            # ''' TV/Radio'dan TV only seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. 4 Favori listesinde de sadece TV kanallari gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz, TV/Radio secenegini 'All' seciniz TV/Radio'dan Radio only seciniz ve filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' Tum kanallar 4 favori listesinde de gorunur olmalidir.(TV, Radio ve Text) '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_Free_CAS(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_Free_CAS')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter Free/CAS')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. Free/CAS'tan Encrypted seciniz, yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Encrypted kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Free/CAS'tan Free seciniz, yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Free kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz, Free/CAS secenegini 'All' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' Tum kanallar 4 favori listesinde de gorunur olmalidir.(Free ve CAS) '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_Sort(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_Sort')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter Sort')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. Sort'tan Numeric seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesi de numeric siralanmis olmalidir. '''
            # ''' Sort'tan Alphabetic seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesi de alphabetic siralanmis olmalidir. '''
            # ''' Tekrar Filter'i aciniz, Sort secenegini 'numeric' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de tum kanallar numerik sirali olmalidir. '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_HD_SD(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_HD_SD')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter HD/SD')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. HD/SD seciminden SD seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece SD kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. HD/SD seciminden HD seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece HD kanallar gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz, HD/SD secenegini 'All' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' Tum kanallar 4 Favori listesinde de gorunur olmalidir.(HD ve SD) '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_A_Z(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_A_Z')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter A/Z')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. A-Z filtresinden 'A' harfini seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece 'A' harfi ile baslayan kanallar gosterilmelidir. '''
            # ''' Tekrar Filter'i aciniz, A-Z secenegini 'All' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' Kanallarin hepsi 4 favori listesinde de gorunmelidir.(Harf ayrimi olmaksizin) '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_Satellite(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_Satellite')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter Satellite')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. Network Type Satellite only seciniz. Filter secenekleri arasinda 'Satellite List' secenegi gorulmelidir. Satellite List'ten Astra seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Astra kanallari gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Satellite List'ten Turksat seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Turksat kanallari gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Satellite List'ten Hotbird seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Hotbird kanallari gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz. Satellite List'ten Eutelsat seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece Eutelsat kanallari gorunmelidir. '''
            # ''' Tekrar Filter'i aciniz, Satellite List secenegini 'All' seciniz ve kanal listesine geri donunuz, 4 favori listesini kontrol ediniz. '''
            # ''' Tum kanallar 4 favori listesinde de gorunur olmalidir.(Tum satellite'lar) '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_MultiFav_Filter_Combination(api):
    api.setTestCaseName('Advance_Chlist_MultiFav_Filter_Combination')
    api.setTestCaseDescription('Advance Channel List - MultiFav Filter Combination 1')
    if not api.start():
        try:
            api.updateTestResult('MANUAL')
            # ''' Advanced kanal listesinde iken filter aciniz. Network Type 'Satellite only' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece satellite kanallar bulunmalidir. '''
            # ''' Tekrar Filter aciniz ve TV/Radio only'i 'TV' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece satellite TV kanallari bulunmalidir. '''
            # ''' Tekrar Filter aciniz ve Free/CAS'tan' Encrypted' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece encrypted satellite TV kanallari bulunmalidir. '''
            # ''' Tekrar Filter aciniz ve HD/SD'yi 'HD' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece encrypted satellite HD TV kanallari bulunmalidir. '''
            # ''' Tekrar Filter aciniz ve A-Z'den 'D' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece 'D' harfi ile baslayan encrypted satellite HD TV kanallari bulunmalidir. '''
            # ''' Tekrar Filter aciniz ve Sort'tan Alphabetic seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' Kanal listesinde sadece 'D' harfi ile baslayan encrypted satellite HD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir. '''
            # ''' Tekrar Filter aciniz ve Satellite List'ten 'Eutelsat' seciniz ve yine filter'dan 4 favourite listi de tek tek secerek advanced kanal listesini kontrol ediniz. '''
            # ''' 4 Favori listesinde de sadece 'D' harfi ile baslayan encrypted Eutelsat satellite HD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir. '''
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_Network(api):
    api.setTestCaseName('Advance_Chlist_Filter_Network')
    api.setTestCaseDescription('Advance Channel List - Filter - Network')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' Network Type Satellite only seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + ['back+5'])
            # ''' Kanal listesinde sadece Satellite kanallar gorunmelidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece Satellite kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Network Type Digital Aerial only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_DIGITAL_AERIAL_ONLY + ['back+5'])
            # ''' Kanal listesinde sadece Digital Aerial kanallar gorunmelidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece Digital Aerial kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Network Type Digital Cable only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_DIGITAL_CABLE_ONLY + ['back+5'])
            # ''' Kanal listesinde sadece Digital Cable kanallar gorunmelidir. '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece Digital Cable kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Network Type Analogue seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_ANALOGUE_TV_ONLY + ['back+5'])
            # ''' Kanal listesinde sadece Analog kanallar gorunmelidir. '''
            api.testImages('pic04-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece Analog kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz, Network Type secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_ALL + ['back+5'])
            # ''' Tum kanallar kanal listesinde gorunur olmalidir.(Analog, DVB-T, DVB-C, DVB-S-All satellites) '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_TV_Radio(api):
    api.setTestCaseName('Advance_Chlist_Filter_TV_Radio')
    api.setTestCaseDescription('Advance Channel List - Filter - TV/Radio')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' TV/Radio'dan Radio only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_RADIOONLY + ['back+5'])
            # ''' Kanal listesinde sadece Radio kanallari gorunmelidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece radio kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' TV/Radio'dan TV only seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_TVONLY + ['back+5'])
            # ''' Kanal listesinde sadece TV kanallari gorunmelidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece tv kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz, TV/Radio secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_TVRADIOALL + ['back+5'])
            # ''' Tum kanallar kanal listesinde gorunur olmalidir.(TV, Radio ve Text) '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_Free_CAS(api):
    api.setTestCaseName('Advance_Chlist_Filter_Free_CAS')
    api.setTestCaseDescription('Advance Channel List - Filter - Free/CAS')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' Free/CAS'tan Encrypted seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_ENCRYPTED + ['back+5'])
            # ''' Kanal listesinde sadece Encrypted kanallar gorunmelidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece Encrypted kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Free/CAS'tan Free seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_FREE + ['back+5'])
            # ''' Kanal listesinde sadece Free kanallar gorunmelidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece Free kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz, Free/CAS secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_FREECAS_ALL + ['back+5'])
            # ''' Tum kanallar kanal listesinde gorunur olmalidir.(Free ve CAS) '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_Sort(api):
    api.setTestCaseName('Advance_Chlist_Filter_Sort')
    api.setTestCaseDescription('Advance Channel List - Filter - Sort')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' Sort'tan Numeric seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SORT_NUM + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesi numeric siralanmis olmalidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Tum kanallar numerik sirali olmalidir.')
            # ''' Sort'tan Alphabetic seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SORT_ALPH + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesi alphabetic siralanmis olmalidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Tum kanallar alphabetic sirali olmalidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Tekrar Filter'i aciniz ve Sort secenegini 'numeric' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SORT_NUM + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Tum kanallar numerik sirali olmalidir. '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Tum kanallar numerik sirali olmalidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_HD_SD(api):
    api.setTestCaseName('Advance_Chlist_Filter_HD_SD')
    api.setTestCaseDescription('Advance Channel List - Filter - HD/SD')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' HD/SD seciminden SD seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_HDSD_SD + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece SD kanallar gorunmelidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece SD kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' HD/SD seciminden HD seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_HDSD_HD + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece HD kanallar gorunmelidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece HD kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz, HD/SD secenegini 'All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_HDSD_ALL + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Tum kanallar kanal listesinde gorunur olmalidir.(HD ve SD) '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde sadece tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_Favourite(api):
    api.setTestCaseName('Advance_Chlist_Filter_Favourite')
    api.setTestCaseDescription('Advance Channel List - Filter - Favorite')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' Favourites seciminden Favourite list 4 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_FAVOURITE_4 + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Favourite List 4'e eklene kanallar gorunmelidir. Favourite List 4 bos ise kanal listesinde kanal olmamalidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Favourite List 4 bos ise kanal listesinde kanal olmamalidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Favourites seciminden Favourite list 2 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_FAVOURITE_2 + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Favourite List 2'ye eklene kanallar gorunmelidir. Favourite List 2 bos ise kanal listesinde kanal olmamalidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Favourite List 2 bos ise kanal listesinde kanal olmamalidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Favourites seciminden Favourite list 3 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_FAVOURITE_3 + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Favourite List 3'e eklene kanallar gorunmelidir. Favourite List 3 bos ise kanal listesinde kanal olmamalidir. '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Favourite List 3 bos ise kanal listesinde kanal olmamalidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Favourites seciminden Favourite list 1 seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.FILTER_FAVOURITE_1 + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Favourite List 1'e eklene kanallar gorunmelidir. Favourite List 1 bos ise kanal listesinde kanal olmamalidir. '''
            api.testImages('pic04-ref', mask=api.advanceChannelListMask, msg='Favourite List 1 bos ise kanal listesinde kanal olmamalidir.')
            # ''' Tekrar Filter'i aciniz, Favorites secenegini 'None' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.FILTER_FAVOURITE_NONE + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Tum kanallar kanal listesinde gorunur olmalidir. '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_SatelliteList(api):
    api.setTestCaseName('Advance_Chlist_Filter_SatelliteList')
    api.setTestCaseDescription('Advance Channel List - Filter - Satellite List')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' Network Type Satellite only seciniz. '''
            # ''' Filter secenekleri arasinda 'Satellite List' secenegi gorulmelidir. '''
            # ''' Satellite List'ten Astra seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_ASTRA + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Astra kanallari gorunmelidir. '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde Astra kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Satellite List'ten Turksat seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_TURKSAT + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Turksat kanallari gorunmelidir. '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde Turksat kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Satellite List'ten Hotbird seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_HOTBIRD + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Hotbird kanallari gorunmelidir. '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde Hotbird kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz '''
            # ''' Satellite List'ten Eutelsat seciniz ve kanal listesine geri donunuz '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_EUTELSAT + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Eutelsat kanallari gorunmelidir. '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde Eutelsat kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz, 'Network Type:All', 'Satellite List:All' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.CLEAR_FILTER + api.GOFIRSTCHANNELOFLIST)
            # ''' Tum kanallar kanal listesinde gorunur olmalidir.(Tum satellite'lar) '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)
 
def Advance_Chlist_Filter_A_Z(api):
    api.setTestCaseName('Advance_Chlist_Filter_A_Z')
    api.setTestCaseDescription('Advance Channel List - Filter - A/Z')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz.
            # ''' A-Z filtresinden 'A' harfini seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_A_Z_A + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'A' harfi ile baslayan kanallar gosterilmelidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde A harfi ile baslayan kanallar gorunmelidir.')
            # ''' Tekrar Filter'i aciniz, 'Numeric' seciniz ve kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_A_Z_ALL + ['back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanallar kanal listesinde numeric siralanmis olmalidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde tum kanallar gorunmelidir.')
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_Combination1(api):
    api.setTestCaseName('Advance_Chlist_Filter_Combination1')
    api.setTestCaseDescription('Advance Channel List - Filter - Combination 1')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST + api.CLEAR_FILTER)
            api.sendKeys([str(chNo)+'+10'])
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Advanced kanal listesinde iken filter aciniz. '''
            # ''' Network Type 'Satellite only' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece satellite kanallar bulunmalidir. '''
            api.testImages('pic01-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde satellite kanallar gorunmelidir.')
            # ''' Tekrar Filter aciniz ve TV/Radio only'i 'TV' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_TVONLY + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece satellite TV kanallari bulunmalidir. '''
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde satellite TV kanallar gorunmelidir.')
            # ''' Tekrar Filter aciniz ve Free/CAS'tan'Free' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_FREE + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Free satellite TV kanallari bulunmalidir. '''
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde Free satellite TV kanallar gorunmelidir.')
            # ''' Tekrar Filter aciniz ve HD/SD'yi 'SD' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_HDSD_SD + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece Free satellite SD TV kanallari bulunmalidir. '''
            api.testImages('pic04-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde Free satellite SD TV kanallar gorunmelidir.')
            # ''' Tekrar Filter aciniz ve A-Z'den 'T' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_A_Z_T + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'T' harfi ile baslayan Free satellite SD TV kanallari bulunmalidir. '''
            api.testImages('pic05-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde T ile baslayan Free satellite SD TV kanallar gorunmelidir.')
            # ''' Tekrar Filter aciniz ve Sort'tan Alphabetic seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SORT_ALPH + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'T' harfi ile baslayan Free satellite SD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir. '''
            api.testImages('pic06-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde T ile baslayan Free satellite SD TV kanallar gorunmelidir alphabetic siralanmalidir.')
            # ''' Tekrar Filter aciniz ve Satellite List'ten 'Turksat' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_SATELLITE_ONLY + api.ADD_SATLIST_TURKSAT + ['+5', 'back+5'] + api.GOFIRSTCHANNELOFLIST)
            # ''' Kanal listesinde sadece 'T' harfi ile baslayan Free Turksat satellite SD TV kanallari bulunmalidir ve alphabetic siralanmis olmalidir. '''
            api.testImages('pic07-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde T ile baslayan Free Turksat satellite SD TV kanallar gorunmelidir alphabetic siralanmalidir.')
            # ''' Kanal listesinde filtrelenen kanallardan birini acarak izleyiniz ya da eger kanal listesi bossa kanal listesinden cikiniz. '''
            api.sendKeys(['ok+2*4+10'])
            # ''' Kanal listesini ve ardindan Filter aciniz. '''
            api.sendKeys(api.ADVANCECHLIST_MENU + ['blue+2'])
            # ''' Daha once filtreleme secenekleri kullanilarak filtrelenen kanallar gorulmelidir, yapilan filtreleme ayarlari saklanmalidir. '''
            api.testImages('pic08-ref', mask=api.advanceChannelListMask, msg='Yapilan filtreleme ayarlari saklanmalidir')
            api.sendKeys(['back'] + api.CLEAR_FILTER + ['clearosd+5'])
        except:
            api.printError()
        api.end(False)

def Advance_Chlist_Filter_Combination2(api):
    api.setTestCaseName('Advance_Chlist_Filter_Combination2')
    api.setTestCaseDescription('Advance Channel List - Filter - Combination 2')
    if not api.start():
        try:
            chNo = api.getChannelNumber(api.firstChannelName, 1)
            api.sendKeys([str(chNo)+'+10'])
            api.sendKeys(api.ADVANCECHLIST_MENU + api.CLEAR_FILTER)
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            api.testImages('picAdvChList-ref', mask=api.advanceChannelListMask, msg='Advance channel list acilmali')
            # ''' Network Type 'Digital Cable only' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            # ''' Kanal listesinde sadece digital cable only kanallar bulunmalidir. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_DIGITAL_CABLE_ONLY + ['back+2'] + api.GOFIRSTCHANNELOFLIST)
            api.testImages('pic02-ref', mask=api.advanceChannelListMask, msg='Kanal listesinde digital cable kanallar gorunmelidir.')
            # ''' Tekrar Filter aciniz ve TV/Radio secenegini 'Radio' seciniz ve filter'dan cikip kanal listesine geri donunuz. '''
            # ''' Eger yayinda varsa, kanal listesinde sadece digital aerial Radio kanallari bulunmalidir, eger yayinda yoksa, kanal listesinde kanalin bulunamadigina dair uyari olmalidir. '''
            api.sendKeys(api.ADV_CHLIST_FILTER_RADIOONLY + ['back+2'] + api.GOFIRSTCHANNELOFLIST)
            api.testImages('pic03-ref', mask=api.advanceChannelListMask, msg='Eger yayinda varsa, kanal listesinde sadece digital aerial Radio kanallari bulunmalidir, eger yayinda yoksa, kanal listesinde kanalin bulunamadigina dair uyari olmalidir.')
            # ''' Kanal listesinde filtrelenen kanallardan birini acarak izleyiniz ya da eger kanal listesi bossa kanal listesinden cikiniz. '''
            # ''' Power off/on yapiniz ve tekrar kanal listesini aciniz '''
            api.doPowerCycle(api)
            api.sendKeys(api.ADVANCECHLIST_MENU + api.GOFIRSTCHANNELOFLIST)
            # ''' Daha once filtreleme secenekleri kullanilarak filtrelenen kanallar gorulmelidir, yapilan filtreleme ayarlari saklanmalidir. '''
            api.testImages('pic04-ref', mask=api.advanceChannelListMask, msg='Daha once filtreleme secenekleri kullanilarak filtrelenen kanallar gorulmelidir')
            api.sendKeys(['blue+1'])
            api.testImages('pic05-ref', mask=api.filterChannelListMask, msg='Yapilan filtreleme ayarlari saklanmalidir.')
            # ''' Yapilan tum filtrelemeleri resetleyiniz. (Channel list ekraninda iken 'All' (kirmizi tus)) '''
            # ''' Tum filtreleme secenekleri default degerlerine geri donmelidir. '''
            api.sendKeys(['red+1'])
            api.testImages('pic06-ref', mask=api.filterChannelListMask, msg='Tum filtreleme secenekleri default degerlerine geri donmelidir.')
            # ''' Exit (cikis) icin atanmis tusa basarak channel list'ten cikiniz. '''
            api.sendKeys(['exit2+2*2', str(chNo)+'+10', 'info+0.5'])
            api.testImages('pic07-ref', mask=api.infoBarMask, msg='Tum filtreleme secenekleri default degerlerine geri donmelidir.')
            # ''' Channel list dialog'undan cikip mevcut kanala geri donmelidir, kanalda ses ve goruntude bir problem olmamalidir. '''
            api.videoAnalysis(duration=(30, 0, 30), tolerance=(5, 0, 5), msg='Izlemek icin kanal listesinden secilen kanalda goruntude bir problem olmamalidir.')
            api.checkAudio(msg='Izlemek icin kanal listesinden secilen kanalda seste bir problem olmamalidir.')
        except:
            api.printError()
        api.end(False)

