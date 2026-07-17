months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        if "/" in date:
            try:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if month>12 or day>31 or year<0:
                    continue
                print(f"{year}-{month:02}-{day:02}")
                break
            except ValueError:
                pass

        elif "," in date:
            try:
                day, year = date.split(",")
                year = int(year)
                for month in range(len(months)):
                    if months[month] in day:
                        day=int(day.replace(months[month],""))
                        month = month+1
                        break
                if month>12 or day>31 or year<0:
                    continue
                print(f"{year}-{month:02}-{day:02}")
                break
            except ValueError:
                pass
    except ValueError:
        pass

