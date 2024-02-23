
#Ask player if they want to play
playing = input("Do you want to know your zodiac sign?     ")

if playing.lower() == "yes":  # Case-insensitive comparison
    print("Great, lets calculate it!")

    # Ask for birth month and convert to lowercase
    birth_month = input("What month were you born?: ").lower()

    # Validate birth month
    valid_months = ["january", "february", "march", "april", "may", "june",
                    "july", "august", "september", "october", "november", "december"]
    if birth_month not in valid_months:
        print("Invalid month entered. Please try again.")
        

    # Convert birth month to number
    month_conversion = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }
    birth_month_num = month_conversion[birth_month]

    # Ask for birth date and validate
    birth_date = int(input("What numerical day were you born?:   "))
    if birth_date <= 0 or birth_date > 31:
        print("Invalid birthday, please try again.")
        

    # Calculate zodiac sign
    zodiacs = {
        "Capricorn": ((12, 22), (1, 19)),
        "Aquarius": ((1, 20), (2, 18)),
        "Pisces": ((2, 19), (3, 20)),
        "Aries": ((3, 21), (4, 19)),
        "Taurus": ((4, 20), (5, 20)),
        "Gemini": ((5, 21), (6, 20)),
        "Cancer": ((6, 21), (7, 22)),
        "Leo": ((7, 23), (8, 22)),
        "Virgo": ((8, 23), (9, 22)),
        "Libra": ((9, 23), (10, 22)),
        "Scorpio": ((10, 23), (11, 21)),
        "Sagittarius": ((11, 22), (12, 21)),
    }
#calculate their sign based on the
    for sign, ((start_month, start_day), (end_month, end_day)) in zodiacs.items():
        if ((birth_month_num == start_month and birth_date >= start_day) or
            (birth_month_num == end_month and birth_date <= end_day) or
            (start_month < end_month and birth_month_num in range(start_month, end_month))):
            print(f"Cute, you're a {sign}!")
            break  
    else:
        print("Birthday falls outside any zodiac sign range.")

    #Fun facts for each sign
    #facts= {
        #"Cap_fact": ("Capricorns are known for being the hardest workers of the zodiac."),
       # "Aqua_fact": ("Aquarians are actually an air sign, not a water sign!"),
       # "Pisces_fact": ("Pisces are a mutable sign, and are known to be very spirtual and in tune with their emotions"),
       # "Aries_fact": ("Aries are thought to be the wild, firey sign of the zodiac, and have a hot temper!"),
       # "Taurus_fact": ("Taruses are known to be home bodies, and love a good night in"),
       # "Gemini_fact": ("Gemini's are one of the smartest signs in the zodiac, and are jacks of all trades"),
       # "Cancer_fact": 
   # }

    #fun_fact=input("Do you want to know a fun fact about your sign?   ")
    #for sign in facts.items():
    # if fun_fact.lower() == "yes":
    #    print(f"{sign}")
else:
    print("Ok, have a good day!")
