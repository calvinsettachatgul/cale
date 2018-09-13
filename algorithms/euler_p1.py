'''
https://projecteuler.net/problem=1
1) Look for pattern:
   if number is 15, multiples of 3 = 3,6,9,12   >>>sum=45
                                 5 = 5,10
                30, multiples of 3: 15,18=15+3,21=15+6,24=15+9,27=15+12
                                 5: 15, 20, 25 >>>sum=150
                45, multiples of 3: 30, 30+3, 30+6, 30+9, 30+12
                                    30, 30+5, 30+10 >>>sum=30+33=63
                                    total=258
    if number is 35,
    multiple=(number-1)//15=2
    remainder = number%15=5
    big_number=45*(multiple)+15*(7)*(multiple-1)=45*2+15*7*1=195
    last_row_sum=3+(multiple*15*2)=63
              
multiplier = 1

the first numbers to add are 3 and 5

iterate by increasing the multiplier

three_sum = 3*multiplier
five_sum = 3*multiplier

n = 35
                three_sum  five_sum
multiplier = 1 3 5
multiplier = 2 6 10
multiplier = 3 9 15
multiplier = 4 12 20
multiplier = 5 15 25
multiplier = 6 18 30
multiplier = 7 21 35
multiplier = 8 24 
multiplier = 9 27 
multiplier = 10 30 
multiplier = 11 33 
multiplier = 12 36 

create set  so that the numbers are unique

if three_sum < input_number push to set
or 
if five_sum < input_number push to set
    
'''
def sum_multi(num):
    fact = 1
    sum_three = sum_five = 0
    all_factors = set()
    while(sum_three < num or sum_five < num):
        sum_three = 3 * fact
        sum_five = 5 * fact
        if(sum_three < num):
            all_factors.add(sum_three)
        if(sum_five < num):
            all_factors.add(sum_five)
        fact += 1
    return sum(all_factors)
    
# print(sum_multi(15) == 45)
# print(sum_multi(5) == 3)
print(sum_multi(35))
print(sum_multi(1000))


def sum_multiples(below_num):
    num1=((below_num-1)//15)
    if num1<0:
        num1=0
    if below_num==15:
        remainder=15
    else:
        remainder = below_num%15
    base_case=[3,5,6,9,10,12]
    sum_base_case=45
    last_row_sum=big_number=0
    print("num1,remainder", num1,remainder)
    '''
    calculating the big sum
    
    
    calculating the sum in the remainder 
    '''
    count=0
    for num in base_case:
        if num<remainder:
            last_row_sum +=num
            count +=1
    
    if num1==2:
        sum_of_sequence=1
    elif num1>2:
        num1 -=1
        sum_of_sequence=(num1+1.0)/2*num1
        num1 +=1
    else:
        sum_of_sequence=0
    
    big_number=45*(num1)+15*7*sum_of_sequence
    last_row_sum=last_row_sum+(num1*15*(count+1))
    
    print("last row sum", last_row_sum)
    print("big number",big_number, 45*(num1), 15*7*sum_of_sequence, sum_of_sequence)
     
    sum=big_number+last_row_sum
    return sum

print(sum_multiples(1000))
# print(sum_multiples(35))
print(sum_multiples(55))
# print(sum_multiples(5))