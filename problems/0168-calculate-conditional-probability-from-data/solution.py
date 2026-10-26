import math

def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here

    n = 0 
    m = 0

    for i in data:
      if(i[0]==x and i[1]==y):
        n+=1
      
      if (i[0]==x):
        m+=1
    
    if(n!=0 and m!=0):
      val=n/m
      return round(val, 4)
    else:
      return 0
    

