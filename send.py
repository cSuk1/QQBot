from trans_api import trans_api
import requests


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
        resp_dict = {"msg_type": type, "number": qid, "msg": result}
        send_msg(resp_dict)
