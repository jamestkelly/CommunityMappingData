# Script to parse raw data taken from source data (Government)

#
import json

#
with open('../Data/RegionalAreaEntity.json') as file:
    data = json.load(file)

#
def write_information_file(data):
    printing_keys = ["\"sa2Id\"", "\"sa3Id\"", "\"sa3Name\"", "\"numOfPph\"", \
                 "\"percentPphPerDay\"", "\"sa2Name\"", "\"indigenous\"", \
                 "\"nonIndigenous\""]
    field_keys = ["sa2Id", "sa3Id", "sa3Name", "numOfPph", "percentPphPerDay", \
              "sa2Name", "indigenous", "nonIndigenous"]

    file = open("../Data/ausInformation.json", "w")
    file.write("{\n")
    
    for i in range(len(data)):
        blob = data[i]
        file.write("\t")
        file.write('"')
        object_key = blob["sa2Id"]
        file.write(str(object_key))
        file.write('": {\n')
        
        counter = 0
        
        for key in printing_keys:
            value = blob[field_keys[counter]]

            if (counter < len(field_keys) - 1):
                file.write("\t\t" + key + ": \"" + str(value) + "\",\n")
            else:
                file.write("\t\t" + key + ": \"" + str(value) + "\"\n")

            counter = counter + 1

        if (i < len(data) - 1):
            file.write("\t},\n")
        else:
            file.write("\t}\n")

    file.write("}")
    file.close()

#
def write_seifa_file(data):
    printing_keys = ["\"sa2Id\"", "\"sa2Name\"", "\"irsd\"", "\"irsad\"", "\"ier\"", "\"ieo\""]
    field_keys = ["sa2Id", "sa2Name", "irsd", "irsad", "ier", "ieo"]

    file = open("../Data/ausSeifa.json", "w")
    file.write("{\n")

    for j in range(len(data)):
        blob = data[j]
        file.write("\t")
        file.write('"')
        object_key = blob["sa2Id"]
        file.write(str(object_key))
        file.write('": {\n')

        counter = 0

        for key in printing_keys:
            value = blob[field_keys[counter]]

            if (counter < len(field_keys) - 1):
                file.write("\t\t" + key + ": \"" + str(value) + "\",\n")
            else:
                file.write("\t\t" + key + ": \"" + str(value) + "\"\n")

            counter = counter + 1

        if (j < len(data) - 1):
            file.write("\t},\n")
        else:
            file.write("\t}\n")

    file.write("}")
    file.close()

#
write_information_file(data)
write_seifa_file(data)