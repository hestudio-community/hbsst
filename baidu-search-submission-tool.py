import sys
import os
import json

class main:
    def submit(self, config=None, url=None):
        if config == None:
            print("请传入预设方案！")
            sys.exit()
        if url == None:
            print("请传入需要提交的url！")
            sys.exit()
        if not os.path.exists(str("config.json")):
            print("未找到配置文件！")
            sys.exit()
        config_db = json.loads(str("config.json"))
        if not config_db[config]:
            print("未找到预设方案！")
            sys.exit()
        
