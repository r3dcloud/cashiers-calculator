from evdev import InputDevice, categorize, ecodes
from select import select
dev = InputDevice('/dev/input/event19')
flag = 1
chunk = ''
product_code = ''
suma = float(0)
price = float(0)
with dev.grab_context():
	while flag == 1:
		r,w,x = select([dev], [], [])
		for event in dev.read():
			if event.value == 1:
				if event.type == ecodes.EV_KEY:
					#print(event)
					if event.code == 2:
						chunk += str('1')
					if event.code == 3:
						chunk += str('2')
					if event.code == 4:
						chunk += str('3')
					if event.code == 5:
						chunk += str('4')
					if event.code == 6:
						chunk += str('5')
					if event.code == 7:		
						chunk += str('6')
					if event.code == 8:
						chunk += str('7')
					if event.code == 9:
						chunk += str('8')
					if event.code == 10:
						chunk += str('9')
					if event.code == 11:
						chunk += str('0')
					if event.code == 28:
						product_code = chunk 
						chunk = '' 
						#print(product_code)	
						#find = open('products', 'r')
						#for line in find:
						#	if product_code in line: 
						#		product_code, product, prices = line.split(':')
						#find.close()
						#float(suma)
						#price = float(prices)
						print product_code
						f = open('products', 'a')
						f.write(product_code + ':' + raw_input('item:') + ':' + raw_input('price:') + '\n')
						f.close()
						print('=====BREAK=====')
					        #suma = suma + price
						#print suma 
						#continue

