#!/usr/bin/env python3
# -*- coding : utf-8 -*-




def readDt(self):
    l , dt = [],[]
    for path in self.local_paths:
        with open('timesteps.dat') as f:
            for line in f:
                if line.strip().startswith('poldt'):
                        l.append (line.strip().split('=')[-1])
            dt.append(l[-1])        
        return dt


def readDt():
    l = []
    with open('timesteps.dat') as f:
        for line in f:
            if line.strip().startswith('poldt'):
                l.append (line.strip().split('=')[-1])
    print(l[-1])        
            #print(l)
        #lines.split('=')

if __name__ == '__main__' :
    readDt()
    
