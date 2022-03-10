from pandas import notnull
from sqlalchemy import null
from Day import Day

class Week:
    def __init__(self):
        self.days =  {
        "Monday":Day("Monday"),"Tuesday":Day("Tuesday"),"Wednesday":Day("Wednesday"),"Thursday":Day("Thursday"),
        "Friday":Day("Friday"),"Saturday":Day("Saturday"),"Sunday":Day("Sunday")
        }

    
    
        
    
    