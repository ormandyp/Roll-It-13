
# checks that users enter an integer
# that is more than 13

def int_check():

    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input("enter an integer:  "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
target_score = int_check()
print(target_score)

# 8 0.29