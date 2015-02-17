testLst = ["krauty", "hello", "there"]
buff = ""
i = 0
for fld in testLst:
	if(i >=1):
		buff = buff + " "+ fld
	i = i+1
print(buff)