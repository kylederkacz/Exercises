def capfirst(s):
	if not isinstance(s, str):
		return

	prev = ' '
	newstring = ''
	for c in s:
		if prev == ' ' and c != ' ':
			newstring = newstring + c.upper()
		else:
			newstring = newstring + c
		prev = c
	return newstring

print capfirst('this is a string')
print capfirst(' this is another string ')
print capfirst(' with   some strange      spacing')
print capfirst(None)
print capfirst(1)
