import pandas as pd
import matplotlib.pyplot as plt
import os
from utils.consts import DOWNLOAD_DIR

def main():
    folder_path = DOWNLOAD_DIR

    total_listen = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            data = pd.read_csv(file_path)
            # top50 = data.head(50)
            time = file_name[19:-4]
            print (time)
            for index, row in data.head(50).iterrows():
                total = row['streams']
                print(total)
                if time in total_listen:
                    print("yes")
                    total_listen[time] += total
                else:
                    print("no")
                    total_listen[time] = total


    print(total_listen)

    time = list(total_listen.keys())
    total_weekly = list(total_listen.values())
    plt.figure(figsize=(20, 6))
    plt.bar(time, total_weekly, color='skyblue')
    plt.title('toatl listeners by week', fontsize=16)
    plt.xlabel('date', fontsize=12)
    plt.ylabel('value', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()