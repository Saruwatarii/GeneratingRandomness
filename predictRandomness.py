import random

money = 1000
game = True
print("Please give AI some data to learn...")

while game:
    def __request_data():
        user_input = input()
        if user_input == "enough":
            print("Game over!")
            exit()
        return user_input

    def __filter_data(data):
        filtered = ''
        for symbol in data:
            if symbol in ['0', '1']:
                filtered += symbol
        return filtered


    def create_data(min_length):
        print("The current data length is 0, 100 symbols left")
        print('Print a random string containing 0 or 1:\n')
        data = __filter_data(__request_data())
        while len(data) < min_length:
            remaining = min_length - len(data)
            print(f'Current data length is {len(data)}, {remaining} symbols left')
            print('Print a random string containing 0 or 1:\n')
            data += __filter_data(__request_data())
        print('\nFinal data string:')
        print(data)
        data = ""
        print("\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.")
        print("""Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")
        return data

    def analyze_data(data):
        triads = [format(n, 'b').zfill(3) for n in range(8)]
        stats = {triad: [0, 0] for triad in triads}
        for triad in triads:
            for i in range(len(data) - 3):
                substring = data[i:i+3]
                if triad == substring:
                    next_symbol = data[i + 3]
                    if next_symbol == '0':
                        stats[triad][0] += 1
                    else:  # next_symbol == '1'
                        stats[triad][1] += 1
        return stats

    def create_test_data():
        print('\n\nPrint a random string containing 0 or 1:')
        test_data = __filter_data(__request_data())
        return test_data

    def guess_data(test_data, stats):
        prediction = []
        for _ in range(3):
            prediction.append(random.choice(['0', '1']))
        while len(prediction) < len(test_data):
            current_triad = test_data[len(prediction)-3:len(prediction)]
            if stats[current_triad][1] > stats[current_triad][0]:
                next_digit = '1'
            elif stats[current_triad][1] < stats[current_triad][0]:
                next_digit = '0'
            else:
                next_digit = random.choice(['0', '1'])
            prediction.append(next_digit)
        guessed_data = ''.join(prediction)
        print(f'prediction:\n{guessed_data}\n')
        return guessed_data

    def compare(test_data, prediction):
        assert len(test_data) == len(prediction)
        total = len(test_data) - 3
        total_guessed = 0
        for i in range(3, len(test_data)):
            if test_data[i] == prediction[i]:
                total_guessed += 1
        percentage = total_guessed / total * 100
        print(f'Computer guessed right {total_guessed} out of {total} symbols ({round(percentage, 2)} %)')
        print(f"Your capital is now ${money - total_guessed}\n")

    if __name__ == '__main__':
        data = create_data(100)
        stats = analyze_data(data)
        test_data = create_test_data()
        prediction = guess_data(test_data, stats)
        compare(test_data, prediction)