def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative") # for negative numbers
    return base * height * 0.5