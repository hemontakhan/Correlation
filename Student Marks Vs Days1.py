import csv 
import numpy as np

def getSource(data_path):
    marks_percentage = []
    days_present = []
    with open(data_path) as ref_file:
        reference = csv.DictReader(ref_file)
        for row in reference:
          marks_percentage.append(float(row["Marks In Percentage"]))
          days_present.append(float(row["Days Present"]))

    return {"x":marks_percentage,"y":days_present}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("The Correlation of the data is :-  \n--->",correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"

    dataSource = getSource(data_path)
    findCorrelation(dataSource)

setup()