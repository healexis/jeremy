#!/usr/bin/python
import pdb
# pdb.set_trace()

# *History[ *Index ] = arr
arrHistory = {}
newArrHistory = {}

def deepcopy( arr, arrIndex="-1," ):
   if type( arr ) is not list:
      return arr

   for ( arrHistoryIndex, arrHistoryElement ) in arrHistory.items():
      if arr == arrHistoryElement:
         # We have a loop!
         return newArrHistory[ arrHistoryIndex ]

   # Need to remember the pointer to the list as well.
   currArrIndex = -1
   currArrIndexStr = arrIndex + str( currArrIndex ) + ","
   newArr = []
   arrHistory[ currArrIndexStr ] = arr
   newArrHistory[ currArrIndexStr ] = newArr
   currArrIndex += 1

   for arrElement in arr:
      currArrIndexStr = arrIndex + str( currArrIndex ) + ","
      arrHistory[ currArrIndexStr ] = arrElement
      newArrElement = deepcopy( arrElement )
      newArrHistory[ currArrIndexStr ] = newArrElement
      newArr.append( newArrElement )
      currArrIndex += 1

   return newArr

"""
arr = []
arr.append( arr )
pdb.set_trace()
b = deepcopy( arr ) #<<<
print arr
print b
"""
