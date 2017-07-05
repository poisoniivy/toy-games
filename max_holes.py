""" NEED TO REDO. """

def max_holes(num_holes, cafes):

    lemming_holes = range(0, num_holes)

    starting_hole = 0
    max_count = 0
    for cafe in cafes:
        diff = count_cafe_dist(lemming_holes[starting_hole:cafe-1])
        if diff > max_count
            max_count = diff


def count_cafe_dist(lemming_holes, food_hole):
    max_count = 0
    for hole in lemming_holes:
        difference = abs(hole - food_hole)
        if difference > max_count
            max_count = difference

    return max_count