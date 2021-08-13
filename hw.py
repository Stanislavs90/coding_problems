nums = [7,1,5,3,6,4]
#nums = [1,2,3,4,5]

def maxprofit(nums):
    """
    new_dict = {}
    new_array = []
    loop over array 
        loop over array, increment by one each iteration


    add profit to array
    add how to get profit to dictionary 
    Buy 1 Sell 2
    """

    m = {}
 
    # max after every iteration 
    maxprofit = []


    for i in range(0, len(nums)):
        profit = []

        for j in range(i+1, len(nums)):
            if (nums[j] - nums[i]) > 0:
            # Buy_day - Sell day
                answer = nums[j] - nums[i]
                profit.append(answer)
                
                print("Buy", nums[i], "Sell", nums[j], "Profit",(nums[j] - nums[i]))
            # add to dict
            # profit as key
            #m[answer] = "Buy", nums[i], "Sell", nums[j]

            # B1 S2 as value



        if len(profit) != 0:
            maxprofit.append(max(profit))


    return maxprofit, m


print(maxprofit(nums))