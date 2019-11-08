#T3C PI08 对接研判 聚合接口 单接口数据比对
import re
import requests
import json
class CompareMethod:

    def data_list_one(self,test_url_one,h,parm1):
        response = requests.get(test_url_one, headers=h, params=parm1)
        response_text_one=response.text

        return response_text_one
    def data_list_two(self,test_url_tow,h,parm2):
        response = requests.get(test_url_tow, headers=h, params=parm2)
        response_text_two = response.text
        return response_text_two
    def data_compare(self,key,data1,data2):
        ListBig=[]
        ListSmall=[]
        ResultData=[]


        compare1 = ((json.loads(data1))).get(key)

        try:
            compare4=dict(compare1)
            compare2 = '{'+'"'+key+'"'+':' + data2 + '}'
            tmp_json = json.loads(compare2)


            compare3 = tmp_json.get(key)
            key1 = zip(compare3.keys(), compare3.values())
            key2 = zip(compare4.keys(), compare4.values())
           # print(sorted(key1))
           # print(sorted(key2))
           #  for small in key1:
           #      if small not in key2:
           #          print(small)
           #  print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(key1)
            print((key2))
            for x in key1:
                ListSmall.append(x)
            for y in key2:
                ListBig.append(y)
            for a in ListBig:
                if a not in ListSmall:

                    if type(a[1]) != dict or list:
                        if a[1] != None:
                            print("*"*50)
                            print(a)
                    elif type(a[1]) == dict:
                        x = a[1].values()
                        for i in list(x):
                            keyDict = (list(a[1].keys())[list(a[1].values()).index(i)])
                            if keyDict != None:
                                print("%s字典中缺少字段%s,值为%s" % (a[0], keyDict, i))
                    elif type(a[1]) == list:
                        for k in a[1]:
                            if type(k) == dict:
                                x = k.values()
                                for i in list(x):
                                    keyDict = (list(k.keys())[list(k.values()).index(i)])
                                    if keyDict != None:
                                        print("%s字典中缺少字段%s,值为%s" % (k, keyDict, i))
        except Exception as E:
            compare2 = '{' + '"' + key + '"' + ':' + data2 + '}'
            tmp_json = json.loads(compare2)
            compare3 = tmp_json.get(key)
            for i, item in enumerate(compare1):#聚合
                bh1 = item.get("bh")
                for a, items in enumerate(compare3):#其他
                    bh2 = items.get("bh")
                    if bh1 == bh2:
                        key1 = zip(item.keys(), item.values())
                        key2 = zip(items.keys(), items.values())#聚合接口
                        for x in key1:
                            ListSmall.append(x)
                        for y in key2:
                            ListBig.append(y)
            for a in ListBig:
                if a not in ListSmall:
                    if a [1]!=None:
                        print("*"*50)
                        print(a)
                    # if type(a[1])==dict:
                    #     x = a[1].values()
                    #     for i in list(x):
                    #         keyDict=(list(a[1].keys())[list(a[1].values()).index(i)])
                    #         if keyDict !=None:
                    #             print("%s字典中缺少字段%s,值为%s"%(a[0],keyDict,i))
                    # elif type(a[1])==list:
                    #     for k in a[1]:
                    #         if type(k)==dict:
                    #             x = k.values()
                    #             for i in list(x):
                    #                 keyDict = (list(k.keys())[list(k.values()).index(i)])
                    #                 if keyDict != None:
                    #                     print("%s字典中缺少字段%s,值为%s" % (k, keyDict, i))









        print("比较样本生成成功...")

        return ResultData

    def CompareMothod(self,ResultData):
        JHJKData=list(ResultData[0])
        QTJKData=list(ResultData[1])



    #test_url = "http://" + url_aj + ":" + port_aj + api

if __name__ == '__main__':
    # 类变量
    url1 = str(input("请输入比较地址1:"))
    url2 = str(input("请输入比较地址2："))
    key1 = str(input("请输入键值:"))
    p1={}
    p2={}
    global test1
    global test2
    if url1 and url2:
        add1=str(url1).split("?")
        add2=str(url2).split("?")
        test1="http://"+add1[0]
        test2="http://"+add2[0]
        B_parm1=add1[1].split("&")
        B_parm2=add2[1].split("&")
        for i in B_parm1:
            result1=i.split("=")

            if result1[0] == "limit" and "offset":
                p1.update({result1[0]: int(result1[1])})
            else:
                p1.update({result1[0]: result1[1]})
        for i in B_parm2:
            result2=i.split("=")
            if result2[0]=="limit" or"offset":
                p2.update({result2[0]:int(result2[1])})
            else:
                p2.update({result2[0]:result2[1]})


    h = {"Content-Type": "application/json"}

    one=CompareMethod().data_list_one(test1,h,p1)#聚合
    two=CompareMethod().data_list_two(test2,h,p2)
    ResultData=(CompareMethod().data_compare(key1,one,two))



