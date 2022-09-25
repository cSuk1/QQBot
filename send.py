from trans_api import trans_api
import requests
from weather_now import get_weather


def send_msg(resp_dict):
    msg_type = resp_dict["msg_type"]  # 回复类型（群聊/私聊）
    number = resp_dict["number"]  # 回复账号（群号/好友号）
    msg = resp_dict["msg"]  # 要回复的消息
    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace(" ", "%0a")
    if msg_type == "group":
        payload = "http://127.0.0.1:5700/send_group_msg?group_id=" + str(
            number) + "&message=" + msg
    elif msg_type == "private":
        payload = "http://127.0.0.1:5700/send_private_msg?user_id=" + str(
            number) + "&message=" + msg
    print("发送" + payload)
    requests.get(payload)
    return 0


def get_res(type, qid, msg):
    if msg[0:2] == "翻译":
        trans_obj = trans_api()
        result = trans_obj.translate(msg[2:])
        if result == 0:
            not_found = "抱歉，没有找到您翻译的单词"
            not_found_dict = {"msg_type": type, "number": qid, "msg": not_found}
            send_msg(not_found_dict)
        else:
            trans_dict = {"msg_type": type, "number": qid, "msg": result}
            send_msg(trans_dict)
    elif msg[0:2] == "天气":
        wt_dict = get_weather(msg[2:])
        if wt_dict == 0:
            not_found = "抱歉，没有找到您查询的城市"
            not_found_dict = {"msg_type": type, "number": qid, "msg": not_found}
            send_msg(not_found_dict)
        else:
            weather = ""
            for key in wt_dict:
                weather += key + ": " + wt_dict[key] + "\n"
            trans_dict = {"msg_type": type, "number": qid, "msg": weather}
            send_msg(trans_dict)
    else:
        greet = "你好，我是菜狗的QQ机器人。\n我能为你做的事：\n翻译功能：翻译[你需要翻译的单词]\n2.实时天气：天气[你所在的城市]"
        greet_dict = {"msg_type": type, "number": qid, "msg": greet}
        send_msg(greet_dict)
