#!/usr/bin/python3
import sys,getopt


def main(argv):
	weights=''
	image=''
	try:
		opts,args=getopt.getopt(argv,"hw:i:",["image=","weights="])
	except getopt.GetoptError:
		print('Usage: main.py -w <weights> -i <image>')
		sys.exit(2)
	if opts==[]:
		print('Usage: main.py -w <weights> -i <image>')
		sys.exit(2)
	for opt,arg in opts:
		if opt=='-h':
			print('Usage: main.py -w <weights> -i <image>')
			sys.exit()
		elif opt in ("-i","--image"):
			image=arg
		elif opt in ("-w","--weights"):
			weights=arg
	if weights!='' and image!='':
		import model
		model.predict(weights,image)
		sys.exit()

if __name__=='__main__':
	main(sys.argv[1:])

