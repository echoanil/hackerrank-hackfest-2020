rdict = {}
bdict = {}
gdict = {}
def formdict(t):
  if (t[0] in rdict):
    if (t[1] in rdict[t[0]]):
      if (not(t[2] in rdict[t[0]][t[1]])):
        rdict[t[0]][t[1]].append(t[2])
else :
  rdict[t[0]][t[1]] = []
rdict[t[0]][t[1]].append(t[2])
else :
  rdict[t[0]] = {}
rdict[t[0]][t[1]] = []
rdict[t[0]][t[1]].append(t[2])
if (t[1] in bdict):
  if (t[0] in bdict[t[1]]):
    if (not(t[2] in bdict[t[1]][t[0]])):
      bdict[t[1]][t[0]].append(t[2])
else :
  bdict[t[1]][t[0]] = []
bdict[t[1]][t[0]].append(t[2])
else :
  bdict[t[1]] = {}
bdict[t[1]][t[0]] = []
bdict[t[1]][t[0]].append(t[2])
if (t[2] in gdict):
  if (t[0] in gdict[t[2]]):
    if (not(t[1] in gdict[t[2]][t[0]])):
      gdict[t[2]][t[0]].append(t[1])
else :
  gdict[t[2]][t[0]] = []
gdict[t[2]][t[0]].append(t[1])
else :
  gdict[t[2]] = {}
gdict[t[2]][t[0]] = []
gdict[t[2]][t[0]].append(t[1])

def checkq(t):
  cnt = {
    'r': False,
    'b': False,
    'g': False
  }
if (t[0] in rdict and t[1] in bdict and t[2] in gdict):
  for i in rdict[t[0]]:
  if (i <= t[1]):
    for j in rdict[t[0]][i]:
    if (j <= t[2]):
      cnt['r'] = True
break
if (cnt['r'] == True):
  break

for i in bdict[t[1]]:
  if (i <= t[0]):
    for j in bdict[t[1]][i]:
    if (j <= t[2]):
      cnt['b'] = True
break
if (cnt['b'] == True):
  break

for i in gdict[t[2]]:
  if (i <= t[0]):
    for j in gdict[t[2]][i]:
    if (j <= t[1]):
      cnt['g'] = True
if (cnt['g'] == True):
  break

if (cnt['r'] == True and cnt['b'] == True and cnt['g'] == True):
  return ("YES")
else :
  return ("NO")

def mixColors(colors, queries):
  s = []
nd = len(colors)
nq = len(queries)
for i in range(nd):
  t = colors.pop()
formdict(t)
print(rdict, bdict, gdict, sep = "\n")
for i in range(nq):
  t = queries[i]
s.append(checkq(t))
return (s)