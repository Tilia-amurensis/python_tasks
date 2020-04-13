
def check_box_a_to_b(a1, b1, c1, a2, b2, c2):
    if c1 <= c2:
        if a1 <= a2:
            if b1 <= b2:
                return True
    return False


def is_box_equal(a1, b1, c1, a2, b2, c2):
    if a1 == a2 and b1 == b2 and c1 == c2:
        return True


if __name__ == "__main__":
    a1 = int(input())
    b1 = int(input())
    c1 = int(input())
    a2 = int(input())
    b2 = int(input())
    c2 = int(input())
    if is_box_equal(a1, b1, c1, a2, b2, c2):
        print("Boxes are equal")
    elif is_box_equal(a1, c1, b1, a2, b2, c2):
        print("Boxes are equal")
    elif is_box_equal(b1, a1, c1, a2, b2, c2):
        print("Boxes are equal")
    elif is_box_equal(b1, c1, a1, a2, b2, c2):
        print("Boxes are equal")
    elif is_box_equal(c1, b1, a1, a2, b2, c2):
        print("Boxes are equal")
    elif is_box_equal(c1, a1, b1, a2, b2, c2):
        print("Boxes are equal")
    elif check_box_a_to_b(a1, b1, c1, a2, b2, c2):
        print("The first box is smaller than the second one")
    elif check_box_a_to_b(a1, c1, b1, a2, b2, c2):
        print("The first box is smaller than the second one")
    elif check_box_a_to_b(b1, a1, c1, a2, b2, c2):
        print("The first box is smaller than the second one")
    elif check_box_a_to_b(b1, c1, a1, a2, b2, c2):
        print("The first box is smaller than the second one")
    elif check_box_a_to_b(c1, a1, b1, a2, b2, c2):
        print("The first box is smaller than the second one")
    elif check_box_a_to_b(c1, b1, a1, a2, b2, c2):
        print("The first box is smaller than the second one")
    elif check_box_a_to_b(a2, b2, c2, a1, b1, c1):
        print("The first box is larger than the second one")
    elif check_box_a_to_b(a2, c2, b2, a1, b1, c1):
        print("The first box is larger than the second one")
    elif check_box_a_to_b(b2, a2, c2, a1, b1, c1):
        print("The first box is larger than the second one")
    elif check_box_a_to_b(b2, c2, a2, a1, b1, c1):
        print("The first box is larger than the second one")
    elif check_box_a_to_b(c2, b2, a2, a1, b1, c1):
        print("The first box is larger than the second one")
    elif check_box_a_to_b(c2, a2, b2, a1, b1, c1):
        print("The first box is larger than the second one")
    else:
        print("Boxes are incomparable")
