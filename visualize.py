import matplotlib.pyplot as plt

def readfile(filename):
    compars = {'Selection sort': [], 'Insertion sort': [], 'Shellsort': [], 'Merge sort': []}
    times = {'Selection sort': [], 'Insertion sort': [], 'Shellsort': [], 'Merge sort': []}
    with open(filename, 'r', encoding='utf-8') as f:
        f.readline()
        i = 2
        for line in f:
            info = line.strip().split(', ')
            if (i + 2) % 4 == 0:
                alg = 'Selection sort'
            elif (i + 2) % 4 == 1:
                alg = 'Insertion sort'
            elif (i + 2) % 4 == 2:
                alg = 'Shellsort'
            else:
                alg = 'Merge sort'
            compars[alg].append(int(info[2]))
            times[alg].append(float(info[3]))
            i += 1
    return compars, times


def draw_graph(data, name, gr_label):
    title = f'Algorithms for array with {name}'.lower().capitalize()
    plt.title(title)
    x = list(range(7, 16))
    y_sel = data['Selection sort']
    y_ins = data['Insertion sort']
    y_shell = data['Shellsort']
    y_merge = data['Merge sort']
    plt.plot(x, y_sel, label = "Selection sort")
    plt.plot(x, y_ins, label = "Insertion sort")
    plt.plot(x, y_shell, label = "Shellsort")
    plt.plot(x, y_merge, label = "Merge sort")

    plt.ylabel(gr_label)
    plt.xlabel('Logariphmic size of array')
    plt.legend()
    
    plt.yscale("log")
    plt.savefig(gr_label + ' ' + name)
    plt.clf()


def main():
    filenames = ('Random numbers1.csv', 'Sorted numbers1.csv', 'Reversed sorted numbers1.csv', 'Numbers 1-31.csv')
    for f in filenames:
        compars, times = readfile(f)
        name = f[:-5]
        draw_graph(compars, name, 'Number of comparisons')
        draw_graph(times, name, 'Working time of algorithm, seconds')

main()
