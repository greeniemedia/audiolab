import wave
import struct
import math
import random
import time
import sys
import math

import pygame as pg

sampleRate = 44100.0 #hertz
#duration = 1.0 # seconds
duration = 0
frequency = 440.0 # hertz

#samples = [None] * frames
top = 32767
range_ = top*2

obj = wave.open("output.wav", 'w')
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(sampleRate)
def triangle_wave(frames, interval):
	samples = [None] * frames

	idiv2 = interval/2.0
	for i in range(frames):
		t = i%interval
		if (t<=idiv2):
			value = (range_ * (t/idiv2)) - top
		else:
			value = (((idiv2-(t-idiv2)) /idiv2) * range_) - top

		samples[i] = int(value)

	return samples

def ramp_wave(frames, interval):
	samples = [None] * frames

	for i in range(frames):
		value = int(((i%interval)*(range_/float(interval)))-top)
		samples[i] = int(value)

	return samples

def sine_wave(frames, interval):
	samples = [None] * frames

	R = math.pi * 2

	for i in range(frames):
		t = ((i%interval) / float(interval)) * R
		#print (t) 
		value = math.sin(t) * top
		#print(value)

		samples[i] = int(value)

	return samples

	
t = triangle_wave(1000*50, 1000)
r = ramp_wave(2000*50, 2000)

#s = triangle_wave(1000*500, 1000)
#for i in range(len(s)):
#	pass

#samples = t + r + t + r + r + t + t + r
#samples = triagle_wave(
#samples = t + t

mult = 10
samples = sine_wave(250*10*mult, 250) + sine_wave(100*15*mult, 100) + sine_wave(300*6*mult, 300) + sine_wave(150*10*mult, 150)

frames = len(samples)
	
for i in range(frames):
	#value = random.randint(-32767, 32767)

	value = samples[i]
	#print(value)
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
	#print(i)
	#print(points[i])
	#print(_points[len(_points)-1])


#print(_points)
#points = _points

pg.draw.lines(win, [255,0,255], False, _points, 2)
#pg.draw.lines(win, [0,255,0], True, [(0, 0), (500, 400), (1000, 0)], 4)
pg.display.flip()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

