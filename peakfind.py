# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 17:21:18 2014
Peak Finding Algorithm for 2-d mtxrix objects

Method:
    - pick a middle column j = m/2
    - find global maximum of col j at (i,j)
    - compare (i,j-i), (i,j), (i,j+1)
        - pick left cols if (i,j-1) > (i,j)
        - pick right cols if (i,j+1) > (i,j)
        IF neither are true, then (i,j) is a peak
    - slice by into the half that contains the greater value
        - pick a new middle column, find its maximum
        - compare left and right values again
    - repeat until there are only two columns
        - find max
        - compare left and right 
        - greater one is the peak


@author: tenz
"""

# make a 2-d mtxrix
matrix = [            # i,j
      [2,6,5,4,5], # 0,j
      [3,4,3,6,5], # 1,j
      [4,6,3,5,4], # 2,j
      [5,6,4,3,6], # 3,j
      [6,3,5,3,7]  # 4,j
      ]

def peakfind(mtx):
    ncols = len(mtx[0])
    nrows = len(mtx)
    
    # find middle column and it's maximum
    mid = [mtx[i][ncols/2] for i in range(nrows)]
    max_ind = mid.index(max(mid))
    
    center = mtx[max_ind][ncols/2]
    
    if len(mtx[0]) > 2:
        if mtx[max_ind][ncols/2 -1] > center or mtx[max_ind][ncols/2 + 1] > center:
            if mtx[max_ind][ncols/2-1] > mtx[max_ind][ncols/2+1]:
                # slice only the left side
                mtx = [mtx[i][:ncols/2] for i in range(nrows)]
                return peakfind(mtx)
            else:
                mtx = [mtx[i][ncols/2+1:] for i in range(nrows)]
                return peakfind(mtx)
        else:
            return center
    else:
        if mtx[max_ind][ncols/2-1] > mtx[max_ind][ncols/2]:
            return mtx[max_ind][0]
        else:
            return mtx[max_ind][1]
    
    