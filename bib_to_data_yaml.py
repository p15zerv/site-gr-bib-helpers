import bibtexparser
import yaml
from pprint import pprint

# load bib
with open('references.bib') as f:
    bib_database = bibtexparser.load(f)
pprint(bib_database.entries)

# convert entry list to dictionary
entries = {}
for entry in bib_database.entries:
    id = entry.pop('ID')
    entry.pop('ENTRYTYPE')
    entry['author'] = entry['author'].replace('{', '').replace('}', '')
    entries[id] = entry

# convert dictionary to yaml and write to file
with open('conversions/books.yml', 'w') as f:
    output_str = yaml.dump(entries, encoding='utf-8', allow_unicode=True)
    output_str = output_str.decode('utf-8').replace('\nisbn_', '\n\n\nisbn_')
    f.write(output_str)
