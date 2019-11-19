#Skardin- NAGRA STRESS TEST TOOL V1.0
#Sri - 20191119
#It will keep transmit the IRD command based on test requirments
#USAGE : python tivusat_stresstest.py < Number_of_loops> <DelayBetweenEachTransmit> < channelchmode>
#        ex python tivusat_stresstest.py 10 5 chup ( it will send the IR CHANNEL UP every 5 secs for 10 times)
#        3 modes of channel change
#        chupdown- it will send the CH UP first and wait for given time and send the CH DOWN and wait for given second
#        chup- it will send the CH UP first and wait for given time
#        chdown- it will send the CH DOWN first and wait for given time
import sys,time,os

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

numberofArguments = len(sys.argv)
if numberofArguments < 4:
    print "ERROR INVALID MODE"
    print "#USAGE : python tivusat_stresstest.py < Number_of_loops> <DelayBetweenEachTransmit> < channelchmode>"
    print " ex python tivusat_stresstest.py 10 5 chup ( it will send the IR CHANNEL UP every 5 secs for 10 times)"
    print " 3 modes of channel change"
    print " chupdown- it will send the CH UP first and wait for given time and send the CH DOWN and wait for given second"
    print " chup- it will send the CH UP first and wait for given time"
    print " chdown- it will send the CH DOWN first and wait for given time "
    exit -2

numberofLoops = int(sys.argv[1])
delayinSecs = float (sys.argv[2])
mode = (sys.argv[3])
i = 0
while 1:
    if(i < numberofLoops):
        os.system("date")
        print i
        i = i+1
        if mode == "chupdown":
            os.system("irsend SEND_ONCE sehs1907_rcu KEY_UP")
            time.sleep(delayinSecs)
            os.system("irsend SEND_ONCE sehs1907_rcu KEY_DOWN")
            time.sleep(delayinSecs)
        elif mode == "chdown":
            os.system("irsend SEND_ONCE sehs1907_rcu KEY_DOWN")
            time.sleep(delayinSecs)
        elif mode == "chup":
            os.system("irsend SEND_ONCE sehs1907_rcu KEY_UP")
            time.sleep(delayinSecs)
        else:
            print "ERROR INVALID MODE"
    else:
        break;
