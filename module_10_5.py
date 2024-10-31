import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            strс = file.readline()
            if strс == '':
                break
            all_data.append(strс)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_start = datetime.now()
for file in filenames:
    read_info(file)
time_end = datetime.now()
print(time_end - time_start)


if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.now()
    print(time_end - time_start)







