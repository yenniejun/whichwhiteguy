from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import math
import csv
import pandas as pd

CHUNK_SIZE = 1000
AUTHOR = "author"
TEXT_CHUNK = "text_chunk"


df = pd.DataFrame([], columns=(AUTHOR, TEXT_CHUNK))


text = strip_headers(load_etext(2701)).strip()
print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'

hawthorne = get_text_from_gutenberg(512)
poe = get_text_from_gutenberg(25525)
wilde = get_text_from_gutenberg(902)
wells = get_text_from_gutenberg(59774)
twain = get_text_from_gutenberg(142)
tolstoy = get_text_from_gutenberg(689)
kipling = get_text_from_gutenberg(32488)
hardy = get_text_from_gutenberg(3056)
doyle = get_text_from_gutenberg(294)

texts = {'hawthorne':hawthorne, 'poe':poe, 'wilde':wilde,'wells':wells,
	'twain':twain,'tolstoy':tolstoy,'kipling':kipling,'hardy':hardy,'doyle':doyle}

texts = {'hawthorne':hawthorne}


for text in texts:
	text_chunk_df = get_text_chunk_df(key, texts[key])
	df = df.append(text_chunk_df)


# Returns the ebook from the index
# The first 1000 characters are thrown away (usually table of contents, etc)
# The split by words, and shave off the last bit of the ending that doesn't divide by 1000
# Return a truncated version of the text, num words divisible by 1000
def get_text_from_gutenberg(index):
	text = strip_headers(load_etext(index)).strip()
	split_by_space = text.split()

	# Lazy way of text cleaning:
	# Ditch the first 1000 characters of each because that's most of the
	# introduction and random metadata I don't feel like cleaning right now
	# But eventually, I should clean this and return a better cleaned version
	# For the ending, stripping the mod so that the result has a number easily divislbe by 1000

	ending = len(split_by_space) - len(split_by_space) % CHUNK_SIZE
	return split_by_space[CHUNK_SIZE:ending]


def get_text_chunk_df(author, text):
	text_len = len(text)
	for i in range(0, text_len, CHUNK_SIZE):
		# Save to pandas df
		text_chunk = text[i:i+(CHUNK_SIZE-1)]
		return pd.DataFrame([[author, text_chunk]], columns=(AUTHOR, TEXT_CHUNK))
