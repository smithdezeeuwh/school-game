
valid = False
while not valid:
    error = ("whoops! please enter a correctly formated input")

    try:
        intcheck_response = input("{} please enter how many troops you would like to send to point {}:")
        # makes 1 into 00001
        intcheck_response_len = len(str(intcheck_response))
        print(intcheck_response_len)
        print(intcheck_response)
        if intcheck_response_len == 5:
            print(intcheck_response)
        else:
            print(error)
            print()

    except ValueError:
        print(error)
