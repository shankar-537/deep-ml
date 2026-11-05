import math

def chi_square_probability(x, k):
    """
    Calculate the probability density of x in a Chi-square distribution
    with k degrees of freedom.
    """
    # your code here
    normalize = 1/(math.exp2(k/2)*math.gamma(k/2))

    probability = normalize * (math.pow(x, (k/2)-1)) * (math.exp(-x/2))

    if (x<0 or k<=0):
        return 0.0
    elif( x == 0 ):
        if((k/2)-1 == 0):
            probability = normalize * (1) * (math.exp(-x/2))
        else:
            return round(probability, 3)
        return round(probability, 3)
    else:
        return round(probability, 3)