import socket
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
#print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
data = 'llll DATA: 0,4.4,-4.3,0,0,6.8,-7,0,0,1.6,-1.6,0,0,6.3,-6.4,0'

while True:

    #data, address = sock.recvfrom(4096)
    if ('DATA:' not in data):
        continue
    else:
        #data = data.decode
        start = data.find("DATA:")
        substring = data[start+5:]
        vect = [x.strip() for x in substring.split(',')]
        print (vect)
        vect = [float(numeric_string) for numeric_string in vect]

        #p = plt.plot(x,vect)
        #plt.show(p)
        xnew = np.linspace(1,16,200)

        power_smooth = spline(range(1,17),vect,xnew)

        plt.plot(xnew,power_smooth)
        font = {'family': 'serif',
                'color': 'black',
                'weight': 'normal',
                'size': 14,
                }
        plt.scatter(range(1,17), vect)
        plt.grid(axis='y')
        plt.xlabel('Time (sec)', fontdict=font)
        plt.ylabel('Amplitude', fontdict=font)
        plt.show()
        break