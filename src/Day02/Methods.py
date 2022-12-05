def check_winning(line):
    match line[1]:
        case 'X':
            if line[0] == 'A':
                return 3
            else:
                if line[0] == 'B':
                    return 0
                else:
                    return 6
        case 'Y':
            if line[0] == 'B':
                return 3
            else:
                if line[0] == 'C':
                    return 0
                else:
                    return 6
        case 'Z':
            if line[0] == 'C':
                return 3
            else:
                if line[0] == 'A':
                    return 0
                else:
                    return 6
        case _:
            return None


def give_points(shape):
    match shape:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            return None
