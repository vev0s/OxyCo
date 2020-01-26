from core.dict import *

dictUTF8Reverse = valuesUTF8.copy()
valuesReverseUTF8 = dict([[v,k] for k,v in dictUTF8Reverse.items()])

dictCesarReverse = valuesCesar.copy()
valuesReverseCesar = dict([[v,k] for k,v in dictCesarReverse.items()])
