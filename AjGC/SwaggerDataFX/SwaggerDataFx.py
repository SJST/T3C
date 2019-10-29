from Z_Method import Method
class SwaggerData:

    def JudgeAddress(self,AjxxDict):
        Address = {}
        try:

            ajlb=AjxxDict.get("ajlb")
            if ajlb=="03":
               Address.update({"url":"172.18.15.249","port":"9001","Ajmc":"民事案件"})
            elif ajlb=="02":
               Address.update({"url": "172.18.15.249", "port": "11119","Ajmc":"刑事案件"})
            elif ajlb=="04":
                Address.update({"url": "172.18.15.153", "port": "9123","Ajmc":"行政案件"})
            elif ajlb == "05":
                Address.update({"url": "172.18.15.153", "port": "9123", "Ajmc": "赔偿案件"})
            elif ajlb == "01":
                Address.update({"url": "172.18.15.153", "port": "9123", "Ajmc": "管辖案件"})
            elif ajlb=="08":
                Address.update({"url": "172.18.15.153", "port": "9123", "Ajmc": "司法制裁"})
            else:
               pass
        except Exception as e:
            print("获取地址失败....")
            input("回车结束该任务!")
        return Address
    def SwaggerDataFx(self,Address,AjxxDict):
        docs=Method.Method().RequestAddress(Address)
        Ajmc=AjxxDict.get("Ajmc")
        Tags = docs.get("tags")



