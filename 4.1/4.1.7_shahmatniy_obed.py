OFFSETS = [
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
]


def can_eat(current_pos, target_pos):
    for offset_x, offset_y in OFFSETS:
        if (current_pos[0] + offset_x, current_pos[1] + offset_y) == target_pos:
            return True

    return False


if __name__ == '__main__':
    main()
