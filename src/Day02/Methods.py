def check_winning(line):
    match line[1]:
        case 'X':
            if line[0] == 'A':
                return 3
            else:
                if line[0] == 'B':
                    return 1
                else:
                    return 2
        case 'Y':
            if line[0] == 'B':
                return 2
            else:
                if line[0] == 'C':
                    return 3
                else:
                    return 1
        case 'Z':
            if line[0] == 'C':
                return 1
            else:
                if line[0] == 'A':
                    return 2
                else:
                    return 3
        case _:
            return None


def give_points(shape):
    match shape:
        case 'X':
            return 0
        case 'Y':
            return 3
        case 'Z':
            return 6
        case _:
            return None
