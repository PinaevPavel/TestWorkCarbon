import json, requests, psutil, time
starttime = time.time()

URL = input("Please enter the server URL [Default http://127.0.0.1:8001]\nPress enter to continue with the default settings. Or enter the address you need:") or "http://127.0.0.1:5000/hello"

while True:
	CPU = psutil.cpu_percent(interval=1)
	r = requests.post("http://127.0.0.1:8001", json={"utilization": CPU})
	print(CPU)
	time.sleep(10.0 - ((time.time() - starttime) % 10))

