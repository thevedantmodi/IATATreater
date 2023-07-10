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

CN_good_ports = ["PEK", "PVG", "CAN", "CTU"]
# Prints all the CN airports that are not internationally significant enough
for port in airports:
    if (airports[port]['country'] == 'CN' and not port in CN_good_ports):
        print(airports[port]['iata'])

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
USairports = 0
for port in airports:
    if (airports[port]['country'] == 'US'):
        USairports += 1
print(USairports)

# Prints significant AU airports
AU_good_ports = ["ADL","BNE","CBR","MEL","PER","SYD"]
for port in airports:
    if (port in AU_good_ports):
        print(port)

