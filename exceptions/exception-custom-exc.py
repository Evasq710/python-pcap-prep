class MyEx(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg+msg)
    print(self.args)
    self.args = (msg,)
    print(self.args)
 
try:
  raise MyEx('wrong!')
except Exception as e:
  print(e)


class MyEx(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg+msg)
 
try:
  raise MyEx('wrong!')
except Exception as e:
  print(e)