from flask import Flask, request
from send import *

app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':  # 私聊信息
        print(request.get_json())
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        get_res("private", uid, message)  # 将 Q号和原始信息传到我们的后台
    # 群聊
    # if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
    #     gid = request.get_json().get('group_id')  # 获取群号
    #     uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
    #     message = request.get_json().get('raw_message')  # 获取原始信息
    #     get_res("group", uid, message)  # 将 Q号和原始信息传到我们的后台

    return "None"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)  # 此处的 host和 port对应上面 yml文件的设置
