import pandas as pd
import os
import numpy as np
import re
import matplotlib.pyplot as plt
from utils.consts import DOWNLOAD_DIR

# פונקציה שבודקת אם יש תו עברי במילה
def is_hebrew(word):
    return bool(re.search(r'[\u0590-\u05FF]', word))  # חפש לפחות תו עברי במילה

def main():
    folder_path = DOWNLOAD_DIR
    # hebrew = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ך', 'ל', 'מ', 'ם', 'נ', 'ן', 'ס', 'ף', 'ע', 'פ',
    #           'ף', 'צ', 'ץ', 'ק', 'ר', 'ש', 'ת']
    israel = {}
    non_israel = {}
    uniq_artist = ['Noa Kirel', 'Tuna', 'E-Z', 'Ravid Plotnik', 'Eden Hason', 'Agam Buhbut', 'Peer Tasi', 'Geva Alon',
                   'Full Trunk, Sivan Talmor', 'Omer Adam, Nicky jam', 'Dennis Loyed', 'Noga Erez']
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            data = pd.read_csv(file_path)
            time = file_name[19:-4]
            for index, row in data.head(50).iterrows():
                if (is_hebrew(row['track_name']) or row['artist_names'] in uniq_artist or is_hebrew(row['artist_names'])):
                    if time in israel:
                        israel[time] += 1
                    else:
                        israel[time] = 1
                else:
                    if time in non_israel:
                        non_israel[time] += 1
                    else:
                        non_israel[time] = 1

    print(non_israel)
    print(israel)

    filtered_dates = list(israel.keys())

    israel_counts = [israel.get(date, 0) for date in filtered_dates]
    non_israel_counts = [non_israel.get(date, 0) for date in filtered_dates]


    print(israel_counts)
    print(non_israel_counts)
    print(filtered_dates)

    x = range(len(filtered_dates))
    width = 0.35
    fig, ax = plt.subplots()

    ax.bar(x, israel_counts, width, label='Israeli', color='blue')
    ax.bar([p + width for p in x], non_israel_counts, width, label='Non-Israeli', color='red')

    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Artists')
    ax.set_title('Number of Israeli and Non-Israeli Artists per Date')
    ax.legend()
    plt.xticks(rotation=45)
    ax.set_xticklabels(filtered_dates)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
# import pandas as pd
# import os
# import numpy as np
# import re
# import matplotlib.pyplot as plt
# from utils.consts import DOWNLOAD_DIR
#
#
# # פונקציה שבודקת אם יש תו עברי במילה
# def is_hebrew(word):
#     return bool(re.search(r'[\u0590-\u05FF]', word))  # חפש לפחות תו עברי במילה
#
#
# def combine_csv_with_date(directory_path, date_pattern=r"(\d{4}-\d{2}-\d{2})"):
#     csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
#
#     dataframes = []
#     for filename in csv_files:
#         filepath = os.path.join(directory_path, filename)
#         match = re.search(date_pattern, filename)
#         if match:
#             file_date = match.group(0)
#         else:
#             print(filename)
#             raise Exception()
#
#         df = pd.read_csv(filepath)
#         df['Date'] = file_date
#         dataframes.append(df)
#
#     if dataframes:
#         combined_df = pd.concat(dataframes, ignore_index=True)
#         return combined_df
#     else:
#         return pd.DataFrame()  # return an empty DataFrame
#
#
# def main():
#     folder_path = DOWNLOAD_DIR
#     israel = {}
#     non_israel = {}
#     uniq_artist = ['Noa Kirel', 'Tuna', 'E-Z', 'Ravid Plotnik', 'Eden Hason', 'Agam Buhbut', 'Peer Tasi', 'Geva Alon',
#                    'Full Trunk, Sivan Talmor', 'Omer Adam, Nicky jam', 'Dennis Loyed', 'Noga Erez']
#     df = combine_csv_with_date(folder_path)
#     df["Date"] = pd.to_datetime(df["Date"])  # Ensure that 'Date' is in datetime format
#
#     # Extract Year, Month, Day for further analysis if needed
#     df["Year"] = df["Date"].dt.year
#     df["Month"] = df["Date"].dt.month
#     df["Day"] = df["Date"].dt.day
#     filtered_dates = pd.to_datetime(list(israel.keys()))  # Ensure the dates are in datetime format
#     filtered_dates = filtered_dates[::3]
#
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith('.csv'):
#             file_path = os.path.join(folder_path, file_name)
#             data = pd.read_csv(file_path)
#             time = file_name[19:-4]
#             dates = pd.to_datetime(time)
#             for index, row in data.head(50).iterrows():
#                 if (is_hebrew(row['track_name']) or row['artist_names'] in uniq_artist or is_hebrew(
#                         row['artist_names'])):
#                     if dates in israel:
#                         israel[dates] += 1
#                     else:
#                         israel[dates] = 1
#                 else:
#                     if dates in non_israel:
#                         non_israel[dates] += 1
#                     else:
#                         non_israel[dates] = 1
#
#
#     df_grouped_by_date_sum_streams = df.groupby('Date', as_index=False).sum()
#
#     # Filtered dates (only every 3rd date)
#     filtered_dates = pd.to_datetime(list(israel.keys()))  # Ensure the dates are in datetime format
#     filtered_dates = filtered_dates[::3]  # Select every 3rd date
#     print (filtered_dates)
#
#     israel_counts = [israel.get(date, 0) for date in filtered_dates]
#     non_israel_counts = [non_israel.get(date, 0) for date in filtered_dates]
#     print (israel_counts)
#     print(non_israel_counts)
#     x = range(len(filtered_dates))
#
#     # Plotting the data
#     width = 0.35
#     fig, ax = plt.subplots()
#
#     # Change colors: Israeli artists are blue, non-Israeli artists are red
#     ax.bar(x, israel_counts, width, label='Israeli', color='blue')
#     ax.bar([p + width for p in x], non_israel_counts, width, label='Non-Israeli', color='red')
#
#     # Adding titles and labels
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Number of Artists')
#     ax.set_title('Number of Israeli and Non-Israeli Artists per Date')
#
#     # Formatting the x-axis to show only the filtered dates (every 3rd date)
#     ax.set_xticks(x)
#     ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in filtered_dates])
#
#     # Displaying the legend
#     ax.legend()
#
#     # Rotate the x-axis labels to prevent overlap
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#
#
# if __name__ == "__main__":
#     main()
