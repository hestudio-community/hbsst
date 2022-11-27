import sys
import os
import json
import time

class main:
    def submit(self, config=None, url=None):
        if config == None:
            print("请传入预设方案！")
            sys.exit()
        if url == None:
            print("请传入需要提交的url！")
            sys.exit()
        if not os.path.exists(str("hbsst_config.json")):
            print("未找到配置文件！")
            sys.exit()
        config_db = json.load(open(str("hbsst_config.json")))
        if not config_db[config]:
            print("未找到预设方案！")
            sys.exit()
        print("正在保存url")
        urls = open("urls.txt", mode = 'w')
        time.sleep(1)
        urls.write(url)
        time.sleep(2)
        urls.close()
        time.sleep(1)
        print("正在推送")
        curl_return = os.popen(str("curl -H 'Content-Type:text/plain' --data-binary @urls.txt "+repr(config_db[config])))
        time.sleep(2)
        print("正在接收返回结果\n")
        curl_return_json = open("hbsst_return.json", mode = 'w')
        time.sleep(1)
        curl_return_json.write(curl_return)
        time.sleep(2)
        curl_return_json.close()
        time.sleep(1)
        curl_return_data = json.load(curl_return)
        if curl_return_data["success"]:
            print("成功推送的url条数：", curl_return_data["success"])
        if curl_return_data["remain"]:
            print("当天剩余的可推送url条数：", curl_return_data["remain"])
        if curl_return_data["not_same_site"]:
            print("由于不是本站url而未处理的url列表：", curl_return_data["not_same_site"])
        if curl_return_data["not_valid"]:
            print("不合法的url列表：", curl_return_data["not_valid"])
        if curl_return_data["error"]:
            print("错误码：", curl_return_data["error"])
        if curl_return_data["message"]:
            print("错误描述：", curl_return_data["message"])
        

    def 