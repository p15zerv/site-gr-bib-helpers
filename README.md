# site-gr-bib-helpers
Helper for ioniodi/site-gr that provides alternatives to bibtex format for bibliography.
This repository contains three python3 scripts that convert a `.bib` file to different formats. This `.bib` file contains data about books for university courses, which have been scraped from [Eudoxus](https://eudoxus.gr/). 

All converters require the `references.bib` file to be present in the same directory. Any `.bib` with a similar format should be compatible. The converters output corresponding files into the `conversions/` folder.

Make sure to install all of the listed requirements by running:
```
pip install -r requirements.txt
```

* `bib_to_json.py` 
  - Converts the `.bib` file to a `.json` file to be used in any general-purpose application.
  - Output: `conversions/references.json`.
* `bib_to_collection.py` 
  - Converts the `.bib` file to a set of `.md` files intended to be used as part of a Jekyll collection. 
  - Output: `conversions/books/`.
* `bib_to_data_yaml.py`
  - Converts the `.bib` file to a `.yml` file, which can be used as a data file in Jekyll.
  - Output: `conversions/books.yml`.
