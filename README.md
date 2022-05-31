# json_parser_gen_code

little tool | Json Parser |gen code

## use
git clone
```python
from json_parser_gen_code.main import json_panser

json = {"such": 1, "as": "test", "this": ["1", "2", "3"]}
json_panser(json, key=None)
"""
:param json: dict
            des: the dict/json need to deal
:param key: [] or "" or default None
            des: to find the key or not
:return: None
"""
```

## input

json / dict

```json
json3 = {
  "ts": 1654004500,
  "code": 0,
  "card": {
    "mid": "33521",
    "name": "玩的就是心跳",
    "approve": False,
    "sex": "保密",
    "rank": "10000",
    "face": "http://i2.hdslb.com/bfs/face/5d2c92beb774a4bb30762538bb102d23670ae9c0.gif",
    "coins": 277,
    "DisplayRank": "10000",
    "regtime": 1273493024,
    "spacesta": 0,
    "place": "",
    "birthday": "1980-01-01",
    "sign": "",
    "description": "",
    "article": 0,
    "attentions": [
      284836154,
      121538100,
      33683045,
      10217261,
      1276787,
      197864
    ],
    "fans": 0,
    "friend": 6,
    "attention": 6,
    "level_info": {
      "next_exp": 28800,
      "current_level": 5,
      "current_min": 10800,
      "current_exp": 11165
    },
    "pendant": {
      "pid": 0,
      "name": "",
      "image": "",
      "expire": 0
    },
    "official_verify": {
      "type": -1,
      "desc": ""
    }
  }
}
```

## output

```python

ts = json3['ts']
code = json3['code']
dict_card = json3['card']
mid = json3['card']['mid']
name = json3['card']['name']
approve = json3['card']['approve']
sex = json3['card']['sex']
rank = json3['card']['rank']
face = json3['card']['face']
coins = json3['card']['coins']
DisplayRank = json3['card']['DisplayRank']
regtime = json3['card']['regtime']
spacesta = json3['card']['spacesta']
place = json3['card']['place']
birthday = json3['card']['birthday']
sign = json3['card']['sign']
description = json3['card']['description']
article = json3['card']['article']
list_attentions = json3['card']['attentions']
for attentions_item in json3['card']['attentions']:
    print(attentions_item)
fans = json3['card']['fans']
friend = json3['card']['friend']
attention = json3['card']['attention']
dict_level_info = json3['card']['level_info']
next_exp = json3['card']['level_info']['next_exp']
current_level = json3['card']['level_info']['current_level']
current_min = json3['card']['level_info']['current_min']
current_exp = json3['card']['level_info']['current_exp']
dict_pendant = json3['card']['pendant']
pid = json3['card']['pendant']['pid']
name = json3['card']['pendant']['name']
image = json3['card']['pendant']['image']
expire = json3['card']['pendant']['expire']
dict_official_verify = json3['card']['official_verify']
type = json3['card']['official_verify']['type']
desc = json3['card']['official_verify']['desc']
----------
attentions = json3['card']['attentions']
----------
name = json3['card']['name']
mid = json3['card']['mid']

```