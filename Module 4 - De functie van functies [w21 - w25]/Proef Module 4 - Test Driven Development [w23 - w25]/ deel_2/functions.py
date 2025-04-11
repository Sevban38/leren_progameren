import time
from termcolor import colored
from data import *
import math
from data import *


##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    silver_amount = copper2silver(amount)
    return round(silver2gold(silver_amount), 2)

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    copper = personCash.get('copper', 0)
    silver = personCash.get('silver', 0)
    gold = personCash.get('gold', 0)
    platinum = personCash.get('platinum', 0)

    total_gold = copper2gold(copper) + silver2gold(silver) + gold + platinum2gold(platinum)
    return total_gold

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horse:int) -> float:
    human_cost = COST_FOOD_HUMAN_COPPER_PER_DAY * people
    horse_cost = COST_FOOD_HORSE_COPPER_PER_DAY * horse
    total_cost = human_cost + horse_cost
    ultimate_cost = total_cost * JOURNEY_IN_DAYS
    return copper2gold(ultimate_cost)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item.get(key) == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    return getShareWithFriends(adventuring_people)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2) 

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    Journey = round(JOURNEY_IN_DAYS / 7)
    horse_cost = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    tent_cost = tents * COST_TENT_GOLD_PER_WEEK * Journey
    return silver2gold(horse_cost) + tent_cost

##################### O08 #####################

def getItemsAsText(items:list) -> str:
   zin = ""
   for index,item in enumerate (items): 
       amount = item['amount']
       unit = item['unit']
       name = item['name']
       zin += f"{amount}{unit} {name}"
       if index < len(items) - 2:
              zin += ", " 
       elif index == len(items) - 2:
           zin += " & "
   return zin
           
   
   
   
   
# item_texts = []
# for item in items:
#     amount = item['amount']
#     unit = item['unit']
#     name = item['name']
#     item_text = f"{amount}{unit} {name}"
#     item_texts.append(item_text)
# return ', '.join(item_texts).replace(', ', ' & ', len(item_texts) - 1)

def getItemsValueInGold(items:list) -> float:
    total_value = 0
    for item in items:
        amount = item['amount']
        price = item['price']
        price_amount = price['amount']
        price_type = price['type']
        item_value = amount * price_amount
        if price_type == 'copper':
            item_value = copper2gold(price_amount) * amount
        elif price_type == 'silver':
            item_value = silver2gold(price_amount) * amount
        elif price_type == 'gold':
            item_value = price_amount * amount
        elif price_type == 'platinum':
            item_value = platinum2gold(price_amount) * amount
        total_value += item_value
    return float(round(total_value, 2))

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()