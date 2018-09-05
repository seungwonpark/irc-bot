import time

import initialize
import repeat
from config import *

conn, aclist = initialize.initialize()

while True:
	resp = repeat.repeat(conn, aclist)
	if resp == '<quit>':
		break
	time.sleep(1)
