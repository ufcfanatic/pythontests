
import itertools

'''
#0 : ['a', 'b']
#1 : ['+', '-']
#2 : ['0', '1', '2', 'w',…..]
  
'a+1'  good
'b-2'  good 
'a+'   X
'a+11' X   
'+a1'  X

[
	['a, 'b'],
  ['+', '-'], 
  ['0', '1', , '2', '3'], 
  ...
]

'''

def generate():

 l = [['a', 'b' ] , ['+', '-'] , ['0' , '1' , '2']]
 return list(itertools.product(*l))

res = generate()
print (' res ' , res)

#[ [ a , + , 0 ] [ b , - , 1] [b , - , 2 ] [ b , + , 0 ] [
      
