file = open("line.txt", "w")
check = " 167 "
for i in range(0,231) :
	if " " + str(i) + " " in check :
		file.write("1 ")
	else :
		file.write("0 ")