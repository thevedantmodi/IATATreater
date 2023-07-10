import airportsdata

airports = airportsdata.load('IATA')

# Gets the number of non FAA airports
nonFAA = 0
for port in airports:
    if (airports[port]['lid'] == ""):
        nonFAA += 1
    
print("number of non FAA airports", nonFAA) # 5819

# Gets the number of non IATA airports (only ICAO)
    # Already removed because loaded by IATA key duh!
nonIATA = 0
for port in airports:
    if (airports[port]['iata'] == ''):
        nonIATA += 1
    
print("number of non IATA airports", nonIATA) # 0

# Prints all the CN airports
for port in airports:
    if (airports[port]['country'] == 'CN'):
        print(airports[port]['city'])

# Prints all the empty city airports (everything needs a city!)
for port in airports:
    if (airports[port]['city'] == ''):
        print(airports[port]['name'], airports[port]['country'])

# Does a ICAO only airport exist? (sanity check)
ICAO = False
for port in airports:
    if (airports[port]['name'] == "Williams Ag Airport"):
        ICAO = True

print("ICAO found:", ICAO)

# Prints the number of US airports
for port in airports:
    if (airports[port]['country'] == 'US'):
        print(airports[port]['city'])