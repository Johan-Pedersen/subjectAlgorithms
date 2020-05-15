#Pattern matching
from BoyerMoores_algoritme import PatternMatch


#abilities er et string array
def deathKnight(abilities):
    pm = PatternMatch()

    wins  =0
    for a in abilities:
        if pm.Boyer_Moores(a, "CD") == -1:
            wins += 1
    
    return wins

abilities = ["DCOOO", "DODOCD", "COD"]
print(deathKnight(abilities))