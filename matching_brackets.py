def is_matched(expression):
    # create a stack, if i see an open, push the correct closed to stack
    # if i see a closed, then pop stack to see if it matched
    bracket_list = []
    for bracket in list(expression):
        if bracket == '{':
            bracket_list.append('}')
        if bracket == '[':
            bracket_list.append(']')
        if bracket == '(':
            bracket_list.append(')')
        # it is a closed backet
        else:
            if bracket_list == []:
                return False
            check_bracket = bracket_list.pop()
            print bracket, check_bracket
            if bracket != check_bracket:
                return False
        print brakcet_list

    if len(bracket_list) == 0:
        return True
    return False
