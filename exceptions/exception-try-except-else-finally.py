try:
#   x = 5 # b c
  x = '5' # a c
  x > 3
except:
  # just in case an Exception arises
  print("a")
else:
  # all went as planned, no except block was executed
  print("b")
finally:
  # will be executed all the time
  print("c")