import csv

zip_code = {}


def zipsetter():
    """ Trick is to read zip.csv file.
        Store it into dictonary like `zip:district` format.
        It will reduce the time-complexity of searching.
    """
    with open('zip.csv', encoding='cp1252') as zip:
        code = csv.reader(zip)
        for i in code:
            if(i[0].isdigit()):
                zip_code[i[0]] = i[1]
