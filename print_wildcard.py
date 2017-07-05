def print_wildcard(str):
    #seed values
    possible_list(str, '', 0)


#contract for each recursive call
def possible_list(str, result, index):
    """return a sublist of all possible combos."""
    # print str, result, index
    #stopping condition
    if len(result) == len(str):
        print result,
        return

    #branching logic here
    if str[index] != "?":
        possible_list(str, result+str[index], index+1)
    else:
        #next step, gets you closer to stopping condition
        possible_list(str, result + "1", index+1)
        possible_list(str, result + "0", index+1)

#result = '1' #index: 0
#result = '10' #index: 1
#result = '100' #index: 2    
#result = '1001'#stopping condition: len(result) = len(str)

print_wildcard("10?") #101, 100
print_wildcard("1?0?") #1000, 1001, 1100, 1101
print_wildcard("?") #1, 0
print_wildcard("100") #100
