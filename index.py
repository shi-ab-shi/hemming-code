def read_binary_sequence(file_name):
    with open(file_name, 'r') as file:
        binary_sequence = file.read().strip()
    return binary_sequence

def write_binary_sequence(file_name, binary_sequence):
    with open(file_name, 'w') as file:
        file.write(binary_sequence)

def generate_parity_bits(data):
    parity_bits = ''
    for i in range(9):
        parity = 0
        for j in range(len(data)):
            if (j + 1) & (2 ** i) != 0:
                parity ^= int(data[j])
        parity_bits += str(parity)
    return parity_bits

def add_parity_bits(data):
    parity_bits = generate_parity_bits(data)
    return data + parity_bits

def check_and_correct_errors(recieved_data):
    error_bit = 0
    for i in range(9):
        parity = 0
        for j in range(len(recieved_data)):
            if (j + 1) & (2 ** i) != 0:
                parity ^= int(recieved_data[j])
        if parity != 0:
            error_bit += 2 ** i

    if error_bit != 0:
        recieved_data = list(recieved_data)
        recieved_data[error_bit - 1] = str(1 - int(recieved_data[error_bit - 1]))
        recieved_data = ''.join(recieved_data)
    return recieved_data, error_bit


def main():
    input_sequence = read_binary_sequence('input1_test.txt')
    output_sequence = add_parity_bits(input_sequence)
    write_binary_sequence('output1_test.txt', output_sequence)
    recieved_sequence = read_binary_sequence('test/recieved.txt')
    corrected_sequence, error_position = check_and_correct_errors(recieved_sequence)
    if error_position != 0:
        print(f"Исправлена ошибка в бите {error_position}")
        write_binary_sequence('output.txt', corrected_sequence)
        print("Исправленная последовательность записана в output.txt")
    else:
        print("Последовательность не содержит ошибок")

main()
