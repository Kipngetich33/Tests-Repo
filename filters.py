def mean_filter(data, width=3):
    if width < 1:
        print("width is positive")
        return []
    elif width % 2 != 1:
        print("width is odd")
        return []

    start = width // 2
    filtered = []
    for i in range(start,len(data)-start):
        sum = 0
        for d in data[i-start:i+start+1]:
            sum += d
        datum = sum / width
        filtered.append(datum)
    return filtered

def median_filter(data, width=3):
    if width < 1:
        print("width is positive")
        return []
    elif width % 2 != 1:
        print("width is odd")
        return []

    start = width // 2
    filtered = []
    for i in range(start,len(data)-start):
        ls = sorted(data[i-start:i+start+1])
        filtered.append(ls[start])
    return filtered

if __name__ == '__main__':
    from sensor import *

    data = generate_sensor_data()
    print_sensor_data(data, 'raw')

    filtered_data = mean_filter(data)
    print_sensor_data(filtered_data, 'filtered_mean_3')

    filtered_data = mean_filter(data, 5)
    print_sensor_data(filtered_data, 'filtered_mean_5')

    filtered_data = median_filter(data, 5)
    print_sensor_data(filtered_data, 'filtered_median_5')
