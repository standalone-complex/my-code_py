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
        '<em class=n_13></em>':'吃', '<em class=n_14></em>':'抽', '<em class=n_15></em>':'处', '<em class=n_16></em>':'床', '<em class=n_17></em>':'春', '<em class=n_18></em>':'唇', '<em class=n_19></em>':'刺', '<em class=n_20></em>':'粗', '<em class=n_21></em>':'大', '<em class=n_22></em>':'洞', '<em class=n_23></em>':'逗', '<em class=n_24></em>':'硬',
        '<em class=n_25></em>':'儿', '<em class=n_26></em>':'反', '<em class=n_27></em>':'犯', '<em class=n_28></em>':'峰', '<em class=n_29></em>':'妇', '<em class=n_30></em>':'抚', '<em class=n_31></em>':'夫', '<em class=n_32></em>':'腹', '<em class=n_33></em>':'干', '<em class=n_34></em>':'搞', '<em class=n_35></em>':'根', '<em class=n_36></em>':'公',
        '<em class=n_37></em>':'宫', '<em class=n_38></em>':'勾', '<em class=n_39></em>':'股', '<em class=n_40></em>':'狠', '<em class=n_41></em>':'花', '<em class=n_42></em>':'滑', '<em class=n_43></em>':'坏', '<em class=n_44></em>':'魂', '<em class=n_45></em>':'鸡', '<em class=n_46></em>':'激', '<em class=n_47></em>':'夹', '<em class=n_48></em>':'奸',
        '<em class=n_49></em>':'交', '<em class=n_50></em>':'叫', '<em class=n_51></em>':'娇', '<em class=n_52></em>':'姐', '<em class=n_53></em>':'禁', '<em class=n_54></em>':'精', '<em class=n_55></em>':'进', '<em class=n_56></em>':'紧', '<em class=n_57></em>':'菊', '<em class=n_58></em>':'渴', '<em class=n_59></em>':'口', '<em class=n_60></em>':'裤',
        '<em class=n_61></em>':'胯', '<em class=n_62></em>':'快', '<em class=n_63></em>':'浪', '<em class=n_64></em>':'力', '<em class=n_65></em>':'搂', '<em class=n_66></em>':'乱', '<em class=n_67></em>':'裸', '<em class=n_68></em>':'妈', '<em class=n_69></em>':'毛', '<em class=n_70></em>':'迷', '<em class=n_71></em>':'靡', '<em class=n_72></em>':'妹',
        '<em class=n_73></em>':'摸', '<em class=n_74></em>':'嫩', '<em class=n_75></em>':'母', '<em class=n_76></em>':'娘', '<em class=n_77></em>':'尿', '<em class=n_78></em>':'咛', '<em class=n_79></em>':'女', '<em class=n_80></em>':'哦', '<em class=n_81></em>':'趴', '<em class=n_82></em>':'喷', '<em class=n_83></em>':'婆', '<em class=n_84></em>':'屁',
        '<em class=n_85></em>':'气', '<em class=n_86></em>':'枪', '<em class=n_87></em>':'窃', '<em class=n_88></em>':'骑', '<em class=n_89></em>':'妻', '<em class=n_90></em>':'情', '<em class=n_91></em>':'亲', '<em class=n_92></em>':'群', '<em class=n_93></em>':'热', '<em class=n_94></em>':'日', '<em class=n_95></em>':'肉', '<em class=n_96></em>':'揉',
        '<em class=n_97></em>':'乳', '<em class=n_98></em>':'软', '<em class=n_99></em>':'润', '<em class=n_100></em>':'入', '<em class=n_101></em>':'塞', '<em class=n_102></em>':'骚', '<em class=n_103></em>':'色', '<em class=n_104></em>':'上', '<em class=n_105></em>':'舌', '<em class=n_106></em>':'射', '<em class=n_107></em>':'身', '<em class=n_108></em>':'深',
        '<em class=n_109></em>':'湿', '<em class=n_110></em>':'兽', '<em class=n_111></em>':'受', '<em class=n_112></em>':'舒', '<em class=n_113></em>':'爽', '<em class=n_114></em>':'水', '<em class=n_115></em>':'睡', '<em class=n_116></em>':'酥', '<em class=n_117></em>':'死', '<em class=n_118></em>':'烫', '<em class=n_119></em>':'痛', '<em class=n_120></em>':'舔',
        '<em class=n_121></em>':'天', '<em class=n_122></em>':'体', '<em class=n_123></em>':'挺', '<em class=n_124></em>':'头', '<em class=n_125></em>':'腿', '<em class=n_126></em>':'脱', '<em class=n_127></em>':'味', '<em class=n_128></em>':'慰', '<em class=n_129></em>':'吻', '<em class=n_130></em>':'握', '<em class=n_131></em>':'喔', '<em class=n_132></em>':'污',
        '<em class=n_133></em>':'下', '<em class=n_134></em>':'小', '<em class=n_135></em>':'性', '<em class=n_136></em>':'胸', '<em class=n_137></em>':'血', '<em class=n_138></em>':'穴', '<em class=n_139></em>':'阳', '<em class=n_140></em>':'痒', '<em class=n_141></em>':'药', '<em class=n_142></em>':'腰', '<em class=n_143></em>':'夜', '<em class=n_144></em>':'液',
        '<em class=n_145></em>':'野', '<em class=n_146></em>':'衣', '<em class=n_147></em>':'姨', '<em class=n_148></em>':'吟', '<em class=n_149></em>':'淫', '<em class=n_150></em>':'荫', '<em class=n_151></em>':'幽', '<em class=n_152></em>':'诱', '<em class=n_153></em>':'尤', '<em class=n_154></em>':'欲', '<em class=n_155></em>':'吁', '<em class=n_156></em>':'玉',
        '<em class=n_157></em>':'吮', '<em class=n_158></em>':'窄', '<em class=n_159></em>':'占', '<em class=n_160></em>':'征', '<em class=n_161></em>':'汁', '<em class=n_162></em>':'嘴', '<em class=n_163></em>':'，', '<em class=n_164></em>':'。', '<em class=n_165></em>':'…', '<em class=n_166></em>':'慾', '<em class=n_167></em>':'丢', '<em class=n_168></em>':'弄'
    }

    for key, value in trans_map.items():
        pattern = re.compile(key)
        html = re.sub(pattern, value, html)

    # rets = re.findall('', html, re.S)

    return html

def main():
    url = 'https://m.sinodan.link/view/715121.html'

    html = get_one_page(url)

    rets = trans(html)

    print(rets)

    return 0

main()