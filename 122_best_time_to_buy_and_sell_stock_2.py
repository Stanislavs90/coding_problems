# #array = [7,1,5,3,6,4]
# array = [1,2,3,4,5]
# #array = [7,6,4,3,1]

# def maxprofit(array):
#     for i in range(len(array)):
#         one = array[i -1] + array[i]
#         two = array[i -2] + array[i]

#     return  one,two

# print(maxprofit(array))


# ------------------------------------------------------------------
"""

Input: [7,1,5,3,6,4]
          i j



Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

buyprice = 

if i > j :
    sell i
    i++
    j++
    
elif i < j:
    buy i
    i++
    j++

else: 
    i++
    j++


    profit = salesprice - buyprice

    ---------------------------------------

loop over array 
maxprofit = prices[i]

# """
# prices = [7,1,5,3,6,4]


# def profit(prices):
#     i=0
#     j=1
#     maxprofit = []
#     salesprice = 0 
#     buyprice = 100

#     while j < len(prices):
#         if prices[j] < prices[i]:
#             salesprice = prices[i]
#             buyprice = prices[j]
#         maxprofit += salesprice - buyprice
        
#         if prices[j] > prices[i]:
#                 buyprice = prices[i]
#                 salesprice = prices[j]
#         maxprofit += salesprice - buyprice
#     return maxprofit

# print(profit(prices))    

#-------------------------------------------------

# Works for second array 


#array = [7,1,5,3,6,4]
#array = [1,2,3,4,5]
#array = [7,6,4,3,1]


# def maxprofit(prices):
#     buyprice = float('inf')
#     profit = []
#     for i in range(len(prices)):
#         if prices[i] < buyprice:
#             buyprice = prices[i]

#         if prices[i] > buyprice:
#             # for i in range
#             for j in range(i, len(array)):
#             # if i + 1 > i dont sell
#             # max(?, ?)s
#                 profit = prices[j] - buyprice
#                 print(profit)
#             buyprice = float('inf')

#     return profit


# print(maxprofit(array))


# ----------------------------------------------------

# works for 1 and 3 array 

array = [7,1,5,3,6,4]
#array = [1,2,3,4,5]
#array = [7,6,4,3,1]
 

def maxprofit(prices):
    buyprice = float('inf')
    profit = 0
    for price in prices:
        # update buy price to lowest found in array so far
        if price < buyprice:
            buyprice = price

        if price > buyprice:

            profit += price - buyprice

            # sell 
            buyprice = float('inf')

    return profit


print(maxprofit(array))

