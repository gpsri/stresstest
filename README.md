# stresstest
Nagra Stress Test IR Blaster
#Skardin- NAGRA STRESS TEST TOOL V1.0
#Sri - 20191119
#It will keep transmit the IRD command based on test requirments
#USAGE : python tivusat_stresstest.py < Number_of_loops> <DelayBetweenEachTransmit> < channelchmode>
#        ex python tivusat_stresstest.py 10 5 chup ( it will send the IR CHANNEL UP every 5 secs for 10 times)
#        3 modes of channel change
#        chupdown- it will send the CH UP first and wait for given time and send the CH DOWN and wait for given second
#        chup- it will send the CH UP first and wait for given time
#        chdown- it will send the CH DOWN first and wait for given time
