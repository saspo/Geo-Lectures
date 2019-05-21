# Lecture 5: Snuffler exercise functions 
# 
# author: Eva Eibl eva.eibl@uni-potsdam.de
# SS 2019: Module MGPW02
# 16.5.2019
# -----------------------------
import Lec5_geyserEx_functions as h
import matplotlib.pyplot as plt
import numpy as np


# -- import the snuffler marker file, time in julian days --
julday, evclass = h.read_snuffler_marker("marker_1605.txt", length=0) #Funktion in extra file
								      # mit h. aufrufen
julday = np.sort(julday) #da Marker nicht zeitlich sortiert sind
plt.plot(julday)
plt.show()




# -- calculate the waiting time after eruption/ duration of bursts in minutes --  

#julian day variable
#calculate the time between two julianday variables 

wait_time = [] 

for i in range (0,len((julday)),1):	
    #wait_time = np.zeros(julday) #error
	wait_time.append(julday[i+1]-julday[i]*24*60) #append function

#or 
#wait_time = np.diff(julday)*24*60

plt.plot(wait_time)
plt.show()

# -- calculate mean time --

mean_wait_time = np.mean(wait_time)

# -- plot waiting time after eruptions/ duration of bursts vs. time --
plt.plot(jul_day, wait_time)
plt.show()


# -- plot histogram of the intereruption times (1 h bins) -- 

plt.hist(wait_time)













