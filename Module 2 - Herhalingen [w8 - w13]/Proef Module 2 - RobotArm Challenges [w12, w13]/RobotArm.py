import pygame # install in terminal with: pip install pygame
from assets.SpriteSheet import SpriteSheet
import os
import sys
import random
import string
import inspect
from math import ceil, floor

# RobotArm class ################################################
help = '''
  =================== RobotArm ===================
  moves boxes from one spot to another...
  
  robotArm = RobotArm(challenge,level)
    loads a challenge and displays its stacks of colored boxes
  
  methods to use with robotArm:

  moveRight()
    moves the robotarm one stack position to the right
    returns True if succeeded, returns False if not possible

  moveLeft()
    moves the robotarm one stack position to the left
    returns True if succeeded, returns False if not possible

  grab()
    lets the robotarm grab a box from the stack if there is one
    returns True if succeeded, returns False if not possible

  drop()
    lets the robotarm drop its box to the stack if not full
    returns True if succeeded, returns False if not possible

  scan()
    returns the color of the box at the robotarm

  stackEmpty()
    returns True if stack under robotarm ie empty, else False

  stackIndex() 
    returns the current index (position) of the robotArm

  showSolution()
    displays the the solution (if available)

  report()
    reports the results of the mission (challenge and level) and then waits
  
  wait()
    waits for the program window to continue 

  operate()
    makes the robotarm operate on keyboard-keys: LEFT, RIGHT and DOWN

  help()
    shows help in the terminal
  
  helpChallenge()
    shows help in the terminal in creating challenges
'''

helpChallenge = '''
=================== define challenges ===================

  challenge example: 
  {'name': 'collect boxes', 
   'start' : 'gbg,,y,,br,,,,' , # defining the colors of boxes at spots separated by komma
   'solution': ',,,,,,,,,gbgybr', # defining the colors of boxes at spots separated by komma
   'levels':'2:20,3:20/29', # defining for levels: maximum code lines / maximum actions taken
   'info': 'move all boxes to last spot' # detailed instructions to reach solution
  }
    
    'start' defines the colors of boxes at spots separated by komma
    'solution' defines the colors of boxes at spots separated by komma
    'levels' defines for levels the levelnr: maximum code lines / maximum actions taken
    'info' detailed instructions to reach solution

    supported colors: 
    w=white, g=green, r=red, b=blue, y=yellow, o=orange, p=purple, l=grey, n=black, t=transparent and i=invisible

    examples of start stacks and solution stacks:

      3y2r  -> 3 yellow boxes, 2 red boxes
      *b    -> random number (0..5) of blue boxes
      4?    -> 4 boxes of a random color from: red, green, blue or white
      *p combined with 'symbols' : '*?2' -> random number (0..2) of purple boxes
      x combined with 'symbols' : 'x?yyyybb' -> 1 box with a color random picked from collection yyyybb
      4x combined with 'symbols' : 'x-rrrrggg' -> 4 boxes with a color once random picked from collection rrrrggg
      #w#r#b combined with 'symbols' : '#+1' -> 1 white, 2 red, 3 blue boxes
      #w,#r,#b combined with 'symbols' : '#-5' -> in subsequent stacks: 5 white, 4 red, 3 blue boxes

    solutions based on a start with random colors or numbers can be defined by a function called with criteria:
    'criteria' : 'r:6' -> all red boxes to be collected at spot 6
    'criteria' : 'b>2' -> all blue boxes to be moved 2 positions to the right
    'criteria' : 'w<1' -> all white boxes to be moved 1 position to the left
    'criteria' : '2}4' -> all boxes on spot to be distributed to the right starting at spot 4
    'criteria' : '3{8' -> all boxes on spot to be distributed to the left starting at spot 8
'''

class RobotArm:
  version = '2.5'
# 2.1: incluses warnings for actions like hitting the borders
# 2.2: includes flaw terminal warnings for pointless actions
# 2.3: may grab once without warning from empty stack that was randomly sized
# 2.3.1: added handling key UP en DOWN for speeding up and down, while running animations
# 2.4: 
  _backgroundColor = (200,200,200)
  _transparentPenColor = list(_backgroundColor) # pencolor slightly different from background
  for i in range(3): _transparentPenColor[i] += 20 if _transparentPenColor[i] <= 235 else -20

  _colors = [
    {"name": 'w', 'color': (255,255,255), 'des': 'white'},
    {"name": 'r', 'color': (255,0,0), 'des': 'red'},
    {"name": 'g', 'color': (0,150,0), 'des': 'green'},
    {"name": 'b', 'color': (0,0,255), 'des': 'blue'},
    {"name": 'y', 'color': (255,255,0), 'des': 'yellow'},
    {"name": 'p', 'color': (128,0,128), 'des': 'purple'},
    {"name": 'o', 'color': (255,128,0), 'des': 'orange'},
    {"name": 'n', 'color': (10,10,10), 'des': 'black'},
    {"name": 'i', 'color': False, 'des': 'invisible','pencolor':False}, # turns into transparent when grabbed
    {"name": 't', 'color': False, 'des': 'transparent','pencolor':_transparentPenColor},
    {"name": 'l', 'color': (160,160,160), 'des': 'gray'},
  ]
  _colorSet = [color['name'] for color in _colors]
  _defaultChallenge = {'name': 'demo','start' : ',r','solution': 'r', 'levels': '1:10,2:10/6'}
  _speeds = [{'fps': 100,'step': 1},{'fps': 150,'step': 2},{'fps': 250,'step': 4},{'fps': 400,'step': 5},{'fps': 500,'step': 10},{'fps': 500,'step': 20}]
  EMPTY = ''

  _backgroundColorAccu = (0,0,0)
  _penColor = (0,0,0)
  _maxStacks = 10
  _maxLayers = 8
  _boxHeight = 29
  _boxWidth = 29
  _penWidth = 1
  _boxMargin = 2
  _armTopHeight = 15
  _bottomMargin = 2
  _idleAnimationTime = 300
  _screenMargin = 3
  _eventSleepTime = 300
  _eventActiveCycles = 100
  _actions = 0 # amount of actions done
  _iconImage = 'robotarm.ico'
  _hazardSprite = 'caution-icon-hi.png'
  _hazardFont = 'FreeSansBold.ttf'
  _previousAction = ''
  _accuWidth = 15
  _accuCapacity = False
  _accuPadding = 5
  _accuColors = ((100,'g'),(50, 'y'),(25, 'o'),(10, 'r'))
  _criticals = {'e':0,'w':0,'i':0}
  _solutionDone = False
  _missionReported = False
  _aborted = False
  _actionFlaws = [
    ['left','right'],
    ['right','left'],
    ['drop','grab'],
    ['grab','drop'],
    ['scan','scan'],
    ['drop','scan'],
  ]
  _knownEmpty = []
  MAXCAPTION = 24

  def _count_lines_of_code(self):
    current_frame = inspect.currentframe()
    while current_frame.f_back:
        current_frame = current_frame.f_back
    caller_filename = inspect.getframeinfo(current_frame).filename
    with open(caller_filename, 'r') as f:
      lines = f.readlines()
    num_lines = 0
    for line in lines:
      line = line.strip()
      if line and not line.startswith("#") and not line.startswith("print(") and not line.startswith("input("):
        num_lines += 1
    return num_lines
  
  def _internalError(self, info):
    print(f' ********* {info} *********')
    exit()

  def _colored(self,text,color):
    if color == 'red':
      return "\033[1;31;40m" + text + "\033[0m"
    elif color == 'green':
      return "\033[1;32;40m" + text + "\033[0m"
    elif color == 'blue':
      return "\033[1;34;40m" + text + "\033[0m"
    elif color == "yellow":
      return "\033[1;33;40m" + text + "\033[0m"
    elif color == "orange":
      return "\033[1;38;2;255;165;0m" + text + "\033[0m"
    else:
      return text

  def _missionInfo(self, state, info1, info2 = '', color='white'):

    def formatLine(text, paddingLeft, length, char, color='white'):
      before = paddingLeft * char 
      after = (length - len(text)) * char
      return '*' + before + self._colored(text,color) + after + '*'
    
    length = max(len(info1),len(info2))
    padding = 5
    totalLength = length + 2 * padding
    title = ' MISSION ' + state + ' '
    top = formatLine(title ,padding, totalLength, '*',color) 
    bottom = formatLine('',padding, totalLength, '*')
    space = formatLine('',padding, totalLength, ' ')
    info1 = formatLine(info1,padding, totalLength, ' ')
    if info2: info2 = formatLine(info2,padding, totalLength, ' ')
    print(top)
    print(space)
    print(info1)
    if info2: print(info2)
    print(space)
    print(bottom)

  def _setScreen(self):
    self._screenWidth = self._stackX(self._maxStacks) + self._screenMargin 
    self._screenHeight = self._layerY(-1) + self._bottomMargin + 2 * self._screenMargin
    self._screen = pygame.display.set_mode((self._screenWidth + self._accuWidth, self._screenHeight))

  def loadDims(self,challenge):
    if not type(challenge) is dict: return
    self._maxLayers = challenge.get('layers',self._maxLayers)
    self._maxStacks = challenge.get('stacks',self._maxStacks)

  def __init__(self, challenge = _defaultChallenge, level = 0):

    self.loadDims(challenge)
    self._color = self.EMPTY
    self._stack = 0
    self._yardBottom = self._armTopHeight + (self._maxLayers + 1) * self._boxSpaceHeight() + self._penWidth
    self._armHeight = self._armTopHeight
    self._armX = 0
    self.speed = 1
    self._yard = []
    
    self._setScreen()

    pygame.init()
    self._clock = pygame.time.Clock()

    assetsDir = os.path.dirname(os.path.realpath(__file__)) + '/assets/'    # force assets to be found in directory of robotarm.py
    try:
      programIcon = pygame.image.load(assetsDir + self._iconImage)
      pygame.display.set_icon(programIcon)
      self._testImage = programIcon
    except:
      self._internalError(f'icon image: {self._iconImage} not found')

    try:
      ss = SpriteSheet(assetsDir + self._hazardSprite)
      self._hazardSign = ss.load_strip((0,0,64,64), 4, self._backgroundColor)
    except:
      self._internalError(f'hazard sprite: {self._hazardSprite} not found')

    try:
      self._font = pygame.font.Font(assetsDir + self._hazardFont, 24)
    except:
      self._internalError(f'font: {self._hazardFont} not found')

    # Load level at creation
    self.load(challenge, level)

########### ANIMATION METHODS ###########

  def _getColorCode(self, name):
    for c in self._colors:
      if c['name'] == name:
        return c['color'], c.get('pencolor',self._penColor)
    return False
  
  def _getColorDes(self,name):
    for c in self._colors:
      if c['name'] == name:
        return c['des']
    return ''   
  
  def _checkSpeed(self):
    speedInvalid = False
    if type(self.speed) is not int:
      speedInvalid = True
    if not (self.speed in range(len(self._speeds))):
      speedInvalid = True
    if speedInvalid:
      self.speed = 0 # reset speed to zero
      print('speed must be an integer between 0 and ' + str(len(self._speeds)-1))

  def _drawBoxAtPosition(self, x, y, color, pencolor):
    if color:
      pygame.draw.rect(self._screen, color, (x, y, self._boxWidth, self._boxHeight))
    if pencolor:
      pygame.draw.rect(self._screen, pencolor, (x, y, self._boxWidth, self._boxHeight), self._penWidth)

  def _boxSpaceWidth(self):
    return (self._boxWidth + 2 * self._boxMargin) + self._penWidth

  def _stackX(self, stack):
    return self._screenMargin + self._boxMargin + stack * self._boxSpaceWidth() + self._penWidth

  def _boxSpaceHeight(self):
    return (self._boxHeight - self._penWidth)

  def _layerY(self,layer):
    return self._yardBottom - (layer + 1) * self._boxSpaceHeight() - self._screenMargin

  def _drawBox(self, stack, layer):
    x = self._stackX(stack) 
    y = self._layerY(layer)
    _color,_pencolor = self._getColorCode(self._yard[stack][layer])
    self._drawBoxAtPosition(x,y,_color, _pencolor)

  def drawSpot(self, stack, color):
    x = self._stackX(stack) - self._boxMargin - self._penWidth


  def _drawStack(self, stack):
    for l in range(len(self._yard[stack])):
      self._drawBox(stack,l)
    x = self._stackX(stack) - self._boxMargin - self._penWidth
    y = self._layerY(-1) + self._bottomMargin

    pygame.draw.lines(self._screen, self._penColor, False, [(x, y - 5), (x, y), (x + self._boxSpaceWidth(), y), (x + self._boxSpaceWidth(), y - 5)])

  def _drawArm(self):
    xm = self._armX + int(self._boxSpaceWidth()/2) - self._boxMargin
    pygame.draw.line(self._screen, self._penColor, (xm, 2), (xm, self._armHeight - 2))
    pygame.draw.lines(self._screen, self._penColor, False, [
      (self._armX - self._boxMargin,                  self._armHeight + 2), 
      (self._armX - self._boxMargin,                  self._armHeight - 2),
      (self._armX + self._boxWidth + self._penWidth,  self._armHeight - 2),
      (self._armX + self._boxWidth + self._penWidth , self._armHeight + 2)])
    if self._color > '':
      _color, _pencolor = self._getColorCode(self._color)
      self._drawBoxAtPosition(self._armX,self._armHeight,_color,_pencolor)

  def _drawAccu(self):
    if self._accuCapacity ==  False: return
    # pygame.draw.rect(self._screen, (0,150,0), (self._screenWidth, 0, self._accuWidth, self._screenHeight))
    _stepsDone  = self._actions if self._actions < self._accuCapacity else self._accuCapacity
    _accuOver = (self._accuCapacity - _stepsDone) / self._accuCapacity
    _accuDone = _stepsDone / self._accuCapacity
    _accuPerc = ceil(_accuOver * 100)

    pygame.draw.rect(self._screen, self._backgroundColorAccu, (self._screenWidth, 0, self._accuWidth, self._screenHeight))
    _x0 = self._screenWidth + self._accuPadding
    _y0 = 0 + self._accuPadding
    _w0 = self._accuWidth - 2 * self._accuPadding
    _h0 = self._screenHeight  - 2 * self._accuPadding

    _x = _x0
    _y = self._accuPadding+ ceil(_h0 * _accuDone)
    _h = floor(_h0 * _accuOver)
    color = 'g'
    for percColor in self._accuColors:
      if _accuPerc < percColor[0]:
        color = percColor[1]
    _color, _ = self._getColorCode(color)
    pygame.draw.rect(self._screen, _color, (_x0, _y, _w0, _h))
    pass

  def _drawState(self):
    steps = ' ['+ str(self._actions)+']' if self._actions > 0 else ''
    _caption = self._challengeName[0:self.MAXCAPTION] + steps
    pygame.display.set_caption(_caption)
    self._screen.fill(self._backgroundColor)
    for c in range(len(self._yard)):
      self._drawStack(c)
    self._drawArm()
    self._drawAccu()

  def _message(self, message = 'problem!', gravity = 1):
    xm = self._armX + int(self._boxSpaceWidth()/2) - self._boxMargin - 31
    ym = 0

    text = self._font.render(message, True, (200,50,50), self._backgroundColor)
    for l in range(12):
      self._drawState()
      if gravity == 1: self._screen.blit(self._hazardSign[l % 4],(xm,ym))
      if l%2 == 0 or l >= 6:
        self._screen.blit(text, ((self._screenWidth//2) - text.get_rect().width//2,60))
      pygame.display.update()
      pygame.time.delay(100)

    self._drawState()
    pygame.display.update()

  def _handleHazard(self, message = 'problem!'):
    self._message(message, 1)
    self._log(message,'e')

  def _log(self, message, cat):
    if self._level in [0] and cat == 'e': return
    if self._level in [0,1,2] and cat == 'w': return
    markup = {'w':{'title':'warning','color':'orange'},'i':{'title':'info   ','color':'white'},'e': {'title':'error  ','color':'red'}}
    title = self._colored(markup[cat]['title'],markup[cat]['color'])
    print(f'{title}: {message}')
    self._criticals[cat] += 1

  def _animate(self, *args):
    self._checkSpeed()
    self._armX = self._stackX(self._stack)

    if (args[0] == 'down'):
      self._armHeight = self._armTopHeight
      targetLayer = len(self._yard[self._stack])
      if self._color == '':
        targetLayer -= 1
      targetHeight = self._layerY(targetLayer)
    elif (args[0] == 'left'):
      targetX = self._stackX(self._stack - 1)
    elif (args[0] == 'right'):
      targetX = self._stackX(self._stack + 1)

    ready = False
    while not ready:
      if (args[0] == 'idle'):
        ready = True
      elif (args[0] == 'down'):
        ready = self._armHeight == targetHeight
      elif (args[0] == 'up'):
        ready = self._armHeight == self._armTopHeight
      elif (args[0] == 'left') or (args[0] == 'right'):
        ready = self._armX == targetX

      for event in pygame.event.get():
        self.checkCloseEvent(event)
        self.handleSpeedEvent(event)
        self.handleSolutionShow(event)

      self._drawState()
      pygame.display.update()

      self._clock.tick(self._speeds[self.speed]['fps'])

      if (args[0] == 'down'):
        self._armHeight += self._speeds[self.speed]['step']
        if self._armHeight > targetHeight:
          self._armHeight = targetHeight
      elif (args[0] == 'up'):
        self._armHeight -= self._speeds[self.speed]['step']
        if self._armHeight < self._armTopHeight:
          self._armHeight = self._armTopHeight
      elif (args[0] == 'left'):
        self._armX -= self._speeds[self.speed]['step']
        if self._armX < targetX:
          self._armX = targetX
      elif (args[0] == 'right'):
        self._armX += self._speeds[self.speed]['step']
        if self._armX > targetX:
          self._armX = targetX
      elif (args[0] == 'idle'):
        pygame.time.delay(self._idleAnimationTime)

  def _hasActionsLeft(self):
    return self._accuCapacity == False or (self._accuCapacity - self._actions) > 0

  def _checkAccu(self):
    if not self._hasActionsLeft():
      if self._accuEmpty:
        self._wait(self._continue)
      if self._accuEmpty == False: 
        self._log('accu empty, use spacebar to proceed, escape to abort','w')
        self._backgroundColorAccu = (255,0,0)
        self._accuEmpty = True
      self._log('action, but accu empty','w')
    self._actions += 1

  def _checkFlaws(self, action):
    for flaw in self._actionFlaws:
      if (self._previousAction == flaw[0] and action == flaw[1]):
        flawText = f'{flaw[1]} after {flaw[0]}'
        self._log(f'action pointless: {flawText}?','w')
    self._previousAction = action
    if self._solutionDone and self._scans > self._scansMax:
      self._log(f'needless action after solution','w')

  ########### ROBOTARM MANIPULATION ###########
  def moveRight(self):
    if self._aborted: return
    self._checkAccu()
    self._checkFlaws('right')
    success = False
    if self._stack < self._maxStacks - 1:
      self._animate('right')
      self._stack += 1
      success = True
    else:
      self._handleHazard('hit right border!')
    return success

  def moveLeft(self):
    if self._aborted: return
    self._checkAccu()
    self._checkFlaws('left')
    success = False
    if self._stack > 0:
      self._animate('left')
      self._stack -= 1
      success = True
    else:
      self._handleHazard('hit left border!')
    return success

  def grab(self):
    if self._aborted: return
    self._checkAccu()
    self._checkFlaws('grab')
    success = False
    if self._color == self.EMPTY:
      self._animate('down')
      if len(self._yard[self._stack]) > 0:
        self._color = self._yard[self._stack][-1]
        if self._color == 'i':
          self._color = 't'
        self._yard[self._stack].pop(-1)
        success = True
      else:
        if self._knownEmpty[self._stack]:
          self._handleHazard('nothing to grab!')
        else:
          self._knownEmpty[self._stack] = True
      self._animate('up')
    else:
      self._handleHazard('robot arm occupied!')
    return success

  def drop(self):
    if self._aborted: return
    self._checkAccu()
    self._checkFlaws('drop')
    success = False
    if self._color != self.EMPTY:
      if len(self._yard[self._stack]) < self._maxLayers:
        self._animate('down')
        self._yard[self._stack].append(self._color)
        self._color = self.EMPTY
        self._animate('up')
        success = True
      else:
        self._handleHazard('stack full!')
    else:
      self._handleHazard('no box to drop!')
    self._watchSolution()
    return success

  def scan(self):
    if self._aborted: return
    self._checkAccu()
    self._checkFlaws('scan')
    self._scans += 1
    return self._getColorDes(self._color)
  
  def stackEmpty(self):
    return len(self._yard[self._stack]) == 0
  
  def stackIndex(self):
    return self._stack

########### LEVEL & YARD lOADING & CREATION ###########

  def _isSolution(self):
    serializedYard = self.serializeYard(self._yard)
    
    if type(self._solution) is str:
      if self._solution == serializedYard:
        return True
      else:
        return False
    elif callable(self._solution):
      return self._solution(self._yardStart, serializedYard, self._criteria)
    
  def _watchSolution(self):
    if self._isSolution():
      self._backgroundColor = (250,250,100)
      self._solutionDone = True
      self._animate('idle')
      
  def constructYard(self, yard = 'r', symbols = '' ):
    colorSymbols = string.ascii_lowercase + '?'  #string.ascii_uppercase + 
    amountSymbols = '*#'
    stdColorSet = ''.join(self._colorSet)
     # determine symbols in the yard
    symbols = symbols.split(',')
    _symbols = {}
    _symbols['?'] = {'colors' : list('rgbw'), 'proces': '?'} # default random color symbol
    _symbols['*'] = {'value' : 4, 'proces': '?'} # default random amount symbol
    for symbol in symbols:
      if len(symbol) > 1 and symbol[0] == '-':
        try:
          self._stack = int(symbol[1])
        except:
          continue

      if len(symbol) < 3: continue

      if symbol[0] in amountSymbols and symbol[2] in string.digits:
        _symbols[symbol[0]] = {'value' : int(symbol[2]), 'proces': symbol[1]}

      if symbol[0] in colorSymbols:
        # get valid colorset
        colorset = ''
        for c in symbol[2:]:
          if c in stdColorSet:
            colorset += c
        if colorset == '': colorset = stdColorSet
        _symbols[symbol[0]] = {'value': False, 'colors' : list(colorset), 'proces': symbol[1], 'reset': list(colorset)}
   
    stacks = yard.split(',')

    _yard = []
    for stack in stacks:
      _stack = []
      amountBoxes = 1
      color = False
      for char in _symbols:
        if _symbols[char]['proces'] == '|':
          _symbols[char]['colors'] = _symbols[char]['reset'] + [] # every stack a new color set
      for char in stack:
        if char in colorSymbols:
          for _ in range(amountBoxes):
            if char in _symbols:
              if _symbols[char]['proces'] == '?':
                color = random.choice(_symbols[char]['colors'])
              elif _symbols[char]['proces'] in ['-','|']:
                color = random.choice(_symbols[char]['colors'])
                _symbols[char]['colors'].remove(color)
                if len(_symbols[char]['colors']) == 0:
                  _symbols[char]['colors'].append('n')
              elif _symbols[char]['proces'] == '>':
                color = _symbols[char]['colors'][_symbols[char]['value']]
                _symbols[char]['value'] = (_symbols[char]['value']+1) % len(_symbols[char]['colors'])
              elif _symbols[char]['proces'] == '<':
                color = _symbols[char]['colors'][_symbols[char]['value']]
                _symbols[char]['value'] = (_symbols[char]['value']-1+len(_symbols[char]['colors'])) % len(_symbols[char]['colors'])
              elif _symbols[char]['proces'] == '=':
                if _symbols[char]['value'] == False:
                  _symbols[char]['value'] = random.randint(0,len(_symbols[char]['colors'])-1)
                color = _symbols[char]['colors'][_symbols[char]['value']]
            elif char in stdColorSet:
              color = char
            else:
              color = self._colorSet[-1] # pick deault last of colors
            if len(_stack) < self._maxLayers:
              _stack.append(color)
          amountBoxes = 1
        elif char in string.digits:
          amountBoxes = int(char)
        elif char in amountSymbols and char in _symbols:
          if _symbols[char]['proces'] == '?':
            if self._level == 3 and self._limitActions:
              amountBoxes = _symbols[char]['value'] # test maximal!!
            else:
              amountBoxes = random.randint(0,_symbols[char]['value'])
          else:
            amountBoxes = _symbols[char]['value']
            if _symbols[char]['proces'] == '+':
              _symbols[char]['value'] += 1
            if _symbols[char]['proces'] == '-':
              _symbols[char]['value'] -= 1
              if _symbols[char]['value'] < 0: 
                _symbols[char]['value'] = 0
      _yard.append(_stack)

    while len(_yard) < self._maxStacks:
      _yard.append([])
    return _yard
  
  def setLevelLimits(self, level, levels):
    _limitLines = False
    _limitActions = False
    if level in [1,2,3] and type(levels) is str and levels > '':
      _levels = levels.split(',')
      try:
        for _level in _levels:
          if level == int(_level[0]):
            _limits =  _level.split(':')[1].split('/')
            _limitLines = int(_limits[0])
            if len(_limits) >= 2:
              _limitActions = int(_limits[1])
      except: pass
    return _limitLines, _limitActions
  
  def setSolution(self, solution):
    if type(solution) is str:
      solution += (self._maxStacks - solution.count(',') - 1) * ','
      _yardSolution = self.constructYard(solution,'')
      solution = self.serializeYard(_yardSolution)
    return solution
  
  def setScanLimits(self,scans):
    _scansMax = False
    _scansMin = False
    if type(scans) is str:
      _limits = scans.split(":")
      try:
        _scansMin = int(_limits[0])
      except:
        print('error specs scans minimum')
      try:
        _scansMax = int(_limits[1])
      except:
        print('error specs scans maximum')        
    return _scansMin, _scansMax
  
  def _displayMission(self):
    
    if self._level == 0: return
    info1 = 'No restrictions on lines of code'
    info2 = 'No restrictions on actions taken, but no errors allowed.'
    if self._level in [1,2,3] and self._limitLines != False:
      info1 = f'Maximum number of lines of code: {self._limitLines}'
    if self._scansMin:
      info2 += f' {self._scansMin} to {self._scansMax} scans needed.'
    if self._level in [3]:
      info2 = f'Maximum number of actions: {self._limitActions}' if self._limitActions != False else 'No restrictions on actions taken'
      if self._scansMax:
        info2 += f', maximal {self._scansMax} scans allowed'      
      info2 += ', no errors nor warnings!'

    _missionText = 'WITH UNKNOWN SOLUTION' if self._solution == False else f'AT LEVEL: {self._level}'
    self._missionInfo(f'STARTED {_missionText} ', info1, info2,'yellow')
    self._log(f'Started with {self._lines} lines of code','i')

  def load(self, challenge = _defaultChallenge , level = 0):
    _symbols = ''
    _solution = False
    _levels = False
    _scans = False
    _criteria = False
    _example = False
    _info = ''

    if type(challenge) is dict:
      _yard = challenge.get('start','')
      _symbols = challenge.get('symbols','')
      _solution = challenge.get('solution',False)
      _criteria = challenge.get('criteria',False)
      _example = challenge.get('example',False)
      _levels = challenge.get('levels',False)
      _scans = challenge.get('scans',False)
      _challengeName = challenge.get('name',f'no name')
      _challengeName = _challengeName if _challengeName else 'no name'
      _info = challenge.get('info','')
    elif type(challenge) is str:
      level = 0
      _yard = challenge
      _challengeName = f'no name' 
    else:
      return False

    if _levels != False:
      while level > 1 and not str(level)+':' in _levels: level -= 1
    self._level = level
    
    self._yard = self.constructYard(_yard, _symbols)
    self._yardStart = self.serializeYard(self._yard)
    self._solution = self.setSolution(_solution)
    self._criteria = _criteria
    self._example = _example
    self._solutionDone = False

    self._limitLines, self._limitActions = self.setLevelLimits(level, _levels)
    self._scansMin, self._scansMax = self.setScanLimits(_scans)
    self._lines = self._count_lines_of_code()
    self._actions = 0
    self._challengeName =_challengeName

    msg = self._colored(self._challengeName,'blue') + ('\n'+_info if _info else '')
    self._log(msg,'i')

    self._mission = False
    self._knownEmpty = [True for stack in range(self._maxStacks)]
    self._accuCapacity = self._limitActions
    self._accuEmpty = False
    self._scans = 0
    self._displayMission()
    self._animate('idle')

    return True

  def serializeYard(self, yard):
    _yard = ''
    for stack in yard:
      _yard += ''.join(stack)+','
    return _yard[:-1]

########### EVENT HANDLING ###########

  def checkCloseEvent(self,event):
    if event.type == pygame.QUIT:
      sys.exit()

  def handleSpeedEvent(self,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          if self.speed < 5:
            self.speed += 1
        elif event.key == pygame.K_DOWN:
          if self.speed > 0:
            self.speed -= 1
  
  def handleSolutionShow(self,event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        self.showSolution(5)

  def _defaultHandler(self, events):
    for event in events:
      self.checkCloseEvent(event)
      self.handleSolutionShow(event)

  def _continue(self, events):
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          return False
        elif event.key == pygame.K_ESCAPE:
          self._aborted = True
          return False
    return True

  def _wait(self, handler = False):
    print(f'Press spacebar to continue...')
    cycle = 0
    while True:
      events = pygame.event.get()               # get latest events
      if callable(handler):
        if not handler(events):
          break
      self._defaultHandler(events)
      if not self._continue(events):
        return
      if len(events) > 0:                       # events happened?
        cycle = 0                               # stay awake and alert
      cycle += 1                                # prepare for sleep

      if cycle > self._eventActiveCycles:       # after 30 cycles
        pygame.time.delay(self._eventSleepTime) # go asleep for 300 milliseconds, give the processor some rest
        cycle = 0                               # wake up for events during sleep

  def _operator(self, instructions):
    for instruction in instructions:
      if instruction.type == pygame.KEYDOWN:
          if instruction.key == pygame.K_LEFT:
            self.moveLeft()
          if instruction.key == pygame.K_RIGHT:
            self.moveRight()
          if instruction.key == pygame.K_DOWN:
            if self._color == '':
              self.grab()
            else:
              self.drop()
    return True # continue listening

  def operate(self):
    self._reportMission()
    self._wait(self._operator)

  def _reportMission(self):
    if self._level == 0 or self._missionReported : return
    self._missionReported = True
    if self._solution == False:
      self._missionInfo(f'UNDECIDED', 'No solution defined', 'Try define a solution with levels','white')  
    elif self._actions == 0:
      self._missionInfo(f'NOT STARTED', 'Start thinking and coding', 'start at level 0','white')  
    else:
      fails = []
      if self._criticals['e'] > 0:
        fails.append('errors encountered')
      if not self._solutionDone:
        fails.append('solution not reached')
      if self._level > 0 and self._limitLines != False and self._lines > self._limitLines:
        fails.append('too many code lines')
      if self._level > 2 and self._limitActions != False and self._actions > self._limitActions:
        fails.append('too many actions')
      if self._level > 2 and self._criticals['w'] > 0:
        fails.append('warnings given')
      if self._scansMin and self._scans < self._scansMin:
        fails.append(f'less than {self._scansMin} scans')
      if self._level > 2 and self._scansMax and self._scans > self._scansMax:
        fails.append(f'more than {self._scansMax} scans')        
      if fails:
        sup = ' AND ABORTED' if self._aborted else ''
        info1 = 'Mission not yet accomplished. Lets work on it!'
        info2 = 'because: ' + ', '.join(fails)
        self._missionInfo(f'FAILED'+sup, info1, info2,'red')
      else:
        info1 = 'Mission accomplished. Congrats!'
        if self._level == 3:
          info2 = 'Try another challenge!'
        else:
          info2 = 'Try a higher level!'
        self._missionInfo(f'ACCOMPLISHED', info1, info2,'green')    
      
  def report(self):
    self._reportMission()
    self._wait()
  
  def wait(self):
    self._wait()

  @staticmethod
  def help():
    print(help)
  
  def helpChallenge(self):
    print(helpChallenge)

  def _reconstructYard(self,yard):
    _yard = []
    stacks = yard.split(',')
    for stack in stacks:
      _yard.append(list(stack))
    return _yard

  def showSolution(self,seconds=0):
    _yard = self.serializeYard(self._yard)
    if type(self._solution) == str:
      _solution = self._solution
    elif callable(self._example):
      _solution = self._example(_yard,self._criteria)
    else: return

    self._yard = self._reconstructYard(_solution)
    self._animate('idle')
    
    if seconds > 1:
      print(self._colored(f'Showing solution for {seconds} seconds','yellow'))
      pygame.time.delay(seconds*1000)
      self._yard = self._reconstructYard(_yard)
      self._animate('idle')
    else:
      print(self._colored(f'Showing solution','yellow'))
      self._aborted = True

    self._wait()


if __name__ == "__main__":
  print('tested module RobotArm')


