import wave
import struct
import math
import random
import time
import sys

import pygame as pg

sampleRate = 44100.0 #hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
frames = 99999

samples = [None] * frames
top = 32767
range_ = top*2

obj = wave.open("output.wav", 'w')
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(frames):
	#value = random.randint(-32767, 32767)
	#value = int(((i%2000)*(range_/2000.0))-top)
	t = i%4000
	if (t<=2000):
		value = (range_ * (t/2000.0)) - top
	else:
		value = (((2000-(t-2000)) /2000.0) * range_) - top

	samples[i] = int(value)
	data = struct.pack('<h', int(value))
	obj.writeframesraw(data)

obj.close()

res = [1920, 768]

pg.init()
win = pg.display.set_mode(res)
points = [None] * frames
for i in range(frames):
	points[i] = [None, None]
	points[i][0] = (i/float(frames)) * res[0]
	#points[i][1] = ((samples[i]/float(top))*(res[1]/2))+(res[1]/2)
	points[i][1] = res[1]-(((top+samples[i])/(range_))*res[1])
	#print(points[i][0], points[i][1])
	#print(points[i])

_points = []
for i in range(0, frames, 200):
	_points.append(points[i])
	#print(i)
	print(i)
	print(points[i])
	print(_points[len(_points)-1])


print(_points)
#points = _points

pg.draw.lines(win, [255,0,255], False, _points, 2)
#pg.draw.lines(win, [0,255,0], True, [(0, 0), (500, 400), (1000, 0)], 4)
pg.display.flip()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

