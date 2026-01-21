def printMonthTitle(year, month):
    width = 28
    month_name = getMonthName(month)

    line = TableModule.getLines(width, "-")
    title = TableModule.getTitle(width, str(year)+" "+month_name)

    print(line)
    pass
def getMonthName(month):
    month_name = ""
    if month==1:
        month_name = "Jan"
    elif month==2:
        month_name = "Feb"
    elif month==3:
        month_name = "March"
    #Add more months
    pass #Pass comment will make Python recognize that this is not an error
def printMonthBody(year, month):
    pass
def getStartDay(year, month):
    pass
def getTotalNumberofDays(year, month):
    pass
def isLeapYear(year):
    leap_year = False
    #add more implementation later
    return leap_year










