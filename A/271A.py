y = int(input()) + 1
while True:
	if len(set(str(y))) < 4:
		y += 1
	else:
		break
print(y)
