weeks_in_year = 52
ages_expected = 90

def life_in_week(ages):
    years_left = ages_expected - ages
    weeks_left = years_left * weeks_in_year
    print(f"You have {weeks_left} weeks left.")
    
ages_input = input("How old are you? ")

life_in_week(int(ages_input))