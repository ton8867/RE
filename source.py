import re
import os

if(os.path.isdir('./data')):
	pass
else:
	os.mkdir('./data')
if (os.path.isfile('./data/config.txt')):
	pass
else:
	conf=open('./data/config.txt','a',encoding='utf_8')
	conf.write('_')
	conf.close
conf=open('./data/config.txt','r',encoding='utf_8')
a=conf.readline()
f1=open('./data/input.txt','a',encoding='utf_8')
f1.close

f = open('./data/output.txt', 'w',encoding='utf_8')
f1 = open('./data/input.txt','r',encoding='utf_8')

w=1

while w:

	w=f1.readline()
	m=re.search('{0}(.+?){0}'.format(a),w)
	if(m!=None):
		d=[m.group(1),'\n']
		f.writelines(d)
	else:
		f.write('[SYSTEM]End of File.')
f.close
f1.close
