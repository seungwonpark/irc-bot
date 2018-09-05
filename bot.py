import time

import initialize
import repeat
from config import *

conn = initialize.initialize()

while True:
	resp = repeat.repeat(conn)
	if resp == '<quit>':
		break
	time.sleep(1)
