import random
import numpy as np


def simulate_dice_sum(num_rolls, seed=0):
    
    rng = np.random.RandomState(seed)
    d1=rng.randint(1,7,size=num_rolls)
    d2=rng.randint(1,7,size=num_rolls)
    sums= d1+d2
    
    empirical = np.zeros(11)
    
    if num_rolls > 0:
        counts = np.bincount(sums)

        empirical = counts[2:13].astype(float)/num_rolls

    s_values = np.arange(2, 13)
    theoretical = (6- np.abs(s_values - 7))/36

    return empirical, theoretical