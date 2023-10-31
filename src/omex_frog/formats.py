import sys
import os.path

SKIP = [
    '__MACOSX'
]

TRANSFORM = [
    {'00_meta', 'meta'}
]

IDENTIFIERS_PREFIX = "http://identifiers.org/combine.specifications:"
PURL_PREFIX = "http://purl.org/NET/mediatypes/"

FROG_JSON_V1 = IDENTIFIERS_PREFIX + "frog-json-version-1"
FROG_METADATA_V1 = IDENTIFIERS_PREFIX + "frog-metadata-version-1"
FROG_OBJECTIVE_V1 = IDENTIFIERS_PREFIX + "frog-objective-version-1"
FROG_FVA_V1 = IDENTIFIERS_PREFIX + "frog-fva-version-1"
FROG_GENEDELETION_V1 = IDENTIFIERS_PREFIX + "frog-genedeletion-version-1"
FROG_REACTIONDELETION_V1 = IDENTIFIERS_PREFIX + "frog-reactiondeletion-version-1"
FROG_MINIFROG_V1 = IDENTIFIERS_PREFIX + "frog-minifrog-version-1"

SBML = IDENTIFIERS_PREFIX + "sbml"
OMEX = IDENTIFIERS_PREFIX + "omex"
OMEX_MANIFEST = IDENTIFIERS_PREFIX + "omex-manifest"

ZIP = PURL_PREFIX + "application/zip"


def guess_format_uri(filename):
    """Guess the format of the input file based on the file
    
    The detection uses some heuristics to guess the format of the file.

    for example: 
    
    >>> import omex_frog
    >>> omex_frog.guess_format_uri('manifest.json')
    'http://identifiers.org/combine.specifications:omex-manifest'
    

    """
    basename = os.path.basename(filename)
    extension = filename.split(".")[-1]

    for substring, replacement in TRANSFORM:
        basename = basename.replace(substring, replacement)

    if basename == 'metadata.json':
        return FROG_METADATA_V1
    if basename == 'manifest.xml':
        return OMEX_MANIFEST
    if extension == "json":
        return FROG_JSON_V1
    if extension == 'tsv':
        if basename.startswith('01_'):
            return FROG_OBJECTIVE_V1
        if basename.startswith('02_'):
            return FROG_FVA_V1
        if basename.startswith('03_'):
            return FROG_GENEDELETION_V1
        if basename.startswith('04_'):
            return FROG_REACTIONDELETION_V1
    if extension == 'xlsx':
        return FROG_MINIFROG_V1

    if extension == 'omex':
        return OMEX

    if extension == 'xml':
        return SBML

    if extension == 'zip':
        return OMEX


def print_types_in_dir(directory):
    """Print the type of all files in a directory"""
    print()
    print(os.path.basename(directory))
    print('-' * len(os.path.basename(directory)))

    for filename in os.listdir(directory):
        full_name = os.path.join(directory, filename)

        if filename in SKIP:
            continue

        if os.path.isdir(full_name):
            print_types_in_dir(full_name)
            continue

        print(filename, guess_format_uri(filename))


def main():
    directory = sys.argv[1]

    # recursively walk through the directory
    print_types_in_dir(directory)


if __name__ == "__main__":
    main()
