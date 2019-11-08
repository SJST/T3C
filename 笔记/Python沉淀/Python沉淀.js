//Python 沉淀
1.sort和sorted函数
2.Python转换zipobject
3.查看一个变量的相关属性
	/*
		函数dir
	*/
4.Python字符串转dict
	/*eval 函数*/
5.Python.xlrd操作Excel
/*
1.获取Execl的sheet数量
	import xlrd
	b = xlrd.open_workbook('path/to/excel')
	count = len(b.sheets()) #sheet数量
	for sheet in b.sheets():
		print sheet.name #sheet名称
*/