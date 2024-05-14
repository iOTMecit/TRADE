# DVT-T icin I-RF1"den gelen yayin baglanmalidir.
# USB Streaming, Record islemi ve "IMPORT CHANNELLIST" icin HDD veya FlashDisk baglanmalidir.
# TV Open internet"e baglanmalidir.

# COUNTRY: GERMANY
# Controls: testImages, checkAudio, videoAnalysis -> HarranBoard
# Live Signal: INT RF1
# USB Streaming: Terrestrial
# Internet: OP-INT (for Portal Test Cases)

# RNSController: Power & RC Keys
# UART: Sending Command, Reading Log
# External Memory (FAT32): USB Streaming (with stream files), PVR (Record), 'IMPORT CHANNELLIST'

# Commands: mheg_epg, RFSIGNALOFF, RFSIGNALON, SETCOUNTRY GERMANY

# Draft Profile:
    # PowerUpMode\PowerUpMode: Last State
    # ServiceListCloning\ServiceListCloning: Enabled
# Dev Profile:
    # USBStreamPlayerSupport->USBStreamPlayerSupport: Enabled

import os
from customTime import sleep
from dll_Manual import Manual

devConf = {
    'uartport': [9],
    'rnsport': [1],
    'keysenddelay': 0.5,
    # 'ethip': ['10.108.83.141'],
    # 'rrnumber': 1,
    # 'rnskeylist': ['rc5_tv'],
    # 'rrkeylist': ['RC_5117'],
    'keysenderdevice': 'UART'
    }

auto_getReportID = 1            # Otomatik reportID alinmasi icin 1 giriniz. reportID: 0 olmali
auto_readTVInfo = 1             # TV/STB bilgilerinin otomatik okunmasi icin 1 giriniz
test_Devices = 1                # Teste baslarken duzgun capture alinip alinmadigini kontrol etmek icin 1 giriniz
webMonitorUserName = 'yasinon'  # WebMonitor kullanici adinizi giriniz. Orn; 'yasinon', 'hadi', 'melihm', 'umutb', 'mustafade', 'irfanc', ...

# ''' reportID > 0 ise auto_getReportID ozelligi calismaz, belirtilen reportID'yi kullanir '''
# ''' projectName, hardwareName, SWVersion, SVNNumber, UIName girilmisse TV/STB'den okunan bu veriler dikkate alinmaz, diger veriler kullanilir '''
reportID = 0                    # WebMonitor'de aldiginiz testID'sini giriniz veya onceden oldiginiz testID'sini giriniz. Orn; 3535, 1923
projectName = ''                # 'sentor', 'ronesans', 'michelangelo', 'raphael', 'donatello', 'yoda', 'anakin'
hardwareName = ''               # 'mb130', 'mb211', ...
SWVersion = ''                  # 'v7.46.0.0', 'v0.31.0.0', ...
SVNNumber = ''                  # '235144', '240490', ...
UIName = 'titanium'                     # 'carbon', 'titanium', 'panasonic', ...

# TV_INFO_PARAM
customerName = 'OEM'            # 'OEM', 'Vestel', 'Panasonic', 'Toshiba'
countryName = 'GERMANY'         # 'GERMANY', 'TURKEY', 'UK' (default: 'GERMANY')
tvIP = '10.108.82.188'          # Ethernet capture kullanilacaksa TV'nin IP adresini giriniz, 'get_IP_address' komutuyla ogrenebilirsiniz

WebMonitor_NewTest_dict = {
    'vestaUserName': webMonitorUserName,
    'jiraTaskNo': '',                       # YODA-1234, VESTA-3535
    'project': projectName,
    'swType': '',                           # '', 'Official', 'Nightly', 'Trial', 'Test'
    'hardware_name': hardwareName,
    'hardware': 'MB130 768MB',              # Orn: 'MB130 1.5GB', 'MB211 768MB'
    'testName': 'EPG',                      # Degistirmeyin
    'version': SWVersion,
    'SVN': SVNNumber,
    'pm': '',
    'romboot': '',
    'mfc': '',
    'sampleCount': '1',
    'pcName': os.environ['COMPUTERNAME'],   # Degistirmeyin. WebMonitor'de 'Test Station Name', 'Test Computer Name' ve 'Test Suite Name'in birbiriyle iliskilendirilmelidir. 
    'ui': UIName,
    'language': 'English',
    'nots': '',
    }

# CONSTANTS
vestaMasterPath = '//manvestafile1/Vesta/MasterImages/'
testSuiteName = 'EPG'
deviceSettings = (2, 1, 1, 0, 2, 2)        # [imgCapDev, imgCompAlg, resizeCapture, rotateCapture, audCapDev, vidAnlDev]

projectN_vs_hardwareN_dict = {
    # ProjectName:  (HardwareName)
    'phoneix':      ('MB82',),
    'thorium':      ('MB95',),
    'sentor':       ('MB97',),
    'ronesans':     ('MB100',),
    'samba':        ('MB110',),
    'michelangelo': ('MB110',),
    'anakin':       ('MB110P',),
    'raphael':      ('MB120',),
    'donatello':    ('MB130',),
    'yoda':         ('MB130', 'MB135',),
    'splinter':     ('MB140',),
    'shredder':     ('MB211',),
    }

''' Settings Types
    imageSettings =             [imgCapDev, imgCompAlg, resizeCapture, rotateCapture, audCapDev, vidAnlDev]
    imgCapDev                   1: VesBox, 2: HarranBoard, 3: Ethernet, 4: Webcam, 5: LogitechCamC920
    imgCompAlg                  0: NoComparison, 1: PSNR, 2: AdvancedFuzzy, 3: FalconEye, 4: SSIM, 5: OpenCV
    resizeCapture               1: Capture'lari FHD cozunurluge donusturur, 0: Capture'larin boyutunu korur
    rotateCapture               0: NO_ROTATE, 1: FLIP_LEFT_RIGHT, 2: FLIP_TOP_BOTTOM, 4: ROTATE_180
    audCapDev                   1: Vesbox, 2: Harranboard
    vidAnlDev                   1: Vesbox, 2: Harranboard
'''

def test(api):
    global reportID
    try:
        api.activateDevices(**devConf)
        try:
            api.manual = Manual(1)
            print '\nMANUAL_CREATED\n'
        except:
            api.printError()
        if auto_getReportID or auto_readTVInfo:
            readTVInfo(api)
        setDeviceParameters(api)
        if test_Devices:
            checkTestDevices(api)
        if auto_getReportID:
            msg = 'ReportID almak icin gonderilen bilgiler:\n-------------------------------------------\n'
            for i in WebMonitor_NewTest_dict:
                msg += str(i)+': '+str(WebMonitor_NewTest_dict[i])+'\n'
            api.manual.sendCommands(['type; 1', 'timeout; 60', 'message; '+msg])
            api.manual.getResult()
            reportID = getReportID(WebMonitor_NewTest_dict)
            api.manual.sendCommands(['type; 1', 'timeout; 60', 'message; REPORTID: '+str(reportID)])
            api.manual.getResult()
        if not reportID:
            api.writeToLog('###### getReportID ERROR ######\n Web arayuzunden reportID alinamadi. \n#############################\n', fileName='ERROR', timestamp=False)
            reportID = 0
        makeTVSettingsGlobal(api)
        readyForTest(api)
        # MAKE_METHODS_GLOBAL
        api.getTV_IP = _getTV_IP
    except:
        api.printError()

def setDeviceParameters(api):
    try:
        # Image
        api.setCaptureDevice(deviceSettings[0])
        if (deviceSettings[0] == 3):
            tvIP = _getTV_IP(api)[0]
            api.setTvIP(tvIP)
        api.setPictureAlgorithm(deviceSettings[1])
        if (deviceSettings[1] == 1):
            api.setPSNRLimits(matchLimit=80, diffLimit=80)
        elif (deviceSettings[1] == 4):
            api.setSSIMLimits(matchLimit=80, diffLimit=80)
        api.setResizeCapture(deviceSettings[2])
        api.setRotateCapture(deviceSettings[3])
        api.setAudioCaptureDevice(deviceSettings[4])
        api.setVideoAnalysisDevice(deviceSettings[5])
        # Test_Case_Sequencer
        api.generateTCSequence(0)
    except:
        api.printError()

def checkTestDevices(api):
    try:
        api.setReportId(0, testName='DEVICE_CONTROL')
        api.setTestCaseName('init')
        api.setTestCaseDescription('Test and Device Configuration')
        if not api.start(force=True):
            try:
                # Test
                print api.grabImage('test1')
                sleep(1)
                print api.grabImage('test2')
            except:
                api.printError()
            api.end(False)
            print 'END: init'
    except:
        api.printError()

def makeTVSettingsGlobal(api):
    try:
        # MAKE_PARAMETERS_GLOBAL
        api.projectName = projectName.lower()
        api.UIName = UIName.lower()
        api.customerName = customerName
        api.countryName = countryName
    except:
        api.printError()

def readyForTest(api):
    try:
        # SET TestName & MasterPath
        masterPath = os.path.join(vestaMasterPath, 'EPG', UIName.lower(), projectName.title())
        testName = testSuiteName + '_' + projectName.title() + '_' + SWVersion + '_svn' + SVNNumber
        api.setTestMasterPath(masterPath)
        api.setReportId(reportID, testName)
    except:
        api.printError()

def readTVInfo(api):
    try:
        global SWVersion, SVNNumber, projectName, hardwareName, UIName, countryName, customerName, WebMonitor_NewTest_dict
        _SWVersion = _SVNNumber = _projectName = _UIName = _hardwareName = ramSize = PMVersion = mbootVersion = mfcVersion = languageName = ''
        langList = {
            'dan': 'danish', 'ger': 'german', 'est': 'estonian', 'eng': 'english', 'spa': 'spanish', 'gre': 'greek',
            'fre': 'french', 'gla': 'gaelic', 'hrv': 'croatian', 'ita': 'italian', 'lav': 'latvian', 'lit': 'lithuanian',
            'hun': 'hungarian', 'dut': 'dutch', 'nor': 'norwegian', 'pol': 'polish', 'por': 'portuguese', 'rus': 'russian',
            'rum': 'romanian', 'alb': 'albanian', 'slv': 'slovanian', 'slo': 'slovak', 'srp': 'serbian', 'fin': 'finnish',
            'swe': 'swedish', 'tur': 'turkish', 'cze': 'czech', 'ukr': 'ukranian', 'bul': 'bulgarian', 'ara': 'arabic',
            'per': 'persian', 'heb': 'hebrew', 'bel': 'belarussian', 'mac': 'macedonian', 'mon': 'montenegrin',
            'kaz': 'kazakh', 'tha': 'Thai'
            }
        countryList = {
            'aus': 'australia', 'dnk': 'denmark', 'fin': 'finland', 'fra': 'france', 'deu': 'germany', 'ita': 'italy',
            'nld': 'netherlands', 'nor': 'norway', 'pol': 'poland', 'prt': 'portugal', 'esp': 'spain', 'swe': 'sweden',
            'gbr': 'united_kingdom', 'alb': 'albania', 'aut': 'austria', 'bel': 'belgium', 'bgr': 'bulgaria', 'chn': 'china',
            'cze': 'czech_republic', 'est': 'estonia', 'grc': 'greece', 'hun': 'hungary', 'isr': 'israel', 'lva': 'latvia',
            'ltu': 'lithuania', 'mkd': 'macedonia', 'rou': 'romania', 'rus': 'russia', 'srb': 'serbia', 'svk': 'slovakia',
            'svn': 'slovenia', 'che': 'switzerland', 'tur': 'turkey', 'hrv': 'croatia', 'ice': 'iceland', 'lux': 'luxembourg',
            'ita': 'san_marino', 'nzl': 'new_zealand', 'mne': 'montenegro', 'ukr': 'ukraine', 'imn': 'isle_of_man',
            'sau': 'saudi_arabia', 'irn': 'persia', 'are': 'united_arab_emirates', 'kwt': 'kuwait', 'omn': 'oman',
            'bhr': 'bahrain', 'qat': 'qatar', 'blr': 'belarussia', 'irl': 'ireland', 'irq': 'iraq', 'jor': 'jordan',
            'lbn': 'lebanon', 'ind': 'india', 'col': 'colombia', 'cyp': 'cyprus', 'tha': 'thailand', 'gha': 'ghana',
            'egy': 'egypt', 'lbr': 'liberia', 'tgo': 'togo', 'sle': 'sierra_leone', 'civ': 'cote_d_ivoire', 'ken': 'kenya',
            'tza': 'tanzania', 'moz': 'mozambique', 'cod': 'congo', 'sen': 'senegal', 'nga': 'nigeria', 'eth': 'ethiopia',
            'zmb': 'zambia', 'uga': 'uganda', 'arg': 'argentina', 'ang': 'angola'}
        result = api.logKeywordsSearch(
            ['TV INFO', '#*project:', '#*hardware:', '#*ram:', '#*sw version:',
            '#*svn no:', '#*mboot ver:', '#*mfc ver:', '#*ip address:',
            '#*ui name:', '#*lang:', '#*country:', '#*customer:',  'Stbc ver:'],
            command=['UART_uartexit', 'UART_GETTVINFO+0.5'], counts=1, sTypes=1, timeout=2, portIndex=0)
        print '-----------> ', result, '<-------------'
        msg = 'GETTVINFO komutuyla alinan bilgiler:\n-------------------------------------------\n'
        for i in range(len(result[0])):
            msg += str(result[0][i])+'\n'
        api.manual.sendCommands(['type; 1', 'timeout; 60', 'message; '+msg])
        api.manual.getResult()
        if result[0][0] and result[0][0][0].find('TV INFO') > -1:
            if result[0][1] and result[0][1][0]:
                _projectName = result[0][1][0].split(': ')[1].strip().upper()
            if result[0][2] and result[0][2][0]:
                _hardwareName = result[0][2][0].split(': ')[1].strip().upper().replace('NC', '')
            if result[0][3] and result[0][3][0]:
                ramSize = result[0][3][0].split(': ')[1].strip().upper()
            if result[0][4] and result[0][4][0]:
                _SWVersion = result[0][4][0].split(': ')[1].strip().replace('V.', 'v')
            if result[0][5] and result[0][5][0]:
                _SVNNumber = result[0][5][0].split(': ')[1].strip()
            if result[0][6] and result[0][6][0]:
                try:
                    aaa = result[0][6][0].rsplit(':', 1)
                    if len(aaa) > 1:
                        PMVersion = aaa[1].strip()
                    aaa[0] = aaa[0].rsplit(': ', 1)[1].split('-')
                    mbootVersion = aaa[0][1].split(' ')[0]
                    _hardwareName = aaa[0][0].replace('NC', '')
                except:
                    pass
            if result[0][7] and result[0][7][0]:
                mfcVersion = result[0][7][0].split(': ')[1].strip().upper()
            if result[0][8] and result[0][8][0]:
                tvIP = result[0][8][0].split(': ')[1].strip().upper()
                api.setTvIP(tvIP)
            if result[0][9] and result[0][9][0]:
                _UIName = result[0][9][0].split(': ')[1].strip().lower().replace('_fhd', '').replace('_hd', '').title()
            if result[0][10] and result[0][10][0]:
                languageName = result[0][10][0].split(': ')[1].strip().title()
            if result[0][11] and result[0][11][0]:
                countryName = result[0][11][0].split(': ')[1].strip().upper()
            if result[0][12] and result[0][12][0]:
                customerName = result[0][12][0].split(': ')[1].strip().upper()
        else:
            result = api.logKeywordsSearch(
                ['MBoot Version:', 'DDR  Size:        ', '\#\*V\.|\#\*SW_VER: V\.', '#*Build info', '#*UI name:', '_hwprofile\.bin'], 
                patterns=[' MB\d{1,5}\-\d{1,6} PM ver: \d{1,6}| MB\d{1,6}NC\-\d{1,5} PM ver: \d{1,6}| MB\d{1,5}\-\d{1,6}| MB\d{1,6}NC\-\d{1,5}',
                '\d{1,5}MB|\d{1,5}\.\d{1,5}GB', 'V\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|V\.\d{1,3}\.\d{1,3}\.\d{1,3}[a-zA-Z]', '\[ \d{1,6}\]|\[\d{1,7}\]',
                '', ' MB\d{1,5}_hwprofile\.bin| mb\d{1,5}_hwprofile\.bin| t\d{1,5}_hwprofile\.bin| T\d{1,5}_hwprofile\.bin'], 
                command=['poweroff+5', 'poweron+10', '00+35', 'UART_aa', 'UART_GETSWVERSION+1', 'UART_aa', 'UART_BUILDINFO+1', 'UART_aa', 'UART_GETUINAME+1', 'UART_aa', 'UART_ls ../conf+1', 'UART_aa', 'UART_ls /conf+1'], counts=1, sTypes=1, timeout=1, portIndex=0)
            if result[0][0] and result[0][0][0]:
                try:
                    aaa = result[0][0][0].split(': ')
                    if len(aaa) > 1:
                        PMVersion = aaa[1]
                    mbootVersion = aaa[0].replace('PM ver', '').strip().split('-')[1]
                    _hardwareName = aaa[0].replace('PM ver', '').strip().split('-')[0].upper().replace('NC', '')
                except:
                    pass
            if result[0][1] and result[0][1][0]:
                ramSize = result[0][1][0]
            if result[0][2] and result[0][2][0]:
                _SWVersion = result[0][2][0].replace('V.', 'v')
            if result[0][3] and result[0][3][0]:
                _SVNNumber = result[0][3][0].replace('[', '').replace(']', '').strip()
            if result[0][4] and result[0][4][0]:
                _UIName = result[0][4][0].split('#*UI name:')[1].strip().lower().replace('_fhd', '').replace('_hd', '').title()
            if result[0][5] and result[0][5][0]:
                _hardwareName = result[0][5][0].split('_')[0].upper().strip().replace('NC', '')

        # Check Conditions
        if not projectName:
            projectName = _projectName
        if not SWVersion:
            SWVersion = _SWVersion
        if not SVNNumber:
            SVNNumber = _SVNNumber
        if not UIName:
            UIName = _UIName
        if not projectN_vs_hardwareN_dict.get(projectName.lower(), False):
            api.writeToLog('Please Update Project Hardware Dict! Since there is no such a project: %s\n' % (projectName.lower()), fileName='ERROR')
            return
        if not hardwareName:
            hardwareName = _hardwareName
        if not hardwareName:
            hardwareName = projectN_vs_hardwareN_dict.get(projectName.lower(), False).upper()
            if not hardwareName:
                api.writeToLog('Please Update Project Hardware Dict! Since there is no hardware for project: %s\n' % (projectName.lower()), fileName='ERROR')
                return
        if not (hardwareName in projectN_vs_hardwareN_dict.get(projectName.lower(), False)):
            api.writeToLog('Please Update Project Hardware Dict! Since there is no such a hardware: %s\n' % (hardwareName), fileName='ERROR')
            return
        if not SWVersion or not SVNNumber or not UIName:
            api.writeToLog('###### ERROR ######\n version, SVN, UI ve hardware bilgisi alinamadi. \n#############################\n', fileName='ERROR', timestamp=False)
            api.writeToLog('version: %s SVN: %s UI: %s\n' % (SWVersion, SVNNumber, UIName), fileName='ERROR', timestamp=False)
            return

        languageName = langList.get(languageName.lower(), 'English').title()
        countryName = countryList.get(countryName.lower(), countryName).title()

        # Update New Test Data
        WebMonitor_NewTest_dict['project'] = projectName
        WebMonitor_NewTest_dict['hardware_name'] = hardwareName
        WebMonitor_NewTest_dict['hardware'] = hardwareName + ' ' + ramSize
        WebMonitor_NewTest_dict['version'] = SWVersion
        WebMonitor_NewTest_dict['SVN'] = SVNNumber
        WebMonitor_NewTest_dict['pm'] = PMVersion
        WebMonitor_NewTest_dict['romboot'] = mbootVersion
        WebMonitor_NewTest_dict['mfc'] = mfcVersion
        WebMonitor_NewTest_dict['ui'] = UIName
        WebMonitor_NewTest_dict['language'] = languageName
        # WebMonitor_NewTest_dict['customerName'] = customerName
        # WebMonitor_NewTest_dict['countryName'] = countryName
    except:
        api.printError()

def getReportID(data):
    import urllib, urllib2
    url = 'http://veargd13262/vesta2/add_test.php'
    data = urllib.urlencode(data)
    content = urllib2.urlopen(url=url, data=data).read()
    reportID = 0
    if str(content).isdigit():
        reportID = int(content)
    return reportID

def _getTV_IP(api):
    try:
        api.TV_IP = ['']
        if api.captureDevice == 3:
            for i in range(5):
                result = api.logKeywordsSearch(['#*IPaddr:|#*IP|addr:'], 1, command=['UART_aa', 'UART_get_IP_address'], sTypes=1, patterns=['(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'])
                api.TV_IP = eval(str(result).replace('[[]]', "''").replace("[['", "'").replace("']]", "'"))
                print 'TV IP: ' + ''.join(api.TV_IP).replace('10.108', ', 10.108')[2:].replace('10.108', ', 10.108').replace('192.168', ', 192.168')[2:]
                if '' in api.TV_IP:
                    sleep(3)
                else:
                    break
    except:
        api.printError()
    return api.TV_IP

