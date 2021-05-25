from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	try:
		word, count = line.split('\t', 1)
	except Exception:
		continue
	try:
		count = int(count)
	except ValueError:
		continue
	if current_word == word:
		current_count += count
	else:
		if current_word:
			print (current_word+'\t'+str(current_count))
			current_count = count
			current_word = word
if current_word == word:
	print (current_word+'\t'+str(current_count))