def leap_year( year):
    if( year % 4 == 0):
        if( year%100 == 0):
            if( year % 400 == 0):
                return "leap year"
            else:
                return "not a leap year"
        else:
            return "leap year"
    else:
        return "not a leap year"

print(leap_year(2001))
print(leap_year(4000))
print(leap_year(3000))
print(leap_year(2000))