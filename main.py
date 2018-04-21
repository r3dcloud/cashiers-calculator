from evdev import InputDevice, categorize, ecodes
from select import select
dev = InputDevice('/dev/input/event24')
flag = 1
a = ''
with dev.grab_context():
	while flag == 1:
		r,w,x = select([dev], [], [])
		for event in dev.read():
			if event.value == 1:
				if event.type == ecodes.EV_KEY:
					print(event)
					if event.code == 2:
						a += str('1')
					if event.code == 3:
						a += str('2')
					if event.code == 4:
						a += str('3')
					if event.code == 5:
						a += str('4')
					if event.code == 6:
						a += str('5')
					if event.code == 7:		
						a += str('6')
					if event.code == 8:
						a += str('7')
					if event.code == 9:
						a += str('8')
					if event.code == 10:
						a += str('9')
					if event.code == 11:
						a += str('0')
					if event.code == 28:
						flag = 0	
						pass

print(a)
