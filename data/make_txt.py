import pandas as pd
import os

def make(folder_name):
    folder_path = f"./{folder_name}"
    # load file name in folder
    file_names = os.listdir(folder_path)
    filename = f"{folder_name}.txt"
    cnt = 0
    f = open(f"../crawling/{filename}", "w")
    for file in file_names:
        file_path = os.path.join(folder_path, file)
        # load csv file as dataframe
        df = pd.read_csv(file_path)
        if len(df) == 1253:
            f.write(file + "\n")
            cnt += 1
    f.close()
    print(str(cnt) + '\n')

if __name__ == "__main__":
    make("growth")
    make("overlap")
    make("value")
