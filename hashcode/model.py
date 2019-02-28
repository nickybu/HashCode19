
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

class HorizontalSlide(object):

    def __init__(self, image):
        if image.orientation == "vertical":
            raise ValueError("HorizontalSlide only accepts a horizontal image")
        self.image = image

    @property
    def id(self):
        return "slide %d" % (self.image.id)

    @property
    def images(self):
        return [self.image]

    @property
    def tags(self):
        return self.image.tags

class VerticalSlide(object):

    def __init__(self, left_image, right_image):
        if (
                left_image.orientation == "horizontal"
                or right_image.orientation == "horizontal"):
            raise ValueError("VerticalSlide only accepts two vertical images")
        self.left_image = left_image
        self.right_image = right_image

    @property
    def id(self):
        return "slide %d - %d" % (self.left_image.id, self.right_image.id)

    @property
    def images(self):
        return [self.left_image, self.right_image]

    @property
    def tags(self):
        return list(set().union(
            self.left_image.tags,
            self.right_image.tags
        ))
