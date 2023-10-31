## OMEX Frog tools
This repository, holds a collection of tools to readily work with FROG files. 

The idea is to keep the library quite lightweight, so as to run with as few modules as possible. 

## installing
probably best done in a virtual environment: 

```bash
python3 -m venv venv
source ./venv/bin/activate
```

then either clone and install for editing: 

```bash

git clone https://github.com/fbergmann/omex-frog.git
cd omex-frog
pip install -e . 
```

or directly from github: 

```bash
pip install https://github.com/fbergmann/omex-frog.git
```

## Using

Not much to this project yet, just a file for guessing format identifiers: 

```
./venv/bin/guess_format ~/MODEL2211290003
```

would yield: 

```

MODEL2211290003
---------------

MM_bound
--------
manifest.xml http://identifiers.org/combine.specifications:omex-manifest

FROG
----

cobrapy
-------
02_fva.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
04_reaction_deletion 2.tsv http://identifiers.org/combine.specifications:frog-reactiondeletion-version-1
01_objective 2.tsv http://identifiers.org/combine.specifications:frog-objective-version-1
metadata 2.json http://identifiers.org/combine.specifications:frog-json-version-1
metadata.json http://identifiers.org/combine.specifications:frog-metadata-version-1
03_gene_deletion.tsv http://identifiers.org/combine.specifications:frog-genedeletion-version-1
frog.json http://identifiers.org/combine.specifications:frog-json-version-1
04_reaction_deletion.tsv http://identifiers.org/combine.specifications:frog-reactiondeletion-version-1
01_objective.tsv http://identifiers.org/combine.specifications:frog-objective-version-1
02_fva 2.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
frog 2.json http://identifiers.org/combine.specifications:frog-json-version-1

cameo
-----
02_fva.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
metadata.json http://identifiers.org/combine.specifications:frog-metadata-version-1
03_gene_deletion.tsv http://identifiers.org/combine.specifications:frog-genedeletion-version-1
frog.json http://identifiers.org/combine.specifications:frog-json-version-1
04_reaction_deletion.tsv http://identifiers.org/combine.specifications:frog-reactiondeletion-version-1
01_objective.tsv http://identifiers.org/combine.specifications:frog-objective-version-1
02_fva 2.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
frog 2.json http://identifiers.org/combine.specifications:frog-json-version-1
iMMM22IC_bound_Condition15.xml http://identifiers.org/combine.specifications:sbml
MM_unbound.omex http://identifiers.org/combine.specifications:omex
MM_bound.omex http://identifiers.org/combine.specifications:omex

MM_unbound
----------
iMMM22IC_unbound.xml http://identifiers.org/combine.specifications:sbml
manifest.xml http://identifiers.org/combine.specifications:omex-manifest

FROG
----

cobrapy
-------
02_fva.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
04_reaction_deletion 2.tsv http://identifiers.org/combine.specifications:frog-reactiondeletion-version-1
01_objective 2.tsv http://identifiers.org/combine.specifications:frog-objective-version-1
metadata 2.json http://identifiers.org/combine.specifications:frog-json-version-1
metadata.json http://identifiers.org/combine.specifications:frog-metadata-version-1
03_gene_deletion.tsv http://identifiers.org/combine.specifications:frog-genedeletion-version-1
frog.json http://identifiers.org/combine.specifications:frog-json-version-1
03_gene_deletion 2.tsv http://identifiers.org/combine.specifications:frog-genedeletion-version-1
04_reaction_deletion.tsv http://identifiers.org/combine.specifications:frog-reactiondeletion-version-1
01_objective.tsv http://identifiers.org/combine.specifications:frog-objective-version-1
02_fva 2.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
frog 2.json http://identifiers.org/combine.specifications:frog-json-version-1

cameo
-----
02_fva.tsv http://identifiers.org/combine.specifications:frog-fva-version-1
metadata.json http://identifiers.org/combine.specifications:frog-metadata-version-1
03_gene_deletion.tsv http://identifiers.org/combine.specifications:frog-genedeletion-version-1
frog.json http://identifiers.org/combine.specifications:frog-json-version-1
03_gene_deletion 2.tsv http://identifiers.org/combine.specifications:frog-genedeletion-version-1
04_reaction_deletion.tsv http://identifiers.org/combine.specifications:frog-reactiondeletion-version-1
01_objective.tsv http://identifiers.org/combine.specifications:frog-objective-version-1
```


### API

```python
>>> import omex_frog
>>> omex_frog.guess_format_uri('manifest.json')
'http://identifiers.org/combine.specifications:frog-json-version-1'
```
