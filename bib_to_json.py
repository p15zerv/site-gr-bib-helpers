import bibtexparser
import json
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
with open('conversions/references.json', 'w') as f:
    output_str = json.dumps(entries, ensure_ascii=False, sort_keys=True,
                            indent=4, separators=(',', ': '))
    f.write(output_str)
