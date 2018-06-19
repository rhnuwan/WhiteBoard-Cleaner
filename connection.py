from serial import Serial
import time


#send data
#  EN--X2--Y2--X1--Y1--ST
# OEN STOP all 
# OST START 
# EN - end 
# ST - start data packet
# CR -color RED
# CB - color BLUE
# CG - color Green
# S1 - side one
# S2 - side two
# S3 - side three
# S4 - side four

s = Serial('com4',9600)


def set_DT(i,x,y):
	s.writelines(i,'.',x,':',y)

def set_ST():
	s.writelines('ST')

def set_OST():
	s.writelines('OST')
def set_OEN():
	s.writelines('OEN')

def get_color():
	if s.readlines() == 'CR':
		color = 'red'
	elif s.readlines() == 'CB':
		color = 'blue'
	elif s.readlines() == 'CG':
		color = 'green'
	else:
		color = None
	return color

def get_Side():
	if s.readlines() == 'S1':
		side = 'S1'
	elif s.readlines() == 'S2':
		side = 'S2'
	elif s.readlines() == 'S3':
		side = 'S3'
	elif s.readlines() == 'S4':
		side = 'S4'
	else:
		side = None
	return side
