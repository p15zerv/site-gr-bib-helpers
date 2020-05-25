import bibtexparser
import frontmatter
from pprint import pprint

# load bib
with open('references.bib') as f:
    bib_database = bibtexparser.load(f)
pprint(bib_database.entries)

for entry in bib_database.entries:
    # reformat entry
    id = entry.pop('ID')
    entry['ref'] = id
    entry.pop('ENTRYTYPE')
    entry['layout'] = 'bibtex'
    entry['author'] = entry['author'].replace('{', '').replace('}', '')
    # create frontmatter with metadata
    post = frontmatter.Post('', **entry)
    # write as collection file
    with open('conversions/books/' + id + '.md', 'wb') as f:
        frontmatter.dump(post, f)
