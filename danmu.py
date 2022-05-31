# -*- coding = utf-8 -*-
# @Python : 3.8
from typing import Type
import sys

json3 = {"ts": 1654004500, "code": 0,
         "card": {"mid": "33521", "name": "玩的就是心跳", "approve": False, "sex": "保密", "rank": "10000",
                  "face": "http://i2.hdslb.com/bfs/face/5d2c92beb774a4bb30762538bb102d23670ae9c0.gif", "coins": 277,
                  "DisplayRank": "10000", "regtime": 1273493024, "spacesta": 0, "place": "", "birthday": "1980-01-01",
                  "sign": "", "description": "", "article": 0,
                  "attentions": [284836154, 121538100, 33683045, 10217261, 1276787, 197864], "fans": 0, "friend": 6,
                  "attention": 6,
                  "level_info": {"next_exp": 28800, "current_level": 5, "current_min": 10800, "current_exp": 11165},
                  "pendant": {"pid": 0, "name": "", "image": "", "expire": 0},
                  "official_verify": {"type": -1, "desc": ""}}}


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
    json_panser(json3)
    print("-" * 10)
    json_panser(json3, "attentions")
    print("-" * 10)
    json_panser(json3, keys)
