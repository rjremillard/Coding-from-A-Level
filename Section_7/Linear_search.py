birdName = ["robin", "blackbird", "pigeon", "magpie", "bluetit", "thrush", "wren", "starling"]

toFind = input("What bird do you want? ")

found = False
for i in range(len(birdName) + 1):
	if birdName[i] == toFind:
		print("Found bird at %d" % i)
		found = True

if not found:
	print("Bird not found")
