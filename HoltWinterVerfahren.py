
from numpy import NaN
import pandas as pd
import matplotlib.pyplot as plt
def holt_winter_verfahren(alpha=0.563,beta=0.372,gamma=0.179,b1=68,b2=58,b3=76,b4=89,b5=98,b6=78,b7=110,b8=122,b9=137,b10=119,b11=150,b12=168):

    data = { '1': [b1], '2': [b2], '3': [b3], '4': [b4], '5': [b5], '6': [b6], '7': [b7], '8': [b8],
            '9': [b9],'10': [b10],'11': [b11],'12': [b12],'13': [NaN],'14': [NaN],'15': [NaN],'16': [NaN]}
    df = pd.DataFrame(data, index=['Bedarf', 'Niveau', 'Trend', 'Saisonalekomponente', 'Prognose', '|Prognosefehler|'])
    df.iloc[1:3,0:4]='-'
    df.iloc[4:6, 0:5] = '-'
    #set first trend
    df.iloc[2,4]=(df.iloc[0,4]-df.iloc[0,0])/4
    #set first seasonal components
    for i in range(4):
        df.iloc[3,(i)]=df.iloc[0,(i)]/(df.iloc[2, 4]*(i+1)+df.iloc[0,0]-df.iloc[2, 4])
    #for t=6 til t=12
    for i in range(5,12):
    #set niveau components
        df.iloc[1,i]=alpha*df.iloc[0,i]/df.iloc[3,i-4]+(1-alpha)*(df.iloc[1,i-1]+df.iloc[2,i-1])
    #set trend components
        df.iloc[2,i]=beta*(df.iloc[1,i]-df.iloc[1,i-1])+(1-beta)*df.iloc[2,i-1]
    #set seasonal components
        df.iloc[3,i-1]=gamma*df.iloc[0,i-1]/df.iloc[1,i-1]+(1-gamma)*df.iloc[3,i-5]
    # calculate forecast
        df.iloc[4, i] = (df.iloc[1, i - 1] + df.iloc[2, i - 1]) * df.iloc[3, i - 4]
    # calculate absolute error
        df.iloc[5,i] = abs(df.iloc[0,i]-df.iloc[4,i])
    #calculate MAD
    df.iloc[5,12]=df.iloc[5,5:11].sum()/7
    #set last seasonal component
    df.iloc[3, 11] = gamma * df.iloc[0, 11] / df.iloc[1, 11] + (1 - gamma) * df.iloc[3, 11-4]
    #calculate forecast for t=13 til t=16
    for i in range(12,16):
        df.iloc[4,i] = (df.iloc[1,11]+df.iloc[2,11]*(i-11))*df.iloc[3,i-4]
    #print df and forecast
    pd.set_option('display.max_columns', None)
    print(df)
    print('Die mittlere absolute Abweichung beim Holt-Winters-Verfahren bei Alpha: ' + str(alpha) + ' Beta: '+str(beta) + ' Gamma: ' + str(gamma) + ' beträgt: ' + str(df.iloc[5, 12]) + ' !')
    #print plot
    dfplot = pd.DataFrame()
    dfplot['Bedarf'] = df.loc['Bedarf']
    dfplot['Prognose Holt Winter'] = df.iloc[4,5:15]
    dfplot.plot()
    plt.ylim(0, (df.iloc[4, 15] * 1.66))
    plt.show()