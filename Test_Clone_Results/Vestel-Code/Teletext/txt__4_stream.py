
def test(api):
    try:
        api.DVBS_10750_27500 = ['InputFile; D:/Streams/Teletext/TRT_TXT_221205_0932_12_05.trp', 'Frequency; 1000', 'BitRate; 38014706', 'ModulationType; DVBS', 'Constellation; QPSK', 'ConvolutionalRate; 3/4', 'remultiplex; 1', 'ignore_stop; 1']
        api.DVBS_10750_27500_TurkGreek = ['InputFile; D:/Streams/Teletext/larissa_tp53_txt_problem_1min_06_06.ts', 'Frequency; 1000', 'BitRate; 38014706', 'ModulationType; DVBS', 'Constellation; QPSK', 'ConvolutionalRate; 3/4', 'remultiplex; 1', 'ignore_stop; 1']
        api.DVBS_10750_27500_East = ['InputFile; D:/Streams/Teletext/hp_tronic_MUX1_3min_dvbc.ts', 'Frequency; 1000', 'BitRate; 38014706', 'ModulationType; DVBS', 'Constellation; QPSK', 'ConvolutionalRate; 3/4', 'remultiplex; 1', 'ignore_stop; 1']
        api.DVBS_10750_27500_Cyrillic = ['InputFile; D:/Streams/Teletext/CH30-DVB-T2-LONG-MOSCOW-DVBT.mpg', 'Frequency; 1000', 'BitRate; 38014706', 'ModulationType; DVBS', 'Constellation; QPSK', 'ConvolutionalRate; 3/4', 'remultiplex; 1', 'ignore_stop; 1']
        api.DVBS_10750_27500_Arabic = ['InputFile; D:/Streams/Teletext/ch37-1.ts', 'Frequency; 1000', 'BitRate; 38014706', 'ModulationType; DVBS', 'Constellation; QPSK', 'ConvolutionalRate; 3/4', 'remultiplex; 1', 'ignore_stop; 1']
        api.DVBT_698Mhz_CH49_Spanish = ['InputFile; D:/Streams/Teletext/20160309_570MHz_TV3HD.ts', 'ModulationType; DVBT', 'Frequency; 698', 'BitRate; 31668449', 'TransmissionMode; 8K', 'Constellation; QAM64', 'ConvolutionalRate; 3/4', 'GuardInterval; 1/32', 'Bandwidth; 8MHz', 'remultiplex; 1', 'ignore_stop; 1']
        api.DVBT_474Mhz_CH21_West = ['InputFile; D:/Streams/Teletext/MHz._ses senkron_undifened.ts', 'ModulationType; DVBT', 'Frequency; 474', 'BitRate; 31668449', 'TransmissionMode; 8K', 'Constellation; QAM64', 'ConvolutionalRate; 7/8', 'GuardInterval; 1/32', 'Bandwidth; 8MHz', 'remultiplex; 1', 'ignore_stop; 1']
    except:
        api.printError()

