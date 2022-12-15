# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.

from argparse import ArgumentParser, RawTextHelpFormatter
import yaml
__author__ = "Doron Chosnek"
__copyright__ = "Copyright (c) 2022 Doron Chosnek."
__license__ = "GNU General Public License, Version 3"


# Recursive function taken from a blog:
# https://medium.com/better-programming/how-to-recursively-parse-api-responses-using-python-126824426b18
# This function uses the concept of the remove_empty_string function from that
# blog but adds a Python dictionary pop command to remove the specified key.
# If the specified key does not exist, the pop command has no affect. A
# recursive function is necessary to traverse a deeply nested dictionary.
def remove_key(d, offensive_key):
    if isinstance(d, dict):
        d.pop(offensive_key, None)   # remove the key
        for k in d.keys():
            d[k] = remove_key(d[k], offensive_key)
        return d
    elif isinstance(d, list):
        for i in range(len(d)):
            d[i] = remove_key(d[i], offensive_key)
        return d
    else:
        # if it's not a dict or list, then it doesn't need to be changed
        return d


parser = ArgumentParser(
    description='removes the specified key from all YAML documents in a file',
    epilog="Example: python yaml_remove_key.py status metal.yaml\n\nOutput is dumped to the screen, so you must redirect it to a file.\n ",
    formatter_class=RawTextHelpFormatter
)
parser.add_argument('key', help='name of the key to remove')
parser.add_argument('filename', help='path to file to modify')
args = parser.parse_args()

# yaml file might include multiple yaml documents
with open(args.filename, 'r') as file:
    documents = yaml.load_all(file.read(), Loader=yaml.FullLoader)

# remove the specified key from each yaml document, one at a time, and save
# to a list to dump to screen later
updated = []
for doc in documents:
    updated.append(remove_key(doc, args.key))

# send cleaned yaml to the screen
print(yaml.dump_all(updated))
