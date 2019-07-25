symbols = '$¢£¥€¤'
codes=[]
for symbol in symbols:
    codes.append(ord(symbol))
    
codes = [ord(symbol) for symbol in symbols]

# list comp
beyond_ascii = [ord(s) for s in symbold if ord(s) > 127]

# lambda operator
beyond_ascii = list(filter(lambda c:c > 127, map(ord, symbols)))

print('debug stop')
