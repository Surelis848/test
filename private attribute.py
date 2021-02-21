class P:
   def __init__(self, name, alias):
      self.name = name       # public
      self._alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self._alias)

x = P(name='Alex', alias='amen')
x.who()