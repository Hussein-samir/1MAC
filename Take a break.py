import webbrowser
import time

break_count = 3
breaks_taken = 0
break_duration = 2 #in seconds
print "This program started on" + time.ctime()
while breaks_taken<break_count:
    time.sleep(break_duration)
    webbrowser.open("https://www.youtube.com/watch?v=rvjQ5Y6a2Ys&index=156&list=PLNi9aJHhlWMiWTSJWuKvJ-gSIOEO_Qfbt")
    breaks_taken += 1