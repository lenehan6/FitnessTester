from FitnessTester import *
import IODevices


jobs = [];

server = IODevices.Server( jobs );
server.start();


while True:
    if ( len(jobs) > 0 ):
        job = jobs.pop(0);
        print job;

