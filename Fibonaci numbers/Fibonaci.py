#           THIS PROBLEM IS FETCHED BY PROJECTEULER.NET and IT is the solution for that PROBLEM!!! :-)

# We have a list named as fb_nums which initially stores a var(1) inorder to get further vars
fb_nums = [1]
# The result or the even fibocani nums will be stroed in this empty list
Even_fb_nums = []

# Defining the function EvnFibNums()..which will take an argument rng i.e the limit for our fib_nums
def EvnFibNum(rng):
    n = 0                    # n will increase everytime the loop runs
    res = 2*fb_nums[0]
# Finding all the fibonaci nums within the limit
    while res <= rng:
        fb_nums.append(res)
        res += fb_nums[n]
        n += 1
# Checking which of them are even....and the result will be stored in the Even_fb_nums[]!!
    for m in fb_nums:
        if m % 2 == 0:
            Even_fb_nums.append(m)
    print(Even_fb_nums)    # Our Result....Yepp We Are Done!!The result is amazing

#Calling the Function
EvnFibNum(1000000)

#    This code is optimized
                # coded by :- Nikhil Bhuyan(Me)

# IF THIS CODE CAN BE IMPROVED THEN PLZZ CONTACT ME ON MY E-MAIL (nikhilbhuyan17@gmail.com)
