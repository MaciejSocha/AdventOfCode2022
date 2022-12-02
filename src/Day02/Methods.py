def check_winning(line):
    match line[1]:
        case 'X':
            if line[0] == 'A':
                return 0
            else:
                if line[0] == 'B':
                    return -1
                else:
                    return 1
        case 'Y':
            if line[0] == 'B':
                return 0
            else:
                if line[0] == 'C':
                    return -1
                else:
                    return 1
        case 'Z':
            if line[0] == 'C':
                return 0
            else:
                if line[0] == 'A':
                    return -1
                else:
                    return 1
        case _:
            return None
