def reverse_string(input_string):
    
    if (input_string == None):
        return None
        
    result = input_string
    
    # if(len(input_string) > 1):
    #     return input_string[1] + input_string[0]
    # if(len(input_string) > 1):
    #     return input_string[::-1]
    
    if(len(input_string)> 1):
        result=''
        for x in range(len(input_string)-1,-1,-1):
            result +=input_string[x]
    
    return result