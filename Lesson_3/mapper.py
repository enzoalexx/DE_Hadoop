import sys
for line in sys.stdin:
	line = line.strip()
	words = line.split(',')
	try:
		word = words[7]
		price = words[5]
		print (word.lower()+'\t'+price)
	except Exception:
		continue
