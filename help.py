nums = [7,1,5,3,6,4]
#nums = [1,2,3,4,5]
#nums = [5,4,3,2,1]

def maxprofit(nums):
    """
    profit array = []

    loop over array
        loop over array ,increment 1 over first loop
            if i+1 > i:
                find profit
                add profit to array
                take the max of that profit 
                add to max profit array 
    """
    max_values = 0
    for i in range(0, len(nums)):
        profit_array=[]

        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                profit = nums[j] - nums[i]
                profit_array.append(profit)
                continue
                # try kadane's

                print("Buy", nums[i], "Sell", nums[j], "profit",profit)
                

        if len(profit_array) > 1:
             max_values += max(profit_array)

    return max_values


print(maxprofit(nums))