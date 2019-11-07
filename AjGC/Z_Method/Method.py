import requests,json
class Method:
    #写入自定义变量到字典中
    def AddDefineXX(self,RelyData):
        for b in range(0,99):
            conc = str(input("是否继续添加指定字段(Y/N):"))
            if conc == "Y":
                RelyDataKey = str(input("请输入字段名:"))
                RelyDataValue = str(input("请输入字段值:"))
                RelyData.update({RelyDataKey: RelyDataValue})
            else:
                print("自定义字段填写完成...")
                break
        return RelyData
    #根据url port做请求
    def RequestAddress(self,Address):
        url=Address.get("url")
        port=Address.get("port")
        r = requests.request("GET", "http://"+url+port+"/v2/api-docs")
        result = r.text
        DictResult = json.loads(result)
        return DictResult
