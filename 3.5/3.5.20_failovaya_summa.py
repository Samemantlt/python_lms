import struct


def main():
    with open('numbers.num', 'rb') as file:
        bin_data = file.read()
    
    num_sum = 0
    for i in range(0, len(bin_data), 2):
        num = struct.unpack_from(">H", bin_data, i)
        num_sum += num[0]
    
    print(num_sum % 2 ** 16)


if __name__ == '__main__':
    main()
