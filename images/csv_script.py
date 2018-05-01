import os
import csv

label_names = []

def update_csv_file():
    with open('labels.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Path"] + ["Label"])
    
        for dirName, subdirList, fileList in os.walk('./'):
            for filename in fileList:
                label_name = dirName[1:] + "/" + filename
                if "positive_images" in label_name:
                    # writerow for 1
                    label_name = dirName[1:] + "/" + filename
                    writer.writerow([label_name] + ["1"])
                elif "negative_images" in label_name:
                    # writerow for 0
                    label_name = dirName[1:] + "/" + filename
                    writer.writerow([label_name] + ["0"])


update_csv_file()