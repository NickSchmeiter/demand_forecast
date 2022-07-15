import pandas as pd
from numpy import NaN
import matplotlib.pyplot as plt



def exponentielle_glättung_2ter_Ordnung(alpha=0.5, b0=200, b1=200, b2=225, b3=270, b4=225, b5=240, b6=310, b7=335, b8=370):
    # Dataframe for 9 periods created
    data = {'0': [b0], '1': [b1], '2': [b2], '3': [b3], '4': [b4], '5': [b5], '6': [b6], '7': [b7], '8': [b8],'9': [NaN]}
    df = pd.DataFrame(data, index=['Bedarf', 'G1', 'G2', 'Achsenabschnitt', 'Steigung', 'Prognose2terOrdnung','|Prognosefehler|'])
    # calculate b
    df.iloc[3, 0] = df.iloc[0, 0]
    Achsenabschnitt = df.iloc[3, 0]
    # calculate gradient
    Steigung = (df.iloc[0, 8] - df.iloc[0, 1]) / 7
    df.iloc[4, 0] = Steigung
    # calculate g1 t=0
    df.iloc[1, 0] = Achsenabschnitt - Steigung * (1 - alpha) / alpha
    # calculate g2 t=0
    df.iloc[2, 0] = Achsenabschnitt - 2 * Steigung * (1 - alpha) / alpha
    # calculate g1 t=n
    for i in range(1, 9):
        df.iloc[1, i] = (1 - alpha) * df.iloc[1, i - 1] + alpha * df.iloc[0, i]
    # calculate g2 t=n
    for i in range(1, 9):
        df.iloc[2, i] = df.iloc[2, i - 1] + alpha * (df.iloc[1, i] - df.iloc[2, i - 1])
    # calculate b for t=n
    for i in range(1, 9):
        df.iloc[3, i] = 2 * df.iloc[1, i] - df.iloc[2, i]
    # calculate gradient for t=n
    for i in range(1, 9):
        df.iloc[4, i] = alpha / (1 - alpha) * (df.iloc[1, i] - df.iloc[2, i])
    # calculate forecast
    df.iloc[5, 0] = NaN
    for i in range(1, 10):
        df.iloc[5, i] = df.iloc[3, i - 1] + df.iloc[4, i - 1]
    # calculate error
    df.iloc[6, 0] = NaN
    for i in range(1, 9):
        df.iloc[6, i] = abs(df.iloc[0, i] - df.iloc[5, i])
    # calculate Mean absolute error
    df.iloc[6, 9]=df.iloc[6].sum() / 8
    # print df and forecast
    pd.set_option('display.max_columns', None)
    print(df)
    print('Die mittlere absolute Abweichung bei der exponentiellen Glättung zweiter Ordnung bei einem Alpha: '+str(alpha)+'  beträgt: '+str( df.iloc[6, 9])+' !' )
    # print plot
    dfplot = pd.DataFrame()
    dfplot['Bedarf'] = df.loc['Bedarf']
    dfplot['Prognose2terOrdnung'] = df.loc['Prognose2terOrdnung']
    dfplot.plot()
    plt.ylim(0, (df.iloc[5, 9] * 1.333))
    plt.show()
