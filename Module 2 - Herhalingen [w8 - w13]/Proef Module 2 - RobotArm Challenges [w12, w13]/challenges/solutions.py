def getDemocratieWinner(yardStart):
  char_count = {}
  _yard = yardStart.split(',')
  for index in range(len(_yard)):
     _yard[index] = list(_yard[index])

  # Count occurrences of each character
  for _stack in _yard:
    for char in _stack:
        char_count[char] = char_count.get(char,0) + 1
 
  # Find the character with the maximum count
  max_count = 0
  winner = None
  for char, count in char_count.items():
      if count > max_count:
          max_count = count
          winner = char

  return winner

def getDemocratieSolution(yardStart, criteria=''):
  winner = getDemocratieWinner(yardStart)
  _yard = yardStart.split(',')
  for indexStack in range(1,len(_yard)):
    if len(_yard[indexStack]) > 0 and _yard[indexStack] == winner:
        _yard[indexStack] = ''
        _yard[0] += winner

  return ','.join(_yard)

def hasDemocratie(yardStart, yardNow, criteria=''):
  solution = getDemocratieSolution(yardStart, criteria)
  return yardNow == solution

def hasColorNotAt(yardStart, yardNow, spec):
  color = spec[0]
  try:
    indexNow = int(spec[2:])
  except: 
     return False

  _yardNow = yardNow.split(',')   
  if 0 <= indexNow < len(_yardNow) and _yardNow[indexNow].count(color) == 0:
    return True

  return False

def hasColorCollectedAt(yardStart, yardNow, spec):
  color = spec[0]
  try:
    indexNow = int(spec[2:])
  except: 
     return False

  totalCounted = yardStart.count(color)
  _yardNow = yardNow.split(',')   
  if 0 <= indexNow < len(_yardNow) and _yardNow[indexNow].count(color) == totalCounted:
    return True
    
  return False

def hasColorMoved(yardStart, yardNow, spec):
  color = spec[0]
  try:
    shift = int(spec[2])
  except: 
     return False
  if spec[1] == '<':
     shift = -1 * shift

  _yardStart = yardStart.split(',')
  _yardNow = yardNow.split(',')
  _length = len(_yardStart)
  for index in range(_length):
     _countStart = _yardStart[index].count(color)
     newIndex = index + shift
     if 0 <= newIndex < _length:
        _countNow = _yardNow[newIndex].count(color)
        if _countStart != _countNow:
           return False
  return True

def hasDistributedFromAt(yardStart, yardNow, spec):
  try:
    source = int(spec[0])
    dest = int(spec[2])
  except:
     return False
  if spec[1] == '}':
    delta = 1
  elif spec[1] == '{':
    delta = -1

  _yardStart = yardStart.split(',')
  _yardNow = yardNow.split(',')

  for index in range(len(_yardStart[source])-1,-1,-1):
    color = _yardStart[source][index]
    if 0 <= dest < len(_yardNow):
      if len(_yardNow[dest]) == 0 or color != _yardNow[dest][-1]:
        return False
    dest += delta

  return True

def hasSolution(yardStart, yardNow, criteria):
  if type(criteria) != str: return False

  _specs = criteria.split(',')
  checked = False
  for _spec in _specs:
    if _spec[1] == ':': 
      if not hasColorCollectedAt(yardStart, yardNow,_spec): 
        return False
      checked = True
    elif _spec[1] in ['}','{']: 
      if not hasDistributedFromAt(yardStart, yardNow,_spec): 
        return False
      checked = True
    elif _spec[1] in ['>','<']: 
      if not hasColorMoved(yardStart, yardNow,_spec): 
        return False
      checked = True
    elif _spec[1] == '-': 
      if not hasColorNotAt(yardStart, yardNow,_spec): 
        return False
      checked = True

  return checked

def moveColor(solution, spec):
  color = spec[0]
  try:
    shift = int(spec[2])
  except: 
     return False
  if spec[1] == '<':
     shift = -1 * shift

  stacks = solution.split(',')
  shifted = ['' for index in range(len(stacks))]
  for index in range(len(stacks)):
    newIndex = index + shift
    if newIndex < 0 or newIndex >= len(stacks): continue
    shifted[newIndex] += color * stacks[index].count(color)
    stacks[index] = stacks[index].replace(color,'')
  for index in range(len(stacks)):
    stacks[index] += shifted[index]
  return ','.join(stacks)


def collectColorAt(solution, spec):
  color = spec[0]
  try:
    indexNow = int(spec[2:])
  except: 
     return solution
  stacks = solution.split(',')
  for index in range(len(stacks)):
    if index == indexNow: continue
    stacks[indexNow] += color * stacks[index].count(color)
    stacks[index] = stacks[index].replace(color,'')

  return ','.join(stacks)

def distributeFromAt(solution, spec):
  try:
    source = int(spec[0])
    dest = int(spec[2])
  except:
     return False
  if spec[1] == '}':
    delta = 1
  elif spec[1] == '{':
    delta = -1

  stacks = solution.split(',')
  boxes = stacks[source]
  stacks[source] = ''
  for index in range(len(boxes)-1,-1,-1):
    color = boxes[index]
    if 0 <= dest < len(stacks):
      stacks[dest] += color
    dest += delta    
  
  return ','.join(stacks)

def exampleSolution(yardStart, criteria):
  solution = yardStart

  if type(criteria) == str:
    _specs = criteria.split(',')
    for _spec in _specs:
      if _spec[1] == ':':
        solution = collectColorAt(solution, _spec)
      elif _spec[1] in ['>','<']: 
        solution = moveColor(solution, _spec)
      elif _spec[1] in ['}','{']:
        solution = distributeFromAt(solution, _spec)
  return solution

# solution = presentSolution('rgboywpt,,,,,,,,,','0}2')
# print(solution)
# print(result)
