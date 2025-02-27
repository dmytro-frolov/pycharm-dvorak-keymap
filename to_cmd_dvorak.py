#!/usr/bin/env python
"""
Bugfix Jetbrains keymaps for Dvorak keyboards.

Prereqs: pip install beautifulsoup4 lxml
"""

import argparse
from bs4 import BeautifulSoup

# below is the mapping to fix the messed up dvorak modifiers
#   the keys are dvorak keys
#   the values are what's usually on a qwerty keyboard in that key's position
REMAP = {
    'B': 'X',
    'C': 'J',
    'D': 'E',
    'E': 'PERIOD',
    'F': 'U',
    'G': 'I',
    'H': 'D',
    'I': 'C',
    'J': 'H',
    'K': 'T',
    'L': 'N',
    'N': 'B',
    'O': 'R', 
    'P': 'L',
    'Q': 'QUOTE',
    'R': 'P',
    'S': 'O', 
    'T': 'Y',
    'U': 'G',
    'V': 'K', 
    'W': 'COMMA', 
    'X': 'Q',
    'Y': 'F',
    'Z': 'SEMICOLON',
    'CLOSE_BRACKET': 'EQUALS', 
    'COMMA': 'W',
    'EQUALS': 'CLOSE_BRACKET', 
    'MINUS': 'OPEN_BRACKET', 
    'OPEN_BRACKET': 'SLASH', 
    'PERIOD': 'V',
    'QUOTE': 'MINUS',
    'SEMICOLON': 'S',
    'SLASH': 'Z',
    # part is responsible for replacing modifiers for macos
    # comment it for other os
    'control': 'meta', 
    'meta': 'control',
    'CONTROL': 'META',
    'META': 'CONTROL'
}

assert set(REMAP.keys()) == set(REMAP.values())

def read_keymap_infile(fname):
    with open(fname) as f:
        return BeautifulSoup(f.read(), features='xml')


def main(fname, outfname=None):
    soup = read_keymap_infile(fname)

    for node in soup.keymap.descendants:
        if node.name == 'action':
            action = node.attrs['id']
        if node.name == 'keyboard-shortcut':
            shortcut = node.attrs['first-keystroke']
            keys = shortcut.split()
            modifiers, key = keys[:-1], keys[-1].upper()
            # if not modifiers:
            #     # it's only modified keystrokes that are messed up (i.e. those with ctrl, alt, shift, or meta)
            #     continue
            if modifiers:

                for i, _key in enumerate(modifiers):
                    try:
                        #breakpoint()
                        modifiers[i] = REMAP[_key]
                    except KeyError:
                        pass
            try:
                new_key = REMAP[key]
                #breakpoint()
            except KeyError:
                # some keys, e.g. A and M, don't need any remapping
                continue
            new_shortcut = ' '.join(modifiers + [new_key])
            if outfname:
                print('Remapping {:35}: {} --> {}'.format(action, shortcut, new_shortcut))
            node.attrs['first-keystroke'] = new_shortcut

    old_name = soup.keymap.attrs.get('name')
    if old_name is not None:
        soup.keymap.attrs['parent'] = old_name
        soup.keymap.attrs['name'] = old_name + ' Dvorak'
    else:
        soup.keymap.attrs['name'] = 'Keymap Dvorak'

    if outfname:
        with open(outfname, 'w') as f:
            f.write(soup.keymap.prettify())
            f.write('\n')
        print('New keymap saved to {}'.format(outfname))
    else:
        print(soup.keymap.prettify())

    return soup


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', metavar='Keymap_Default.xml', help='Find them in e.g. <pycharm>/lib/resources.jar/idea/Keymap_*.xml')
    parser.add_argument('-o', '--outfile', help='Write to file instead of spamming output xml to stdout')
    args = parser.parse_args()
    main(fname=args.infile, outfname=args.outfile)
