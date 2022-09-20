import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataLoc = '../../data/befkbhalderstatkode.csv'

df = pd.read_csv(dataLoc)

dd = df.to_numpy()

print(dd)
print(dd.shape)

print(df)

#3166

def sortPeople(AAR, BYDEL) -> int:
    maskAAR = dd[:,0] == AAR
    maskBYDEL = dd[:,1] == BYDEL
    #maskALDER = dd[:,2] == ALDER
    #maskSTAKODE = dd[:,3] == STATKODE

    return np.sum(dd[maskAAR & maskBYDEL][:,4])


if __name__ == '__main__':
    
    indreBy = sortPeople(2015, 1)
    østerbro = sortPeople(2015, 2)
    nørrebro = sortPeople(2015, 3)
    vesterbro = sortPeople(2015, 4)
    valby = sortPeople(2015, 5)
    vanlose = sortPeople(2015, 6)
    bronshoj = sortPeople(2015, 7)
    bispe = sortPeople(2015, 8)
    amagerEast = sortPeople(2015, 9)
    amagerWest = sortPeople(2015, 10)
    outside = sortPeople(2015, 99)

    data = {
    'Indre':indreBy,
    'Øster':østerbro,
    'Nørre':nørrebro,
    'Vester':vesterbro,
    'Valby':valby,
    'Vanløse':vanlose,
    'Bronshøj':bronshoj,
    'Bispe':bispe,
    'AmagerEast':amagerEast,
    'AmagerWest':amagerWest,
    'Outside':outside
    }

    cities = list(data.keys())
    population = list(data.values())
    print(cities)
    print(population)


    plt.bar(cities,population)
    plt.show()

    maskAar = dd[:,0] == 2015
    maskAge65 = dd[:,2] >= 65
    maskCopenhagen = dd[:,1] != 99

    above65 = np.sum(dd[maskAar & maskAge65 & maskCopenhagen][:,4])
    print(above65)


def sortPeopleAge(AAR, BYDEL, ALDER) -> int:
    maskAAR = dd[:,0] == AAR
    maskBYDEL = dd[:,1] == BYDEL
    maskALDER = dd[:,2] == ALDER
    #maskSTAKODE = dd[:,3] == STATKODE

    return np.sum(dd[maskAAR & maskBYDEL & maskALDER][:,4])


    