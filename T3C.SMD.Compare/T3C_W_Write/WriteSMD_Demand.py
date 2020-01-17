class Write_SMD_Demand:
    def WriteDiffZD(self,DirName,LocationTime,TitleDemand,fileName,TitleSMD,WriteList):
        a=str(DirName).split("3")[1]#T3C民事案件
        b="..\\T3C_AR_Result\\"
        path =b +"\\"+ a + LocationTime + fileName + ".txt"
       # path="../T3C_AR_Rrsult\\"+DirName+"\\"+a+LocationTime+fileName+".txt"
        SMD_Demand=dict(WriteList).get("S_Demand")
        Demand_SMD=dict(WriteList).get("S_SMD")
        flie=open(path,"w+",encoding="utf-8")
        flie.write(TitleDemand+"\n")
        flie.write(str(Demand_SMD)+"\n")
        flie.write(TitleSMD+"\n")
        flie.write(str(SMD_Demand))
        flie.close()
        print("文件写入完成....")

