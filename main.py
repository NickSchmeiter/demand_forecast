import ExponentielleGlättung2Ordnung as e
import HoltWinterVerfahren as h

def main():
    #erste zeitreihe im vergleich
    e.exponentielle_glättung_2ter_Ordnung()
    h.holt_winter_verfahren(alpha=0.5,b1=200,b2=225,b3=270,b4=225,b5=240,b6=310,b7=335,b8=370,b9=340,b10=310,b11=320,b12=330)
    #zweite zeitreihe im vergleich
    e.exponentielle_glättung_2ter_Ordnung(alpha=0.563,b0=68,b1=58,b2=76,b3=89,b4=98,b5=78,b6=110,b7=122,b8=137)
    h.holt_winter_verfahren()
    #dritte zeitreihe im vergleich
    e.exponentielle_glättung_2ter_Ordnung(alpha=0.6, b0=1000, b1=1111, b2=1200, b3=900, b4=1050, b5=1200, b6=1300, b7=1350, b8=1330)
    h.holt_winter_verfahren(alpha=0.6, b1=1000, b2=1111, b3=1200, b4=900, b5=1050, b6=1200, b7=1300, b8=1350, b9=1330, b10=1410,b11=1320, b12=1200)
main()