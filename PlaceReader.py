import csv
import Location


def parseData(path, name):
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        headers = next(reader)
        names = list()
        specialAttrs = list()
        positions = list()
        portals = list()
        for row in reader:
            names.append(row[0])

            rowSpecialAttrs = list()
            if row[1].lower() == "yes":
                rowSpecialAttrs.append(headers[1])
            if row[2].lower() == "yes":
                rowSpecialAttrs.append(headers[2])
            if row[3].lower() == "yes":
                rowSpecialAttrs.append(headers[3])
            if row[4].lower() == "yes":
                rowSpecialAttrs.append(headers[4])
            if not all(x is None for x in rowSpecialAttrs):
                specialAttrs.append(rowSpecialAttrs)
            else:
                specialAttrs.append(None)

            if row[5].lower() == "yes":
                portals.append(row[0])

            if row[6] not in (None, ""):
                positions.append(row[6].split('|'))
            else:
                positions.append(None)
    ret = Location.Location(name, names, specialAttrs, positions, portals)
    return ret
