# -*- coding = utf-8 -*-
# @Python : 3.8
from typing import Type
import sys

json3 = {"ts":1654037445,"code":0,"card":{"mid":"33605910","name":"啵啵小麻","approve":False,"sex":"女","rank":"10000","face":"http://i0.hdslb.com/bfs/face/4575bd4b85f60e3a007227baed5d72223e152052.jpg","coins":102.7,"DisplayRank":"10000","regtime":1467103006,"spacesta":2,"place":"","birthday":"2000-04-18","sign":"玉桂狗不灭","description":"","article":0,"attentions":[99239148,284120,22017124,229733301,3379951,21562856,291323980,118939898,26249803,343063698,261485584,1005135296,399114140,1618410357,1202350411,207346018,499136616,75500504,481661177,1037927190,690777707,355124538,2209088,29919485,17485141,324516490,1629188451,482753878,32803588,16720403,107280606,701527753,1511521955,544126329,434656505,1482994322,396848107,7706705,33165826,673416125,29944130,424439,41397542,537698,1296133469,1783485518,345046260,1493826216,88082626,21446657,1638018482,222103174,54898207,37786223,1327333801,631067,502544405,452606628,22911118,20151208,442976618,1185499676,1020040160,402978061,358648389,470270944,34218422,1206696349,674888583,267038161,42870908,392475261,10128411,7233069,477936031,1910162022,397633449,40712950,42986429,345630501,162732046,31859146,404114320,19012355,20511047,1777380035,97181110,11025317,17364274,11292325,410517509,39972323,383444157,75901514,95220561,1659994,111398038,298165739,12428214,37090048,546195,112924325,258449297,11299405,22548267,43088421,28285245,135589565,82640453,110352985,46494878,2735036,2173411,14636079,17702916,927587,23210525,14764672,51946738,16307541,3331521,12723824,13792126,2024816,178069965,87456568,30954515,101666745,53747420,2691287,16785036,123987724,200870,415405,18020792,222614252,2338033,7866992,592232,3632990,378034,2743119,618340,2884277,35049444,5462540,622863,1324413,71203142,1678535,119418,15404697,31766424,44170758,13204855,5905751,26253404,1532165,19456751,35836017,4537274,116683],"fans":197698,"friend":162,"attention":162,"level_info":{"next_exp":28800,"current_level":5,"current_min":10800,"current_exp":13591},"pendant":{"pid":0,"name":"","image":"","expire":0},"official_verify":{"type":-1,"desc":""}}}


def json_parse_gen(json, name, key=None):
    j = json
    if type(j) == list:
        if j:
            t = type(j[0])
            if t == list:
                json_parse_gen(j[0], f"{name}[{0}]", key)
            elif t == dict:
                json_parse_gen(j[0], f"{name}[{0}]", key)
            else:
                if not key:
                    print(f"""for {name.split("'")[-2]}_item in {name}:\n    print({name.split("'")[-2]}_item)""")
        else:
            if not key:
                print(f"""for i in {name}: # 空\n    print(i)""")
    elif type(j) == dict:
        if j:
            for k in j:
                if k == key:
                    print(f"{k}={name}['{k}']")
                    return f"{k}={name}['{k}']"  # sys.exit()
                t = type(j[k])
                if t == list:
                    if not key:
                        print(f"list_{k}={name}['{k}']")
                    json_parse_gen(j[k], f"{name}['{k}']", key)
                elif t == dict:
                    if not key:
                        print(f"dict_{k}={name}['{k}']")
                    json_parse_gen(j[k], f"{name}['{k}']", key)
                else:
                    if not key:
                        print(f"""{k}={name}['{k}']""")


def get_varname(var, locals=locals()):
    for k, v in locals.items():
        if v is var:
            return k


def json_panser(json, key=None):
    """
    :param json: dict
                des: the dict/json need to deal
    :param key: [] or "" or default None
                des: to find the key or not
    :return: None
    """
    t = type(key)
    if t == list:
        for k in key:
            if k:
                json_parse_gen(json=json, name=get_varname(json), key=k)
    elif t == str:
        json_parse_gen(json=json, name=get_varname(json), key=key)
    elif key is None:
        json_parse_gen(json=json, name=get_varname(json))
    else:
        raise TypeError("need list or str")


if __name__ == '__main__':
    keys = ["bvid", "name", "uid", "mid", "time", "uname", "reply", "like", ""]
    j_asd = {
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" },
    { "name":"google" , "url":"www.google.com" },
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}
    json_panser(j_asd)
    # json_panser(json3, keys)
