from flask import Flask, request
from danawa import load_first_category, load_second_category, load_third_category, load_prod

app = Flask(__name__)

SIZE = 4


@app.route("/api/c1", methods=['POST', 'GET'])
def category1():
    body = request.get_json()
    utt = body['userRequest']['utterance']  # 채팅창에 입력한 값

    result = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "carousel": {
              "type": "listCard",
              "items": []
            }
          }
        ]
      }
    }

    if utt == '시작':
        cate_dict = load_first_category()
        cate_list = list(cate_dict.keys())
        items = []
        for idx, c in enumerate(cate_list):
            item = {
                "title": c,
                "imageUrl": cate_dict[c]['link'],
                "action": "block",
                "blockId": "65717e4b063df03a4fcadb97",
                "extra": {
                    "prev_category": c,
                    "code_num": str(cate_dict[c]['code']),
                }
            }

            items.append(item)
            # 각각의 listCard에 4개씩 추가
            if len(items) == SIZE or idx+1 == len(cate_list):
                div = {
                  "header": {
                    "title": "전체 카테고리"
                  },
                  "items": items
                }
                items = []
                result['template']['outputs'][0]['carousel']['items'].append(div)

    return result


@app.route("/api/c2", methods=['POST', 'GET'])
def category2():
    body = request.get_json()

    prev_category = body['action']['clientExtra']['prev_category']
    code_num = body['action']['clientExtra']['code_num']

    result = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "carousel": {
              "type": "listCard",
              "items": []
            }
          }
        ]
      }
    }

    cate_dict = load_second_category(code_num)
    cate_list = list(cate_dict.keys())

    items = []
    for idx, c in enumerate(cate_list):
        item = {
            "title": c,
            "imageUrl": f"https:{cate_dict[c]['link']}",
            "action": "block",
            "blockId": "6571869a6acfc8089c74b388",
            "extra": {
                "prev_category": c,
                "code_num": str(code_num),
                "category_num": str(idx)
            }
        }

        items.append(item)
        # 각각의 listCard에 4개씩 추가
        if len(items) == SIZE or idx+1 == len(cate_list):
            div = {
              "header": {
                "title": prev_category
              },
              "items": items
            }
            items = []
            result['template']['outputs'][0]['carousel']['items'].append(div)

    return result


@app.route("/api/c3", methods=['POST', 'GET'])
def category3():
    body = request.get_json()

    prev_category = body['action']['clientExtra']['prev_category']
    category_num = body['action']['clientExtra']['category_num']
    code_num = body['action']['clientExtra']['code_num']

    result = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "carousel": {
              "type": "listCard",
              "items": []
            }
          }
        ]
      }
    }

    cate_dict = load_third_category(category_num, code_num)
    cate_list = list(cate_dict.keys())

    items = []
    for idx, c in enumerate(cate_list):
        item = {
            "title": c,
            "imageUrl": "",
            "action": "block",
            "blockId": "6574218865f62e039fa23985",
            "extra": {
                "link": cate_dict[c]
            }
        }

        items.append(item)
        # 각각의 listCard에 4개씩 추가
        if len(items) == SIZE or idx+1 == len(cate_list):
            div = {
              "header": {
                "title": prev_category
              },
              "items": items
            }
            items = []
            result['template']['outputs'][0]['carousel']['items'].append(div)

    return result


@app.route("/api/product", methods=['POST', 'GET'])
def product():
    body = request.get_json()
    link = body['action']['clientExtra']['link']

    result = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "carousel": {
              "type": "basicCard",
              "items": []
            }
          }
        ]
      }
    }

    prod_dict = load_prod(link)
    prod_list = list(prod_dict.keys())

    for idx, p in enumerate(prod_list):
        item = {
            "title": p,
            # "description": "",
            "description": prod_dict[p]['spec'],
            "thumbnail": {
                "imageUrl": "",
                "imageUrl": prod_dict[p]['img'],
                # "link": prod_dict[p]['url'],
                "fixedRatio": True
            },
            "buttons": [
                {
                    "action":  "webLink",
                    "label": "구경하기",
                    "webLinkUrl": prod_dict[p]['url']
                }
            ]
        }
        result['template']['outputs'][0]['carousel']['items'].append(item)

    return result

app.run(host='0.0.0.0', port=80)
