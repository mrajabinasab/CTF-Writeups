import os
import base64
from zipfile import ZipFile


i=1
while i==1:
	for f in os.listdir('.'):
		if f.endswith(".zip"):
			p = os.path.splitext(f)[0]
			passw2 = base64.b64decode(p)
			passw = passw2.decode('utf-8')
			with ZipFile(f) as zf:
				zf.extractall(pwd=bytes(passw))
			print(f)
            os.remove(f)