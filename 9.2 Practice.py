#Practice 9.2

#A program includes the days of the week then prompts the user for a number 0-6
#Then outputs the day of the week assosiated

#get User Input and verify
def inputverify():
    usernum = int(input("Input a number of the week (0-6): "))
    if usernum < 0 or usernum > 6:
        return usernum, False
    else:
        return usernum, True


weekdays = [ "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" ]
inputday, verify = inputverify()

if verify == False:
    print("Error: Please only input a int between 0-6")
else:
    print(inputday, "=", weekdays[inputday])
