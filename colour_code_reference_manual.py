from color_code_Pairing import get_color_from_pair_number, color_pair_to_string, MAJOR_COLORS, MINOR_COLORS

def generate_reference_manual():
    reference_manual = []
    reference_manual.append("Color Code Reference Manual\n")
    reference_manual.append("----------------------------\n")
    for i in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        color_pair = get_color_from_pair_number(i)
        color_pair_names = color_pair_to_string(color_pair)
        line = f"{i}: {color_pair_names}\n"
        reference_manual.append(line)
    return ''.join(reference_manual)

if __name__ == '__main__':
    manual = generate_reference_manual()
    print(manual)
