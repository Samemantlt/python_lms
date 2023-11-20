def to_string(*values, sep=" ", end="\n"):
    return sep.join(map(str, values)) + end


if __name__ == '__main__':
    main()
