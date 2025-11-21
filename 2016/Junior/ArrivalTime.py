import sys

line = sys.stdin.read()

hours, minutes = map(int, line.split(":"))

real_time_mins = hours * 60 + minutes
#print(hours, minutes)
#print(real_time_mins)

time_distance_left = 120 # in mins
final_time = 0

def time_format(mins):
    hours = int(mins / 60)
    mins = (mins % 60)
    
    # leading zero in time
    if hours < 10:
        hours = "0" + str(hours)
    if mins < 10:
        mins = "0" + str(mins)
    
    return f"{hours}:{mins}"


# rush hour is at 7-10, affecting leaving time of 5:20 to 9:40 (intervals of 20 mins)
if 320 <= real_time_mins <= 580:
    if real_time_mins < 420:  # leaving before rush hour
        real_time_travelled = 420 - real_time_mins
        
        real_time_mins += real_time_travelled
        time_distance_left -= real_time_travelled    # updated time left, 7 o'clock reached

        # RUSH HOUR REACHED
        time_distance_left *= 2
        if (time_distance_left + real_time_mins) < 600:
            final_time = time_distance_left + real_time_mins
            print(time_format(final_time))
        
        # Rush hour ends but still going; still have to update time tho
        else:
            real_time_mins = 600
            time_distance_left -= 180   # at ten o'clock
            
            # RUSH HOUR DONE
            time_distance_left /= 2
            real_time_mins += time_distance_left
            print(time_format(int(real_time_mins)))

    elif 420 <= real_time_mins:
        time_distance_left *= 2
        time_distance_left -= (600 - real_time_mins)
        real_time_mins = 600    # at ten o'clock
       
        # RUSH HOUR DONE
        time_distance_left /= 2
        real_time_mins += time_distance_left
        print(time_format(int(real_time_mins)))


# rush hour is also at 15-19, affecting leaving time of 13:20 to 18:40 (interval 20 mins).
elif 800 <= real_time_mins <= 1120:
    if real_time_mins < 900:  # leaving before rush hour
        real_time_travelled = 900 - real_time_mins
        
        real_time_mins += real_time_travelled
        time_distance_left -= real_time_travelled    # updated time left, 15 o'clock reached

        # RUSH HOUR REACHED
        time_distance_left *= 2
        if (time_distance_left + real_time_mins) < 1140:
            final_time = time_distance_left + real_time_mins
            print(time_format(final_time))
        
        # Rush hour ends but still going; still have to update time tho
        else:
            real_time_mins = 900
            time_distance_left -= 240   # at 15 o'clock
            
            # RUSH HOUR DONE
            time_distance_left /= 2
            real_time_mins += time_distance_left
            print(time_format(int(real_time_mins)))

    elif 900 <= real_time_mins:
        time_distance_left *= 2
        time_distance_left -= (1140 - real_time_mins)
        real_time_mins = 1140    # at 19 o'clock
       
        # RUSH HOUR DONE
        time_distance_left /= 2
        real_time_mins += time_distance_left
        print(time_format(int(real_time_mins)))


else:
    real_time_mins += 120
    if real_time_mins >= 1440:
        real_time_mins -= 1440
    print(time_format(real_time_mins))