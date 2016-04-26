# -*- coding: utf-8 -*-
"""
Where the magic happens
Copyright 2014 Mathieu Guimond-Morganti

Featuring some of the ugliest code I've ever written,
long before I had taken an actual programming course.
I'm not proud of this code, but hey, it *technically* works.
Good enough.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import multiprocessing

import datetime

from PIL import Image

from colorama import Fore, Back, Style, init
from random import randrange, random

import networkx
from colormath.color_objects import LabColor, sRGBColor, XYZColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976

import codecs

def initializeProgram():

	init(autoreset=True)
	# os.system('chcp 850 > nul')
	if __name__ == '__main__':
		os.system('cls')

		print(Fore.YELLOW + Back.RED + Style.BRIGHT +" ************************************************** ")
		print(Fore.YELLOW + Back.RED + Style.BRIGHT +" **  Please maximize the command prompt window.  ** ")
		print(Fore.YELLOW + Back.RED + Style.BRIGHT +" **        Then, press CTRL+C to continue.       ** ")
		print(Fore.YELLOW + Back.RED + Style.BRIGHT +" ************************************************** ")

		try:
			os.system('wmic')
			# os.system('chcp 850 > nul')
			os.system('cls')
		except KeyboardInterrupt:
			# os.system('chcp 850 > nul')
			os.system('cls')
			## COPYRIGHT NOTICE:
			print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+'''\n'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + ''' '''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + ''' '''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.RED + Back.BLUE + Style.BRIGHT + ''' '''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''T'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''h'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''e'''+Fore.RED + Back.BLUE + Style.BRIGHT + ''' '''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''E'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''l'''+Fore.WHITE + Back.BLUE +Style.BRIGHT + '''e'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''c'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''t'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''r'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''o'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''n'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''i'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''c'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''K'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''o'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''o'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''l'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''-'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''A'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''i'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''d'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + ''' '''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''A'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''S'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''C'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''I'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''I'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''T'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''e'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''s'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''t'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + ''' '''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''1'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''.'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''0'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.GREEN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.GREEN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+'''\n'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + ''' '''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + ''' '''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.CYAN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.RED + Back.BLUE + Style.BRIGHT + '''('''+Fore.RED + Back.BLUE + Style.BRIGHT + '''c'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + ''')'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''2'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''0'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''1'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''4'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + ''' '''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''M'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''a'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''t'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''h'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''i'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''e'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''u'''+Fore.WHITE + Back.BLUE + Style.BRIGHT+ ''' '''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''G'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''u'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''i'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''m'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''o'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''n'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''d'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''-'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''M'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''o'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''r'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''g'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''a'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''n'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''t'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''i'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.GREEN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.BLACK + Back.BLUE + Style.BRIGHT + ''' '''+Fore.BLACK + Back.BLUE + Style.BRIGHT + ''' '''+Fore.GREEN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.WHITE + Back.BLUE + Style.BRIGHT + ''' '''+Fore.GREEN + Back.BLUE + Style.BRIGHT + ''' '''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+'''\n'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.GREEN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLUE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.WHITE + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.RED + Back.BLUE + Style.BRIGHT + '''*'''+Fore.YELLOW + Back.BLUE + Style.BRIGHT + '''*'''+Fore.MAGENTA + Back.BLUE + Style.BRIGHT + '''*'''+Fore.BLACK + Back.BLUE + Style.BRIGHT + '''*'''+Fore.CYAN + Back.BLUE + Style.BRIGHT + '''*''')
		# image = Image.open('input.png').load()

		init(autoreset=False)
		print(Fore.BLUE + Back.WHITE + Style.NORMAL, end="")
		input_image = input(" What is the filename of the image? (default: input.png) \n ")
		if len(input_image) == 0: 
			input_image = "input.png"
			workingfile = codecs.open("temp"+str(os.getpid())+".txt", "w", "utf-8")
			workingfile.write("\'\'\'"+input_image+"\'\'\'")
			image = Image.open('input.png') # .load moved to getAverageLabColor(x,y, dx, dy, image)
		else :
			workingfile = codecs.open("temp"+str(os.getpid())+".txt", "w", "utf-8")
			workingfile.write("\'\'\'"+input_image+"\'\'\'")
			image = Image.open(input_image)
		init(autoreset=True)
	else: # if a worker thread
		input_image = codecs.open("temp"+str(os.getppid())+".txt", "r", "utf-8") # os.getpid() = child, os.getppid() = parent
		input_image = eval(input_image.read())
		image = Image.open(input_image)
	
	file = codecs.open("colorpalette.txt", "r", "utf-8")
	charlist = eval(file.read())
	
	return image, charlist

# print(charlist)
# print(len(charlist))
# print(charlist[533])
# print(len(charlist[533]))
# print(charlist[533][1])
# print(len(charlist[533][1]))
# print(charlist[533][1][2]) # e.g. [533] is the 534th character as a list, [533][1] is its Lab color as tuple, [533][1][2] is its b value as a float

### Reference color.
# color1 = LabColor(lab_l=0.9, lab_a=16.3, lab_b=-2.22)
### Color to be compared to the reference.
# color2 = LabColor(lab_l=0.7, lab_a=14.2, lab_b=-1.80)
### This is your delta E value as a float.
# delta_e = delta_e_cie1976(color1, color2)

def getAverageLabColor(x,y, dx, dy, image):
	""" Returns a 3-tuple containing the Lab value of the average color of the
	given square bounded area of length = dx, height = dy whose origin (top left corner) 
	is (x, y) in the given."""
	red, green, blue, alpha = 0, 0, 0, 0
	l, a, b = 0, 0, 0
	count = 0
	# image = image.load()
	for s in range(x, x+dx):
		for t in range(y, y+dy):
			try :
				pixel_red, pixel_green, pixel_blue, pixel_alpha = image[s, t]
			except :
				pixel_red, pixel_green, pixel_blue = image[s, t]
			
			rgb = sRGBColor(pixel_red, pixel_green, pixel_blue, True)
			xyz = convert_color(rgb, XYZColor)
			lab = convert_color(xyz, LabColor)
			
			pixel_l, pixel_a, pixel_b = lab.get_value_tuple()
			l += pixel_l
			a += pixel_a
			b += pixel_b
			count += 1
	return ((l/count), (a/count), (b/count))
	
def imageManip(image):
	input_grid = []
	i = 0
	width, height = image.size
	if (width%8) != 0:
		print(Fore.BLACK + Back.YELLOW + Style.NORMAL + " The width isn't a multiple of 8.", end="")
	if (height%12) != 0:
		print(Fore.BLACK + Back.YELLOW + Style.NORMAL + " The height isn't a multiple of 12.", end="")
	if (width%8) != 0 or (height%12) != 0:
		print(Fore.BLACK + Back.YELLOW + Style.NORMAL + " The image will be cropped. ")
	width, height = (int(width/8)*8), (int(height/12)*12)
	image = image.crop((0,0,width,height))
	image = image.load() #remove if buggy and put back in getAverageLabColor
	while i < ((width*height)/(8*12)):
		print("\r" + Fore.BLUE + Back.WHITE + Style.NORMAL + " Averaging the colour of sample "+str(i+1)+"/"+str(int(((width*height)/(8*12))))+" of the input image. "+Fore.WHITE + Back.BLUE + Style.BRIGHT+" ("+str(int((i)/((width*height)/(8*12))*100))+"%) "+Fore.WHITE + Back.RED + Style.NORMAL+" This might take a while. ", end="")
		l, a, b = getAverageLabColor(int(8*(i%(width/8))),int(12*int((8*i)/width)), 8, 12, image)
		input_grid.append((l,a,b))
		i += 1
	print("\r" + Fore.BLUE + Back.WHITE + Style.NORMAL + " Averaging the colour of sample "+str(i)+"/"+str(int(((width*height)/(8*12))))+" of the input image. "+Fore.WHITE + Back.BLUE + Style.BRIGHT+" ("+str(int((i)/((width*height)/(8*12))*100))+"%) "+Fore.WHITE + Back.RED + Style.NORMAL+" This might take a while. ")
	return (input_grid, width, height)

def findBestCharacter(l, a, b, sample_number=1, total_samples=1, verbose=True):
	# input_rgb = sRGBColor(33, 78, 60, True) #couleur test orange brique/ocre (191,73,10,True)
	# input_xyz = convert_color(input_rgb, XYZColor)
	# input_lab = convert_color(input_xyz, LabColor)
	input_lab = LabColor(l, a, b)
	smallest_delta_e = float("inf")
	best_character = []
	permutation = 0
	for ref_char in charlist:
		permutation += 1
		char, fg, bg, intensity = ref_char[0]
		if verbose == True:
			print("\r" + Fore.BLUE + Back.WHITE + Style.NORMAL + " Comparing "+ eval('''Fore.'''+fg+''' + Back.'''+bg+''' + Style.'''+intensity+''' + \'\'\''''+char+'''\'\'\'''') + Fore.BLUE + Back.WHITE + Style.NORMAL+" "+str(permutation)+"/"+str(len(charlist))+" with sample "+str(sample_number)+"/"+str(total_samples)+". "+Fore.WHITE + Back.BLUE + Style.BRIGHT+" ("+str(int(((sample_number - 1)/total_samples+permutation/len(charlist)*1/total_samples)*100))+"%) "+Fore.WHITE + Back.RED + Style.NORMAL+" This WILL take a while. ", end="")
		l, a, b = ref_char[1]
		ref_lab = LabColor(l, a, b)
		delta_e = delta_e_cie1976(input_lab, ref_lab)
		if delta_e < smallest_delta_e :
			smallest_delta_e = delta_e
			best_character = []
			best_character.append(ref_char[0])
		elif delta_e == smallest_delta_e:
			best_character.append(ref_char[0])
		else :
			pass
	return best_character
	
def findBestCharacterParallel(input_color, sample_number=1, total_samples=1):
	l, a, b = input_color
	# input_rgb = sRGBColor(33, 78, 60, True) #couleur test orange brique/ocre (191,73,10,True)
	# input_xyz = convert_color(input_rgb, XYZColor)
	# input_lab = convert_color(input_xyz, LabColor)
	input_lab = LabColor(l, a, b)
	smallest_delta_e = float("inf")
	best_character = []
	permutation = 0
	for ref_char in charlist:
		permutation += 1
		char, fg, bg, intensity = ref_char[0]
		## BUGGY IN PARALLEL, NEEDS TO BE FIXED:
		# print("\r" + Fore.BLUE + Back.WHITE + Style.NORMAL + " Comparing "+ eval('''Fore.'''+fg+''' + Back.'''+bg+''' + Style.'''+intensity+''' + \'\'\''''+char+'''\'\'\'''') + Fore.BLUE + Back.WHITE + Style.NORMAL+" "+str(permutation)+"/"+str(len(charlist))+" with sample "+str(sample_number)+"/"+str(total_samples)+". "+Fore.WHITE + Back.BLUE + Style.BRIGHT+" ("+str(int(((sample_number - 1)/total_samples+permutation/len(charlist)*1/total_samples)*100))+"%) "+Fore.WHITE + Back.RED + Style.NORMAL+" This WILL take a while. ") #removed ,end=""
		##WORKAROUND:
		# statusbar = ["\\","|","/","-"]
		# print("\r"+statusbar[permutation%len(statusbar)], end="")
		l, a, b = ref_char[1]
		ref_lab = LabColor(l, a, b)
		delta_e = delta_e_cie1976(input_lab, ref_lab)
		if delta_e < smallest_delta_e :
			smallest_delta_e = delta_e
			best_character = []
			best_character.append(ref_char[0])
		elif delta_e == smallest_delta_e:
			best_character.append(ref_char[0])
		else :
			pass
	return best_character

def printOutputText(image):
	# os.system('chcp 850 > nul')
	grid, width, height = imageManip(image)
	output = []
	sample_number = 0
	for input_color in grid :
		sample_number += 1
		l, a, b = input_color
		output.append(findBestCharacter(l, a, b, sample_number, int(((width*height)/(8*12)))))
	i = 0
	os.system('cls')
	print("")
	# print(len(output) == ((width*height)/(8*12)))
	for color in output:
		char, fg, bg, intensity = color[randrange(len(color))]
		if i % (width/8) == 0:
			print("")
		exec('''print(Fore.'''+fg+''' + Back.'''+bg+''' + Style.'''+intensity+''' + \'\'\''''+char+'''\'\'\', end="")''')
		i += 1
	print("")
	os.system('pause')
	
def printOutputTextParallel(image):
	# os.system('chcp 850 > nul')
	grid, width, height = imageManip(image)
	output = []
	# sample_number = 0
	if __name__ == '__main__':
		print(Fore.BLUE + Back.WHITE + Style.NORMAL+" Matching each sample of the input image to a coloured character. ")
		starttime = datetime.datetime.now()
		findBestCharacterParallel((28.26223883969351, 49.90677151721382, 27.198472821976473))
		endtime = datetime.datetime.now()
		print(Fore.BLUE + Back.WHITE + Style.NORMAL+" Diving the workload between "+str(multiprocessing.cpu_count())+" workers. ")
		print(Fore.BLUE + Back.WHITE + Style.NORMAL+" Estimated time to complete: "+str((endtime - starttime)*len(grid)/int(multiprocessing.cpu_count()))+" ")
		with multiprocessing.Pool() as pool:		 # start optimal nb of worker processes, otherwise specify Pool(processes=4) or Pool(multiprocessing.cpu_count())
			output = pool.map(findBestCharacterParallel, grid)
	# for input_color in grid :
		# sample_number += 1
		# l, a, b = input_color
		# output.append(findBestCharacter(l, a, b, sample_number, int(((width*height)/(8*12)))))
	i = 0
	os.system('cls')
	print("")
	# print(len(output) == ((width*height)/(8*12)))
	for color in output:
		char, fg, bg, intensity = color[randrange(len(color))]
		if i % (width/8) == 0:
			print("")
		exec('''# os.system('chcp 850 > nul')\nprint(Fore.'''+fg+''' + Back.'''+bg+''' + Style.'''+intensity+''' + \'\'\''''+char+'''\'\'\', end="")''')
		i += 1
	print("\n")
	if __name__ == '__main__':
		os.remove("temp"+str(os.getpid())+".txt")
	os.system('pause')

# print(best_character)

# x = 0
# while x < 256:
	# char, fg, bg, intensity = best_character[randrange(len(best_character))]
	# eval('''print(Fore.'''+fg+''' + Back.'''+bg+''' + Style.'''+intensity+''' + \'\'\''''+char+'''\'\'\', end="")''')
	# if (x+1)%16 == 0:
		# print("")
	# x += 1

# for character in best_character:
	# char, fg, bg, intensity = character
	# eval('''print(Fore.'''+fg+''' + Back.'''+bg+''' + Style.'''+intensity+''' + \'\'\''''+char+'''\'\'\', end="")''')
	
# print(imageManip(image))

image, charlist = initializeProgram()

if __name__ == '__main__':
	printOutputTextParallel(image)