# DESCRIPTION
# Script to update file, 'geo-numeric.json' with the current gap scores from
# database

# Import packages
import json, glob, os, csv, pprint

#
def read_csv(latest_csv):
    file = open(latest_csv)
    csv_reader = csv.reader(file)
    header = []
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)
    file.close()

    return rows

#
def fetch_props(data):
    feature_props = [] # Initialise an empty array

    # Iterate through all features
    for i in range(len(data["features"])):
        feature_props.append(data["features"][i]["properties"]) # Append the properties

    # Return the array
    return feature_props

#
def fetch_gap_score(sa2Id, csv_data):
    for i in range(len(csv_data)):
        if csv_data[i][0] == sa2Id:
            return csv_data[i][1]
        elif i == len(csv_data) - 1:
            #print(csv_data[5][1])
            return csv_data[5][1]

#
def edit_props(feature_properties, latest_csv):
    edited_props = [] # Initialise an empty array
    csv_data = read_csv(latest_csv)

    # Iterate through all properties and append values
    for i in range(len(feature_properties)):
        # Fetch corresponding "gap score"
        gap_score = fetch_gap_score(feature_properties[i]["sa2Id"], csv_data)

        temp_props = {
            "sa2Id": feature_properties[i]["sa2Id"],
            "sa2Name": feature_properties[i]["sa2Name"],
            "stateName": feature_properties[i]["stateName"],
            "sa3Id": feature_properties[i]["sa3Id"],
            "sa3Name": feature_properties[i]["sa3Name"],
            "gapScore": gap_score
        }

        edited_props.append(temp_props)

    return edited_props

#
def property_to_string(edited_properties):
    integer_keys = ["sa2Id", "sa3Id", "gapScore"]
    printing_keys = ["\"sa2Id\"", "\"sa2Name\"", "\"stateName\"", "\"sa3Id\"", "\"sa3Name\"", "\"gapScore\""]
    test_dict = edited_properties
    output = "\"properties\":{"

    count = 0
    for key in test_dict:
        if (count < 5):
            if (key not in integer_keys):
                output += printing_keys[count] + ":\"" + test_dict[key] + "\","
            else:
                output += printing_keys[count] + ":" + test_dict[key] + ","
        else:
            if (key not in integer_keys):
                output += printing_keys[count] + ":\"" + test_dict[key] + "\"},"
            else:
                output += printing_keys[count] + ":" + test_dict[key] + "},"

        count = count + 1

    output += "\"id\":\"" + test_dict["sa2Id"] + "\"},\n"
    return output

#
def prop_to_string_last(edited_properties):
    printing_keys = ["\"sa2Id\"", "\"sa2Name\"", "\"stateName\"", "\"sa3Id\"", "\"sa3Name\"", "\"gapScore\""]
    test_dict = edited_properties
    output = "\"properties\":{"

    count = 0
    for key in test_dict:
        if (count < 5):
            output += printing_keys[count] + ":\"" + test_dict[key] + "\","
        else:
            output += printing_keys[count] + ":\"" + test_dict[key] + "\"},"

        count = count + 1

    output += "\"id\":\"" + test_dict["sa2Id"] + "\"}\n"
    return output

# 
def main():
    # Specify path to .csv file location in data directory
    data_dir = glob.glob('../Data/*.csv')
    latest_csv = max(data_dir, key = os.path.getctime) # Fetch latest .csv in directory

    print("Initialising operations...")
    with open('../Data/geo.json') as data_file:
        data = json.load(data_file)

    print("Fetching data...")
    feature_properties = fetch_props(data)

    print("Editing properties...")
    edited_properties = edit_props(feature_properties, latest_csv)

    data_file.close()
    print("Data operations complete.")

    file = open('../Data/geo.json', 'r')
    data = file.readlines()

    output_data = []
    counter = 0

    print("Converting data to write...")
    for line in data:
        if "properties" in line:
            prop_start = line.index("properties") - 1
            new_line = line[:prop_start]
            if counter <= len(edited_properties) - 2:
                new_line += property_to_string(edited_properties[counter])
            else:
                new_line += prop_to_string_last(edited_properties[counter])

            counter = counter + 1
            output_data.append(new_line)
        else:
            output_data.append(line)

    print("Writing data to new file...")
    output_file = open("../data/geo-numeric.json", 'w')
    for line in output_data:
        output_file.write(line)

    output_file.close()
    print("Operation complete. Program shutting down.")

# Run operations
main()
