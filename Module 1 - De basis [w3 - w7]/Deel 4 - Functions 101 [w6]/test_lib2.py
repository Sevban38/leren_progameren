import sys,time
import builtins
import re
from colorama import init
from termcolor import colored

MAX_REPORT_STRING = 100

init()

data = {'results':[], 'inputs': [], 'prompts': [], 'prints': [], 'active': True}

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    builtins.print(txt.format(*vars))

def feed_inputs(*values):
  for value in values:
    data['inputs'].append(value)

def expect_prompts(*values):
  for value in values:
    data['prompts'].append(value)

def expect_prints(*values):
  for value in values:
    data['prints'].append(value)

def start():
  data['active'] = True

def stop():
  data['active'] = False

def add_test_result(txt:str='{}', vars:list=[], color:str='yellow'):
  data['results'].append({"txt": txt, "vars": vars, "color": color })

def type_text(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def input(prompt: str = ''):
  # global data
  builtins.print(prompt,end='')
  if data['active']:
    if len(data['prompts']) > 0:
      expected_prompt = data['prompts'].pop(0)
      if expected_prompt != '*':
        test('Input prompt',expected_prompt, prompt)
    if len(data['inputs']) > 0:
      input_data = data['inputs'].pop(0)
      type_text(input_data+'\n')
      return input_data

  return builtins.input()

def print(*args, **kwargs):
  builtins.print(*args,**kwargs)
  if data['active']:
    total_text = ''
    for text in args:
      total_text += str(text)
    if len(data['prints']) > 0:
      expected_print = data['prints'].pop(0)
      if expected_print != '*':
        test('Print text',expected_print, total_text)
  return None

def str_type(s):
  return str(s).replace('<class \'','').replace('\'>','')

def str_more(s: str, max: int) -> str:
  if len(s) > max:
      return s[:max] + "..."
  else:
      return s  

def test(name: str, expect: any, value: any):
  passed = False
  type_expected = ''
  is_regex = False
  is_range = False
  is_regex = type(expect) == dict and 're' in expect
  is_range = type(expect) == dict and 're' not in expect
  if is_regex:
    type_expected = expect['re']
    if 'min' in expect:
      min = expect['min']
    else:
      min = 1
    if 'max' in expect:
      max = expect['max']
    else:
      max = 1
    if max < min:
      max = min
  if is_range:
    if 'min' in expect:
      min = expect['min']
    else:
      min = float('-inf')
    if 'max' in expect:
      max = expect['max']
    else:
      max = float('inf')
    if max < min:
      max = min 
    type_expected = f'{min} <= expected < {max}'
  if is_regex:
    matches = x = re.findall(expect['re'], value)
    passed = min <= len(matches) <= max
  elif is_range:
    passed = min <= value <= MAX_REPORT_STRING
  else:
    type_expected = type(expect)
    if value == expect and type(expect) == type(value):
      passed = True
  if passed:
    add_test_result(txt = '{}: ' + name, vars=['success'], color='green')
    add_test_result(txt = '  for:      {}', vars=[str(expect)], color='white')
    if is_regex:
      add_test_result(txt = '  with:     {}', vars=[str(value)], color='white')
    
  else:
    add_test_result(txt = '{}: ' + name, vars=['failed'], color='red')
    expect_str = str_more(str(expect),60)
    add_test_result(txt = '  expected: {} : {}', vars=[str_type(type_expected),str_more(str(expect),MAX_REPORT_STRING)])
    add_test_result(txt = '  got:      {} : {}', vars=[str_type(type(value)),str_more(str(value),MAX_REPORT_STRING)])
  add_test_result(txt = '')
  return passed

def report():
  builtins.print('\n******** TEST REPORT *********')
  if len(data['results']) == 0 and not data['active']:
    print('Test not started, no test results!')
  while len(data['results']) > 0:
    line = data['results'].pop(0)
    print_colorvars(txt=line['txt'],vars=line['vars'], color=line['color'])
