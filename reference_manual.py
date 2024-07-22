

from color_code import get_color_from_pair_number

def print_reference_manual():
    print("Color Code Reference Manual")
    print("---------------------------")
    for pair_number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        print(f"{pair_number:2}: {major_color:<6} - {minor_color:<6}")

if __name__ == '__main__':
    print_reference_manual()
