import airportsdata
import pandas as pd
import sys, os, shutil, time

airports = airportsdata.load('IATA')

def read(filename):
    try:
        df = pd.read_csv(filename, header=None)
        print(df)
    # df.rename(index=str.strip)
    except:
        print("Could not open file, check path", file=sys.stderr)
        exit()
    
    return df

def mkout():
    try:
        if (os.path.isdir(sys.argv[2])):
            rmedir(sys.argv[2])
        os.mkdir(sys.argv[2])
    except:
        print("Could not create output dir, check permissions", file=sys.stderr)
        exit()

def rmedir(dirpath):
    while True: 
        qr = input("Do you want to delete and replace the existing \
directory and all the files at " + dirpath+ "? (y/n) ") 
        if qr == '' or not qr[0].lower() in ['y','n']:print('[y/n]') 
        else:break 
    if qr[0].lower() == 'y':
        shutil.rmtree(dirpath)
        return 
    if qr[0].lower() == 'n':
        return

df = read(sys.argv[1])
mkout()

# Pass over whole list to make sure each code is valid
for index, code in df.items():
    df.at[0,index] = df.at[0,index].strip()
    print(df.at[0,index])
    try:
        country = airports[df.at[0,index]]['country']
    except KeyError:
        print("Could not find", index)
        df = df.drop(index, axis=1)
        # df.drop(str(code), axis=0,inplace=True)
        continue    

print("\n\n\n\n\nfinding country")
# Finding country, after passing through and making sure each code is valid
countries = []
unique_countries = set()
for index, code in df.items():
    country = airports[df.at[0,index]]['country']
    countries.append(country)
    unique_countries.add(country)

df.loc[len(df.index)] = countries
df.sort_values(by=[1],axis=1, inplace=True)
print(df)

paths = []
countryNames = []
files = []
for code in unique_countries:
    filename = sys.argv[2] + "/" + code
    file = open(filename, "x")
    countryNames.append(code)
    paths.append(filename)
    files.append(file)

EAGLE = ["US"]
for x in range(len(countryNames)):
    code = countryNames[x]
    filepath = paths[x]
    ports = []
    for index, code in df.items():
        if (countryNames[x] == df.at[1,index]):
            ports.append(df.at[0,index])

    print(ports)
    with files[x] as f:
        count = 0
        for elem in ports:
            if (count == len(ports) - 1):
                f.write(elem)
            else:
                f.write(elem + ", ")
            count += 1