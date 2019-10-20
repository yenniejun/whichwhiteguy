## Which White Guy Do YOU Write Like?

The purpose of this script is to create an input to train an NLP model that will be
able to predict which white guy's writing style you emulate the most.

I get the short stories (at random, for now, so not the best method) from several authors
from the 19th and 20th centuries using the [Gutenberg API](https://github.com/c-w/gutenberg/).

Currently the authors I'm using are:
	* Nathaniel Hawthorne
	* Edgar Allan Poe
	* Oscar Wilde
	* H. G. Wells
	* Mark Twain
	* Leo Tolstoy
	* Rudyard Kipling
	* Thomas Hardy
	* Arthur Conan Doyle

## Things to improve:
 * Chunking of texts. Right now I'm just getting 1000-word long chunks for each
   text. Might be an improvement to chunk based on section (i.e. based on chapter
   or separate short story. Could scrape the table of contents for page numbers
   or chapter names and such)
 * More texts for each author. Right now I got one short story collection for each
   author but I should mix in short storeis and long-form from different periods in
   their life as well
 * Choose a more comprehensive list of authors?

