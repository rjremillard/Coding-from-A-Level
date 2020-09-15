# one-liner

print("There are %d years in that range with a repeated digit" % sum([
	1 for i in range(int(input("Start: ")), int(input("End: ")) + 1) if len(dict.fromkeys(str(i))) < 4]))
