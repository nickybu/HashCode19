
class Image(object):

    def __init__(self,
            orientation,
            tags):
        if orientation == "H":
            self.orientation = "horizontal"
        elif orientation == "V":
            self.orientation = "vertical"
        else:
            pass

        self.tags = tags

