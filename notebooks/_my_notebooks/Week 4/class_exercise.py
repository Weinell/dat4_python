import numpy as np
import pandas as pd

""" if __name__ == '__main__':
    a = np.arange(10,30).reshape(4,5)

    print(a)

    yellow = a[0,0]
    cyan = a[::1,1::2]
    green = a[0:3,2]
    blue = a[0::2,-1]



    print('Yellow:\n',yellow,'\nCyan:\n',cyan,'\nGreen:\n',green,'\nBlue:\n',blue)
 """

def sortPeople(AAR, BYDEL, ALDER, STATKODE) -> int:
    maskAAR = dd[:,0] == AAR
    maskBYDEL = dd[:,1] == BYDEL
    maskALDER = dd[:,2] == ALDER
    maskSTAKODE = dd[:,3] == STATKODE

    return np.sum(dd[maskAAR & maskBYDEL & maskALDER & maskSTAKODE][:,4])

def sumAllAges(AAR, BYDEL, STATKODE, ALDER=None) -> int:
    maskAAR = dd[:,0] == AAR
    maskBYDEL = dd[:,1] == BYDEL
    maskALDER = dd[:,2] == ALDER
    maskSTATKODE = dd[:,3] == STATKODE

    if ALDER == None:
        return np.sum(dd[maskAAR & maskBYDEL & maskSTATKODE][:,4])

    return np.sum(dd[maskAAR & maskBYDEL & maskALDER & maskSTATKODE][:,4])

def mask(array,pos,arg):
    mask = array[:,pos] == arg
    return mask

def sumAllCitizensAllAreas(dd, AAR, BYDEL=None, STATKODE=None, ALDER=None) -> int:
    args = [AAR, BYDEL, STATKODE, ALDER]
    goodMasks = []
    counter = 0
    for arg in args:
        if arg != None:
            dd = dd[mask(dd,0,arg)]
            

    print(np.sum(dd[:,4]))

    return 0
    return np.sum(dd[maskAAR & maskBYDEL & maskALDER & maskSTATKODE][:,4])


if __name__ == '__main__':

    dataLoc = '../../data/befkbhalderstatkode.csv'

    df = pd.read_csv(dataLoc)

    dd = df.to_numpy()

    print(dd)
    print(dd.shape)

    maskYear = dd[:,0] == 2015
    maskGerman = dd[:,3] == 5180
    maskAge = dd[:,2] == 0

    sort = np.sum(dd[maskYear & maskGerman & maskAge][:,4])
    print(sort)

    mySort = sortPeople(2015,1,0,5180)
    print(mySort)

    sumAge = sumAllAges(2015,1,5180)
    print(sumAge)

    print(sumAllCitizensAllAreas(dd, 2015))
