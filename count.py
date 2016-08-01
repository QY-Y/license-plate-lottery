import zipfile
import os
# def get_times():
# 	f = open("times.txt","r")
# 	times = []
# 	for line in f.readlines():
# 		line = line.replace("\n","")
# 		times.append(line)
# 	f.close()
# 	return times
def get_data():
	filelist = os.listdir(os.getcwd()+"/data/")
	filelist.sort()
	f = open("data.txt","a+")
	proceed = f.readlines()
	for info in proceed:
		info = info.split(" ")[0]
		if info in filelist>0:
			filelist.remove(info)
	for file in filelist:
		z = zipfile.ZipFile("./data/"+file, "r")
		for filename in z.namelist():
			if filename.find("NumberPeriod")>0:
				content = z.read(filename)
				content = content.split('\n')
				all_ = float(content[len(content)-3].replace("\r",""))
				plate_num = float(content[len(content)-2].replace("\r",""))
				rate = plate_num/all_
				line = file+" "+str(rate)+"\n"
				f.writelines(line)
				break
	f.close()
def caculate(num):
	filelist = os.listdir(os.getcwd()+"/data/")
	filelist.sort()
	failedrate = 1
	time_rate = {}
	for line in open("data.txt","r"):
		line = line.split(' ')
		time = line[0][24:30]
		time_rate[time] = line[1]
		copy = 0
		filename = 'PersonCommonNumberPeriod'+time+'.zip'
		z = zipfile.ZipFile("./data/"+filename, "r")
		for filename in z.namelist():
			if filename.find("ApplyNumber")>0:
				content = z.read(filename)
				if content.find(str(num))>0:
					copy += 1
		if not copy == 0:
			rate = float(time_rate[time]) * copy
			failedrate *= 1-rate
			print time+"\t"+rate+"\t"+copy+"\t"+failedrate
		else:
			print "missing",time



if __name__ == '__main__':
	num = '2937101329248'
	print "checking",num
	get_data()
	caculate(num)
	
	
	