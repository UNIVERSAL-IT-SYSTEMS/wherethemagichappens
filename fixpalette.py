import codecs
from ast import literal_eval

file = codecs.open("colorpalette.txt", "r", "utf-8")
charlist = literal_eval(file.read())
file.close()
fixed = 0
print("Before:", len(charlist))

try:
	for i in range(len(charlist)):
		try :
			bytes(charlist[i][0][0], 'cp437')
		except UnicodeEncodeError:
			charlist.pop(i)
			fixed += 1
except IndexError:
	pass

out = codecs.open("colorpalette.txt", "w", "utf-8")
out.write(str(charlist))
out.close()
print("Fixed: "+str(fixed)+"Unicode errors")
print("After:", len(charlist))