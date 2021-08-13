nums = [7,1,5,3,6,4]

array[i][j] = {-10000} # negative invinity

def maxprofit(nums):

    for i in range(len(nums)) :
        for j in range(i + 1, len(nums)) :
            buy_price = num[i]
            sell_price = numb[j]
            array[i][j] = sell_price - buy_price

    

















print(maxprofit(nums))