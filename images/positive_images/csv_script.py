import os
import csv

label_names = []

def build_list_label():
    for dirName, subdirList, fileList in os.walk('./'):
        for filename in fileList:
            if ".jpg" in filename:
                label_name = dirName[1:] + "/" + filename
                label_names.append(label_name)

def update_csv_file():
    build_list_label()

    with open('labels.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for label_name in label_names:
            writer.writerow([label_name] + ["1"])


update_csv_file()