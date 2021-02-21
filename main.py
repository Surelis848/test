class Colour:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    # END _ _init_ _

    def set_name(self, name):
        if name == "":
            raise Exception("That is a blank value")
        else:
             self._name = name
        #ENDIF;
    # END set_name

    def get_name(self):
        if self._name == "":
            return "There is a blank value"
        else:
            return self._name
        # ENDIF;
    # END get_name
    name = property(get_name, set_name)
# END class.

redcolour = Colour("#FF0000", "Red")
print(redcolour._name)
print(redcolour.get_name())
redcolour.name = "Red"
print(redcolour._name)
print(redcolour.get_name())
redcolour.set_name("Red")
print(redcolour._name)
print(redcolour.get_name())
redcolour.name = ""
print(redcolour._name)
print(redcolour.get_name())
redcolour.set_name("")
print(redcolour._name)
print(redcolour.get_name())


