# Extra Credit 1
# Lucas Greenwood

# print list of available films
print("""
Available movies today:
A)12 Strong:	1)2:30	2)4:40	3)7:50	4)10:50
B)Coco:		    1)12:40	2)3:45
C)The Post:	    1)12:45	2)3:35	3)7:05	4)9:55
""")

# create dictionary for movie times
movie_times = {
    'A': ['2:30', '4:40', '7:50', '10:50'],
    'B': ['12:40', '3:45'],
    'C': ['12:45', '3:35', '7:05', '9:55'],
}

# define error message to print on invalid inputs
error_msg = "Invalid option; please restart app..."

# prompt movie choice
movie_choice = input("Movie choice: 	").upper()  # force input character to uppercase

# condition to exit program
if movie_choice not in ['A', 'B', 'C']:
    print(error_msg)
else:
    # prompt showtime choice
    showtime = int(input("Showtime: 	"))     # categorical variable (1-4)

    # condition to exit program
    if showtime not in range(1, len(movie_times[movie_choice])+1):
        print(error_msg)
    else:
        # convert selection to valid showtime (string)
        actual_showtime = movie_times[movie_choice][showtime - 1]
        # prompt adult ticket selection
        ticket_adult = int(input("Adult tickets: 	"))     # cast number of tickets to integer
        # exit conditional
        if ticket_adult > 30:
            print(error_msg)
        else:
            # prompt child ticket selection
            ticket_kid = int(input("Kid tickets: 	"))     # cast to integer
            if ticket_adult + ticket_kid > 30:
                print(error_msg)
            else:
                # Determine if the movie is before or after 2
                # and set prices accordingly
                if actual_showtime in ['12:40', '12:45']:
                    price_adult = 11.17
                    price_kid = 8
                else:
                    price_adult = 12.45
                    price_kid = 9.68
                # calculate total cost for user & print
                cost = ticket_adult * price_adult + ticket_kid * price_kid
                print(f"Total cost: 	${cost:.2f}")       # round to two decimal places
