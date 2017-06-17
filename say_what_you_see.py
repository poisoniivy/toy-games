def  say_what_you_see(input_strings):

    spoken_string_list = []
    for number in input_strings:

        spoken_string = ""
        previous_num = number[0]
        num_count = 0
        
        i = 0
        while i <= len(number) - 1:

            if number[i] == previous_num and i != len(number):
                num_count += 1
                i += 1
            else:
                spoken_string += str(num_count) + str(previous_num)
                previous_num = number[i]
                num_count = 1
                i += 1

        spoken_string += str(num_count) + str(previous_num)

        print spoken_string