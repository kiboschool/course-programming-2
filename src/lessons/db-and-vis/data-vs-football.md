
# Football 
https://github.com/kiboschool/programming-2/blob/draft/internal-notes/scraped_datasets/footballdata_players.json

https://github.com/kiboschool/programming-2/blob/draft/internal-notes/scraped_datasets/footballdata_countries.json

Queries who has the most goals
Queries who has the most goals and born after year 2000
Queries who is the not-forward with the most goals

Scatter plot:
    Caps vs goals but only for forward position
    
    
```
from ben_python_common import *

import matplotlib.pyplot as plt
import numpy as np

xar = []
yar = []
xmorrocoar = []
ymorrocoar = []

lns = files.readall('footballdata.tsv', encoding='utf-8').replace('\r\n', '\n').split('\n')
lns.pop(0)
for ln in lns:
    if ln.strip():
        if not 'FW' in ln:
            continue
        pts = ln.split('\t')
        caps = int(pts[3])
        goals = int(pts[4])
        if ln.startswith('Morocco'):
            xmorrocoar.append(caps)
            ymorrocoar.append(goals)
        else:
            xar.append(caps)
            yar.append(goals)

x = np.array(xar)
y = np.array(yar)
plt.scatter(x, y)
xm = np.array(xmorrocoar)
ym = np.array(ymorrocoar)
plt.scatter(xm, ym, color='red')


plt.show()



```

