import csv, operator

op_list = {
    
    '<': operator.lt,
    '=': operator.eq,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '!=': operator.ne
    
}

ms = list(csv.DictReader(open("search.csv", 'r'), delimiter=','))

print(ms[0])

name = input("Write vaguely what the name of the card is:").lower()

cmc = input("CMC value: ") or 0
op = input("Operator: ") or '>='
tp = input("Type: ") 

for i in ms:
    if (name in i['name'].lower()) and (op_list[op](i['cmc'], cmc)) and (tp in i['type_line'].lower()):
        print(i['name'])
