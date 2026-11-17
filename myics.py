from datetime import date,timedelta
today=date.today()
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "courses.csv"
WEEKDAY = {"周一": 0, "周二": 1, "周三": 2, "周四": 3, "周五": 4, "周六": 5, "周日": 6}
BYDAY = ["MO","TU","WE","TH","FR","SA","SU"]
with open(fname,encoding="utf-8") as f:
    next(f)
    total=[]
    for l in f :
        line=l.strip().split(",")
        course=line[0]
        day=line[1]
        con=line[2]
        target=WEEKDAY[day]
        delta=(target-today.weekday()+7)%7
        targetday=today+timedelta(days=delta)
        prefix=targetday.strftime("%Y%m%d")
        byday=BYDAY[WEEKDAY[day]]
        begin=prefix+"T"+line[3][:2]+line[3][3:5]+"00"
        end=prefix+"T"+line[4][:2]+line[4][3:5]+"00"
        location=line[5]
        eve="\n".join([
            "BEGIN:VEVENT",
            f"DTSTART;TZID=Asia/Shanghai:{begin}",
            f"DTEND;TZID=Asia/Shanghai:{end}",
            f"SUMMARY:{course}",
            f"LOCATION:{location}",
            f"RRULE:FREQ=WEEKLY;BYDAY={byday};UNTIL=20270115T235959Z",
            "END:VEVENT"
        ])
        total.append(eve)
with open(fname.replace(".csv",".ics"),"w",encoding="utf-8") as f:
    f.write("BEGIN:VCALENDAR\n"+"\n".join(total)+"\nEND:VCALENDAR\n")


