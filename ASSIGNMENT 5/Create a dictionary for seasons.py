seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Fall',
    10: 'Fall',
    11: 'Fall',
    12: 'Winter'
}

def get_season(month):
    return seasons.get(month, "Invalid month")

month_number = 5  
print(f"The season for month {month_number} is: {get_season(month_number)}")