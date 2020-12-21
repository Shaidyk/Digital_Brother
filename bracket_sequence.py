n = 2 * int(input('Enter positive integer: '))
bracket_sequence = ['(' for i in range(n // 2)] + [')' for i in range(n // 2)]


def generate_bracket_sequence(bracket_sequence, n):
    """ Print zero sequence """
    count_sequence = 1

    while True:
        index = n - 1
        counter = 0
        """ Find an open parenthesis that can be replaced """
        while index >= 0:
            if bracket_sequence[index] == ')':
                counter -= 1
            if bracket_sequence[index] == '(':
                counter += 1
            if counter < 0 and bracket_sequence[index] == '(':
                break
            index -= 1
        print(''.join(bracket_sequence))
        """ If there are no replacement brackets, we complete the algorithm """
        if index < 0:
            break

        """ Replace the bracket """
        bracket_sequence[index] = ')'

        """ Replace with the most lexicographic minimum """
        for i in range(index + 1, n):
            if i <= (n - index + counter) / 2 + index:
                bracket_sequence[i] = '('
            else:
                bracket_sequence[i] = ')'

        """ Count the number of sequences """
        count_sequence += 1
    print(f'Number of sequences: {count_sequence}')


generate_bracket_sequence(bracket_sequence, n)
