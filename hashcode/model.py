
class Image(object):

    def __init__(self,
            _id,
            orientation,
            tags):
        if orientation == "H":
            self.orientation = "horizontal"
        elif orientation == "V":
            self.orientation = "vertical"
        else:
            pass

        self.id = _id
        self.tags = tags

