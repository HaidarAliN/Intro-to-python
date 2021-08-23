#cubic root using Bisection search

def cubic_root(x): 
    start = 0
    end = x
    eps = 0.001 #deffine eps
    while True:
        mid = (start + end) //2
        cube = mid * mid * mid
        if cube == x:
            return mid
        if cube < x :
            start = mid + 1
        else:
            end = mid - 1 
        if start == end:
            cube = start * start * start
            if cube > x:
                start = start - 1 + eps
                end = end - eps 
            else:
                start = start + eps
                end = end + 1 - eps
            while True:
                mid = round(((start + end) / 2),3)
                cube = mid * mid * mid
                if start == end:
                    if cube > x:
                        return round((mid-eps),3)
                    else:
                        return mid 
                if cube == x:
                    return mid
                if cube < x:
                    start = round((mid + eps ),3)
                else:
                    end = round((mid - eps),3)

#perfect number
def perfect(number): 
      is_perfect = False
      sum = 0  
      div = 1
      while div<number:
          if number%div == 0:
              sum += div
          div += 1
      if sum == number:
          is_perfect = True
      return is_perfect

#cubic
def cubic_root2(n):
    start = 0
    end = n
    eps = 0.00001
    guess = (start + end) / 2
    while abs(guess ** 3 - n) >= eps:
        if guess ** 3 == n:
            return guess
        if guess ** 3 > n:
            end = guess
        else:
            start = guess
        guess = (start + end) / 2
    return round(guess,3)

