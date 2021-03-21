import numpy

MAX_CASHIERS = 10
MAX_SERVERS = 10
MAX_USHERS = 10
MAX_CUSTOMERS = 453



times = []
for cashiers in range(1, MAX_CASHIERS):
	for servers in range(1, MAX_SERVERS):
		for ushers in range(1, MAX_USHERS):
			times.append(((cashiers, servers, ushers), calc(cashiers, servers, ushers)))

print(times)
