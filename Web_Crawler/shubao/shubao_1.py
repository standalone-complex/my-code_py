import requests
import re

def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.38'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    
    return None

def trans(html):
    trans_map = {
        '<em class=n_1></em>':'男', '<em class=n_2></em>':'人', '<em class=n_3></em>':'啊', '<em class=n_4></em>':'爱', '<em class=n_5></em>':'按', '<em class=n_6></em>':'暴', '<em class=n_7></em>':'臀', '<em class=n_8></em>':'逼', '<em class=n_9></em>':'擦', '<em class=n_10></em>':'潮', '<em class=n_11></em>':'操', '<em class=n_12></em>':'插',
        '<em class=n_13></em>':'吃', '<em class=n_14></em>':'抽', '<em class=n_15></em>':'处', '<em class=n_16></em>':'床', '<em class=n_17></em>':'春', '<em class=n_18></em>':'唇', '<em class=n_19></em>':'刺', '<em class=n_20></em>':'粗', '<em class=n_21></em>':'大', '<em class=n_22></em>':'洞', '<em class=n_23></em>':'逗', '<em class=n_24></em>':'',
        '<em class=n_25></em>':'', '<em class=n_26></em>':'', '<em class=n_27></em>':'', '<em class=n_28></em>':'', '<em class=n_29></em>':'', '<em class=n_30></em>':'', '<em class=n_31></em>':'', '<em class=n_32></em>':'', '<em class=n_33></em>':'', '<em class=n_34></em>':'', '<em class=n_35></em>':'', '<em class=n_36></em>':'',
        '<em class=n_37></em>':'', '<em class=n_38></em>':'', '<em class=n_39></em>':'', '<em class=n_40></em>':'', '<em class=n_41></em>':'', '<em class=n_42></em>':'', '<em class=n_43></em>':'', '<em class=n_44></em>':'', '<em class=n_45></em>':'', '<em class=n_46></em>':'', '<em class=n_47></em>':'', '<em class=n_48></em>':'',
        '<em class=n_49></em>':'', '<em class=n_50></em>':'', '<em class=n_51></em>':'', '<em class=n_52></em>':'', '<em class=n_53></em>':'', '<em class=n_54></em>':'', '<em class=n_55></em>':'', '<em class=n_56></em>':'', '<em class=n_57></em>':'', '<em class=n_58></em>':'', '<em class=n_59></em>':'', '<em class=n_60></em>':'',
        '<em class=n_61></em>':'', '<em class=n_62></em>':'', '<em class=n_63></em>':'', '<em class=n_64></em>':'', '<em class=n_65></em>':'', '<em class=n_66></em>':'', '<em class=n_67></em>':'', '<em class=n_68></em>':'', '<em class=n_69></em>':'', '<em class=n_70></em>':'', '<em class=n_71></em>':'', '<em class=n_72></em>':'',
        '<em class=n_73></em>':'', '<em class=n_74></em>':'', '<em class=n_75></em>':'', '<em class=n_76></em>':'', '<em class=n_77></em>':'', '<em class=n_78></em>':'', '<em class=n_79></em>':'', '<em class=n_80></em>':'', '<em class=n_81></em>':'', '<em class=n_82></em>':'', '<em class=n_83></em>':'', '<em class=n_84></em>':'',
        '<em class=n_85></em>':'', '<em class=n_86></em>':'', '<em class=n_87></em>':'', '<em class=n_88></em>':'', '<em class=n_89></em>':'', '<em class=n_90></em>':'', '<em class=n_91></em>':'', '<em class=n_92></em>':'', '<em class=n_93></em>':'', '<em class=n_94></em>':'', '<em class=n_95></em>':'', '<em class=n_96></em>':'',
        '<em class=n_97></em>':'', '<em class=n_98></em>':'', '<em class=n_99></em>':'', '<em class=n_100></em>':'', '<em class=n_101></em>':'', '<em class=n_102></em>':'', '<em class=n_103></em>':'', '<em class=n_104></em>':'', '<em class=n_105></em>':'', '<em class=n_106></em>':'', '<em class=n_107></em>':'', '<em class=n_108></em>':'',
        '<em class=n_109></em>':'', '<em class=n_110></em>':'', '<em class=n_111></em>':'', '<em class=n_112></em>':'', '<em class=n_113></em>':'', '<em class=n_114></em>':'', '<em class=n_115></em>':'', '<em class=n_116></em>':'', '<em class=n_117></em>':'', '<em class=n_118></em>':'', '<em class=n_119></em>':'', '<em class=n_120></em>':'',
        '<em class=n_121></em>':'', '<em class=n_122></em>':'', '<em class=n_123></em>':'', '<em class=n_124></em>':'', '<em class=n_125></em>':'', '<em class=n_126></em>':'', '<em class=n_127></em>':'', '<em class=n_128></em>':'', '<em class=n_129></em>':'', '<em class=n_130></em>':'', '<em class=n_131></em>':'', '<em class=n_132></em>':'',
        '<em class=n_133></em>':'', '<em class=n_134></em>':'', '<em class=n_135></em>':'', '<em class=n_136></em>':'', '<em class=n_137></em>':'', '<em class=n_138></em>':'', '<em class=n_139></em>':'', '<em class=n_140></em>':'', '<em class=n_141></em>':'', '<em class=n_142></em>':'', '<em class=n_143></em>':'', '<em class=n_144></em>':'',
        '<em class=n_145></em>':'', '<em class=n_146></em>':'', '<em class=n_147></em>':'', '<em class=n_148></em>':'', '<em class=n_149></em>':'', '<em class=n_150></em>':'', '<em class=n_151></em>':'', '<em class=n_152></em>':'', '<em class=n_153></em>':'', '<em class=n_154></em>':'', '<em class=n_155></em>':'', '<em class=n_156></em>':'',
        '<em class=n_157></em>':'', '<em class=n_158></em>':'', '<em class=n_159></em>':'', '<em class=n_160></em>':'', '<em class=n_161></em>':'', '<em class=n_162></em>':'', '<em class=n_163></em>':'', '<em class=n_164></em>':'', '<em class=n_165></em>':'', '<em class=n_166></em>':'', '<em class=n_167></em>':'', '<em class=n_168></em>':''
    }

    for key, value in trans_map.items():
        html = re.compile(key, value, html)

    # rets = re.findall('', html, re.S)

    # return rets

def main():
    url = 'https://m.sinodan.link/view/715121.html'

    html = get_one_page(url)

    rets = trans(html)

    print()

    return 0

main()