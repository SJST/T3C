#根据用户输入生成dictory
import re
from Z_Method import Method
class UserInput:
    def UserInputAjxx(self):
        RelyData={}
        #输入业务类型 判断案件类型,自定义业务类型
        ywlx=str(input("请输入业务类型:"))
        jbfy=str(input("请输入经办法院(高院,中院,基层院):"))
        ajjd=str(input("请输入案件阶段(立案/办案)"))
        sfbhdsr=str(input("是否需要创建当事人(Y/N)"))
        ZDYDict=Method.Method().AddDefineXX(RelyData)
        RelyData.update(ZDYDict)
        RelyData.update({"ywlx":ywlx,"jbfy":jbfy,"ajjd":ajjd,"sfbhdsr":sfbhdsr})
        return RelyData
    def GGDict(self,RelyData):
        ywlx=RelyData.get("ywlx")
        jbfy=RelyData.get("jbfy")
        GGDict={"ywlx":ywlx,"jbfy":jbfy}
    def YwlxXX(self,RelyData):
        Ywlx=RelyData.get("ywlx")
        ajlb = re.match("\d{2}", Ywlx).group()
        RelyData.update({"ajlb":ajlb})
    def JbfyXX(self,RelyData):
        Jbfy=RelyData.get("jbfy")
        FYXXDict = {}
        if Jbfy=="高院":
            FYXXDict.update({"jbfy":"2400","cbr":"157286789","cbspt":"157286406"})
        elif Jbfy=="中院":
            pass#待补充 中院 中院李凯伦
        else:
            pass#待补充 基层院 基层李凯伦
        RelyData.update(FYXXDict)
        return FYXXDict
    def AjjdXX(self,RelyData):
        AjjdXX=RelyData.get("ajjd")
        if AjjdXX=="办案":
            ajjzjd=6
            RelyData.update({"ajjzjd":ajjzjd})
        else:
            pass#待补充,立案是否ajjzjd=2
        return
    def DsrXX(self,RelyData,GGDict):
        DsrList = []
        SFBHDSR=RelyData.get({"sfbhdsr"})
        if SFBHDSR=="Y":
            DsrNum=int("需要几个当事人?")
            if DsrNum>0:
                for i in range(0,DsrNum+1):

                    DsrDict={}
                    MC="第"+str(i)+"人"
                    print(MC+":")
                    ZDYDict = Method.Method().AddDefineXX(DsrDict)
                    ZDYDict.update(GGDict)
                    DsrList.append(ZDYDict)
        return DsrList




'''
 最后需要的结果 案件 dict dsr list 
'''
