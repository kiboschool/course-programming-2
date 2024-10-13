

from ben_python_common import *
txt = files.readall('../src/SUMMARY.md', encoding='utf-8')
lines = txt.replace('\r\n', '\n').split('\n')
for i, line in enumerate(lines):
    if line.startswith('  - [xxx]'):
        path = line.split('(')[1].split(')')[0]
        pathParts = path.split('/')
        leaf = pathParts[-1].replace('.md', '')
        leafParts = leaf.split('-')
        for j, leafPart in enumerate(leafParts):
            leafParts[j] = leafPart[0].upper() + leafPart[1:]
        title = ' '.join(leafParts)
        replaceWith = f'  - [{title}]'
        lineOut = line.replace('  - [xxx]', replaceWith)
        trace(lineOut)
        # [xxx](lessons/classes-and-objects/methods.md)
        
        lines[i] = lineOut

outTxt = '\n'.join(lines)
files.writeall('../src/SUMMARY.md', outTxt)

