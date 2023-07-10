import airportsdata
import pandas as pd
import sys, os, shutil, time

airports = airportsdata.load('IATA')

def read(filename):
    try:
        df = pd.read_csv(filename).transpose()
        df.rename(index=str.strip)
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


countries = []
unique_countries = set()
for code, index in df.iterrows():
    code = code.strip()
    country = airports[code]['country']
    countries.append(country)
    unique_countries.add(country)

df['countries'] = countries


df.sort_values(by=['countries'], inplace=True)


paths = []
countryNames = []
files = []
for code in unique_countries:
    filename = sys.argv[2] + "/" + code + ".txt"
    file = open(filename, "x")
    countryNames.append(code)
    paths.append(filename)
    files.append(file)

EAGLE = ["US"]
for x in range(len(countryNames)):
    code = countryNames[x]
    filepath = paths[x]
    filter = df.query("countries == @code")
    del filter['countries']
    with files[x] as f:
        list = filter.index.values.tolist()
        count = 0
        for port in list:
            if (count == len(list) - 1):
                f.write(port)
            else:
                f.write(port + ", ")
            count += 1