def option_01():
	l = []
	for i in range(2000, 3201):
		if i % 7 == 0 and i % 5 != 0:
			l.append(i)
	return l


def option_02():
	return [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]

print(option_01())
print(option_02())
