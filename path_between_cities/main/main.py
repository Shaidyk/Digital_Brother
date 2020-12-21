from path_between_cities.matrix import Matrix

"""Number of tests"""
while True:
    try:
        number_of_tests = int(input())
        if number_of_tests <= 0:
            raise ValueError
        break
    except:
        print("Incorrect input, try again")

""""Number of cities"""
while True:
    try:
        number_of_cities = int(input())
        if number_of_cities <= 0:
           raise ValueError
        break
    except:
        print("Incorrect input, try again")

matrix = Matrix(number_of_cities)
current_city_number = 0
city_names = [number_of_cities]

"""Add city names and costs"""
for test in range(number_of_tests):
    for i in range(number_of_cities):
        while True:
            try:
                name = input()
                city_names.append(name)
                p = int(input())
                if p >= number_of_cities:
                    raise ValueError
                break
            except:
                print("Incorrect input, try again")
        for j in range(p):
            while True:
                try:
                    cost = input().split(' ')
                    next_city_number = int(cost[0]) - 1
                    transport_cost = int(cost[1])
                    if (next_city_number == current_city_number
                            or next_city_number < 0
                            or transport_cost < 1):
                        raise ValueError
                    matrix[current_city_number][next_city_number] = transport_cost
                    break
                except:
                    print("Incorrect input, try again")
        current_city_number += 1

    """Start floyd's algorithm"""
    matrix.floyd()

    """Path finding"""
    while True:
        try:
            number_of_test_travels = int(input())
            if number_of_test_travels <= 0:
                raise ValueError
            break
        except:
            print("Incorrect input, try again")
    for i in range(number_of_test_travels):
        while True:
            cost_btw_cities = input().split(' ')
            try:
                start_city = int(city_names.index(cost_btw_cities[0])) - 1
                end_city = int(city_names.index(cost_btw_cities[1])) - 1
                break
            except:
                print("Input correct name of cities!")

        print(matrix[start_city][end_city])


