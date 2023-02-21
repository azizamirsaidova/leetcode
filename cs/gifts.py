"""
-> each coupon is going to be used before it expires
-> decided when every gift should be bought

gift n = [3,4,5]
price of the gift  j = [10,15,17]
coupons  m = [1,2, 3]

coupon expiration day t = [31, 27, 30]
coupon discount  d = [20, 14, 25]

Alice would like to use her coupons to minimize the total cost of all gifts. 
To do so, she needs to decide when she will buy each gift and what coupon to use for each purchase.

assign lowest_price to 0
sort the coupon from highest to lowest [3,2,1]
sort the prices from highest to lowest [17,15,10]

iterate over the lenth of coupons 
    match the ith of the coupon to ith of the price 
    if there is an index in prices or coupon not in either, assign zero (For example if you have more coupons than prices, then assign zero to price for the missing index so that the coupon is not used and if you have more gift)
    if you have more gift prices than coupon assign zero to discount so that 1-d is one and no discount is applied
    
    calculate the total price of gift with coupon (1 - d_i)p_j and pass to curr_total_price
    append curr_total_price to lowest_price
return to min value from lowest_price
    
    

edge cases:
- there exist more gifts than coupons 
"""

