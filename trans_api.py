import requests
import random
import hashlib
import time


class trans_api:
    word = "hello"

    def __int__(self):
        self.word = None

    def salt_sign(self):
        navigator_appVersion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        t = hashlib.md5(navigator_appVersion.encode("utf-8")).hexdigest()
        r = str(int(time.time() * 1000))
        i = r + str(random.randint(1, 10))
        return {
            "ts": r,
            "bv": t,
            "salt": i,
            "sign": hashlib.md5(
                str("fanyideskweb" + self.word + i + "Ygy_4c=r#e#4EX^NUGUc5").encode("utf-8")).hexdigest()
        }

    def translate(self, word):
        self.word = word
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        r = self.salt_sign()
        data = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": r["salt"],
            "sign": r["sign"],
            "lts": r["ts"],
            "bv": r["bv"],
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        headers = {
            "Cookie": "OUTFOX_SEARCH_USER_ID=-286220249@10.108.160.17;",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
        res = requests.post(url=url, data=data, headers=headers).json()
        result = self.word + "的译文：" + res['translateResult'][0][0]['tgt'] + "\n" + "用法：" + res['smartResult']['entries'][1]
        return result

