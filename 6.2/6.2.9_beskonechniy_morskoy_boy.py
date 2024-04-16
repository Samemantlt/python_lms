import pandas as pd


min_x, min_y = map(int, input().split(' '))
max_x, max_y = map(int, input().split(' '))

min_y, max_y = sorted([min_y, max_y])
min_x, max_x = sorted([min_x, max_x])

rows_per_chunk = 5000
first_time = True

glob_result = None

with pd.read_csv('data.csv', chunksize=rows_per_chunk) as reader:
    for steps in reader:
        steps: pd.DataFrame = steps
        result = steps[(min_x <= steps["x"]) & (min_y <= steps["y"]) & (max_x >= steps["x"]) & (max_y >= steps["y"])]
        
        if glob_result is None:
            glob_result = result
        else:
            glob_result = pd.concat([glob_result, result])
        

print(glob_result)
