print "Military Time Converter."
print "Required format: '12:40:22AM'"
print "Type in time and press Enter:"

time = input().strip()

def time_conversion(time):
    if 'AM' in time and time[:2] == '12':
        print '00' + time[2:-2]
    elif 'PM' in time and time[:2] == '12':
        print time[:-2]
    elif 'AM' in time:
        print time[:-2]
    elif 'PM' in time:
        print str(int(time[:2]) + 12) + time[2:-2]
    else:
        print time

time_conversion(time)
