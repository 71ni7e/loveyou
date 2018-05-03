import subprocess
import sys
import time
import click #working on getting rid of this one, soon^tm


def firstCheck():
    if len(sys.argv) < 2 and len(sys.argv) < 3:
        print("No arguments given, correct syntax: ./loveyou.py [New MAC] [Interface]")
        sys.exit()
    elif len(sys.argv) < 2:
        print("No MAC address provided")
        sys.exit()
    elif len(sys.argv) < 3:
        print("No Interface specified")
        sys.exit()
    else:
        readStateZero()
        return



def readStateZero():

    #Find the current MAC address
    command = "awk 'NR==1' /sys/class/net/*/address"
    mainVal = subprocess.Popen (command, stdout=subprocess.PIPE, shell=True)
    mainVal.wait()
    stdOutIn = mainVal.communicate()

    #Do some string manipulation so we can end up with the correctly formatted answer
    currentMAC = stdOutIn[:1]
    currentMAC2 = str(currentMAC)
    global currentMAC3
    currentMAC3 = currentMAC2[3:20]
    print('Current Address: ' + currentMAC3)
    secondCheck()
    return



def secondCheck():
    #"Force" the user to check his input so he doesn't screw up.
    if click.confirm('Is ' + sys.argv[1] + ' the correct new mac addr?', default=True) and click.confirm('Is ' + sys.argv[2] + ' the correct interface?', default=True):
        print('Got answer [Y]es, going forward.')
        changeAddr()
    else:
            sys.exit()
    return

def changeAddr():
    #Let the user know what is happening
    print('Changing MAC address from ' + currentMAC3 + ' to ' + sys.argv[1] + ' on interface ' + sys.argv[2])

    #Define command sequence
    command1 = ('ifconfig ' + sys.argv[2] + ' down')
    command2 = ('ifconfig ' + sys.argv[2] + ' hw ether ' + sys.argv[1])
    command3 = ('ifconfig ' + sys.argv[2] + ' up')

    #Run the command, notice that we run command3 two times as a placeholder since it wouldn't
    #work all the time, still working on that.
    returnValue = subprocess.Popen(command1, shell=True)
    returnValue.wait()
    returnValue2 = subprocess.Popen(command2, shell=True)
    returnValue2.wait()
    returnValue3=subprocess.Popen(command3, shell=True)
    returnValue.wait()
    returnValue4=subprocess.Popen(command3, shell=True)
    returnValue.wait()
    return

firstCheck();
