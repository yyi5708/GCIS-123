def square(length):
    if length < 0:
        return None
    else:
        area = length * length
        return area

def rectangle(width, height):
    if width and height < 0:
        return None
    else:
        area = width * height
        return area
    
def triangle(base, height):
    if base and height < 0:
        return None
    else:
        area = 0.5 * base * height
        return area