class Rectangle:
  

  def __init__(self, w, h):
    self.width = w
    self.height = h

  def set_width(self, w):
    self.width = w

  def set_height(self, h):
    self.height = h

  def get_area(self):
    return (self.width * self.height)
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    line = ""
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    for i in range(self.height):
      line += f"{'*' * self.width}"
      line += '\n'
    return (line)

  def __str__(self):
    line = f"Rectangle(width={self.width}, height={self.height})"
    return line

  def get_amount_inside(self,object):
    nw = round(self.width / object.width)
    nh = round(self.height / object.height)
    return (nw * nh)




class Square(Rectangle):

  def __init__(self, l):
    self.width = l
    self.height = l

  def set_side(self, s):
    self.width = s
    self.height = s

  def __str__(self):
    line = f"Square(side={self.width})"
    return line


