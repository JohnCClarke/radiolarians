
from numpy import *

n = 1000

pts = empty( ( n, 3 ) )

for i in range( pts.shape[ 0 ] ):
    pts[i,:]  = [ random.normal( 0.0, 1.0 ), random.normal( 0.0, 1.0 ), random.normal( 0.0, 1.0 ) ]
    pts[i,:] /= linalg.norm( pts[i,:] )

schedule = [ { 'iters':  60, 'step': 0.1   },
             { 'iters': 240, 'step': 0.01  },
             { 'iters': 240, 'step': 0.001 } ]

for epoch in schedule:
    for iter in range( epoch['iters'] ):
        minmin = 10.0 # radians - overall closest approach
        maxmin =  0.0 # radians - largest "closest approach"

        for i in range( pts.shape[ 0 ] ):
            dotmax  = -2.0
            jdotmax = pts.shape[ 0 ]
            for j in range( pts.shape[ 0 ] ):
                if ( i == j ):
                    continue
                dot = inner( pts[i,:], pts[j,:] )
                if ( dotmax < dot ):
                    dotmax  = dot;
                    jdotmax = j

            angle = math.acos( dotmax )
            if ( minmin > angle ):
                minmin = angle
            if ( maxmin < angle ):
                maxmin = angle
                
            pts[i,:] += epoch['step'] * ( pts[i,:] - pts[jdotmax,:] )
            pts[i,:] /= linalg.norm( pts[i,:] )

        print minmin, maxmin

for p in pts:
    print str( p )
