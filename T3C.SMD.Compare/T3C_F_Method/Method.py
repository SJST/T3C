class Method:
    def LXChange(self,LX):
        LX_Dict={
            "CID":"VC",
            "RID":"VC",
            "N":"INT",
            "M":"N",
            "F":"INT",
            "D":"D",
            "DT":"DT",
            "Cn":"VC",
            "Cdx":"ARRAY VC",
            "Cgl":"ARRAY VC",
            "Cpc":"VC",
            "ID":"VC"

        }
        ChangeLX=dict(LX_Dict)[LX]
        return ChangeLX
