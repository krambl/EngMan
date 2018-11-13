from googletrans import Translator
import random
import requests

print('================================================================================')
print('\n', '                    ДОБРО ПОЖАЛОВАТЬ В МЕГАПРОГРАММУ', '\n')
print('================================================================================')

print('               Нажмите enter, чтобы получить предложение для перевода        ')


file = open('Z:\\ОСНОВНЫЕ\\VE --- eng - rus.txt', 'r')
text = file.readlines()

while 1 == 1:
    bessy = input()
    eng = ''
    rus = ''
    vibor = random.randint(0, len(text) - 1)
    para = text[vibor]
    para = list(para)
    file.close()

    for i in range(len(para)):
        xm = para.pop(0)
        if xm != '\t':
            eng += xm
        if xm == '\t':
            break
    for i in range(len(para)):
        xm = para.pop(0)
        if xm != '\n':
            rus += xm
        if xm == '\n':
            break

    mst = [['i', 'я'], ['you', 'ты'], ['he', 'он'], ['she', 'она'], ['we', 'мы'], ['they', 'они']]
    vibor = random.randint(0, 5)
    msti = mst[vibor]
    mrus = msti[1]
    meng = msti[0]

    eng_f_ut = meng + ' will ' + eng
    eng_f_otr = meng + ' will not ' + eng
    eng_f_vp = 'will ' + meng + ' ' + eng

    eng_past_ut = meng + ' ' + eng + 'ed'
    eng_past_otr = meng + ' did not ' + eng
    eng_past_vp = 'Did ' + meng + ' ' + eng

    if meng == 'he' or meng == 'she':
        eng_simpl_ut = meng + ' ' + eng + 's'
        eng_simpl_otr = meng + ' does not ' + eng
        eng_simpl_vp = 'Does ' + meng + ' ' + eng

    if meng != 'he' and meng != 'she':
        eng_simpl_ut = meng + ' ' + eng
        eng_simpl_otr = meng + ' do not ' + eng
        eng_simpl_vp = 'Do ' + meng + ' ' + eng

    vibor = random.randint(0, 8)
    v_eng = [eng_f_ut, eng_f_otr, eng_f_vp, eng_past_ut, eng_past_otr, eng_past_vp, eng_simpl_ut, eng_simpl_otr,
             eng_simpl_vp]
    print(v_eng[vibor])

    eng_text = v_eng[vibor]
    token = 'trnsl.1.1.20181112T204902Z.eb0176a347eb7516.875716dc4d0ec45835f09680e96438d89aff6df4'
    url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
    webRequest = requests.get(url_trans, params=trans_option)

    rus_text = webRequest.text

    rus_text = rus_text[36:(len(rus_text) - 3)]
    bassys = input()
    print(rus_text)


