import math, time, pyautogui

#Define part of the screen the program should search (START < END)
xMIN = 0
xMAX = 2560
yMIN = 0
yMAX = 1600

#Set what fraction of pixels should be checked
fractionCHECK = .01

#Enter target range of red, green, and blue in RGB value
rRANGE = range(0, 15)
gRANGE = range(115, 145)
bRANGE = range(0, 15)

#Set seconds pause after positive result
timePAUSE = 15

#Check a fraction of pixels to see if desired color is present
if __name__ == '__main__':
	jump = int(1/math.sqrt(fractionCHECK))
	xmaxval = int(round(xMAX-xMIN)/jump)
	ymaxval = int(round(yMAX-yMIN)/jump)
	triggered = 0

	while True:
		z = pyautogui.screenshot()
		for m in range(1, xmaxval):
			for n in range(1, ymaxval):
				x = xMAX - m*jump
				y = yMAX - n*jump
				color = z.getpixel((x, y))
				if color[0] in rRANGE and color[1] in gRANGE and color[2] in bRANGE:
					print("Found!" + "\a \nRed: " + str(color[0]) + ", Green: " + str(color[1]) + ", Blue: " + str(color[2]))
					time.sleep(timePAUSE)
					triggered = 1
					break
			if triggered == 1:
				triggered = 0
				break