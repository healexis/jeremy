#!/usr/bin/python
import pdb

# Deepcopy.

def deepcopy( arr ):

   # Keep a history of all the elements we've seen so far, so we can
   # compare them with the current element to check for loops.
   # history[ id ] = newArr
   history = {}

   def _deepcopy( arr ):
      if type( arr ) is not list:
         return arr

      if id( arr ) in history:
         return history[ id( arr ) ]

      newArr = []
      history[ id( arr ) ] = newArr
      for element in arr:
         newElement = _deepcopy( element )
         newArr.append( newElement )

      return newArr

   return _deepcopy( arr )

class DeepCopyTestCase( object ):
   def __init__( self, arr=[] ):
      self.arr = arr

   def run( self ):
      #pdb.set_trace()
      self.newArr = deepcopy( self.arr )

   def check( self ):
      print "arr:", self.arr
      print "newArr:", self.newArr
      self.arr.append( 3 )
      self.newArr.append( 5 )
      assert 3 in self.arr
      assert 3 not in self.newArr
      assert 5 not in self.arr
      assert 5 in self.newArr
      print "pass"

if __name__ == "__main__":
   # Sanity test cases.
   tests = [
      [],
      range( 10, 20 ),
      ]

   # Test with loop.
   arr = []
   arr.append( arr )
   tests.append( arr )

   # Test with loop at 3rd level.
   arr = []
   arr.append( [] )
   arr.append( 1 )
   arr[ 0 ].append( arr )
   arr[ 0 ].append( 2 )
   tests.append( arr )

   # Test loops between siblings in same level.
   arr = []
   arr.append( [ 1 ] )
   arr.append( [ 2 ] )
   arr[ 0 ].append( arr[ 1 ] )
   arr[ 1 ].append( arr[ 0 ] )
   arr[ 1 ].append( arr )
   tests.append( arr )

   for arr in tests:
      testcase = DeepCopyTestCase( arr )
      testcase.run()
      testcase.check()

