# DESCRIPTION
# Script to edit a 'geo.json' file to conform to the requirements
# of Mapbox-GL API.

# Import packages
import json

# Method to parse the 'properties' from the geo.json file.
def fetch_properties(data):
    feature_props = []

    for i in range(len(data["features"])):
        feature_props.append(data["features"][i]["properties"])

    return feature_props

def edit_props(feature_properties):
    edited_props = []

    for i in range(len(feature_properties)):
        temp_props = {
            "sa2Id": feature_properties[i]["sa2Id"],
            "sa2Name": feature_properties[i]["sa2Name"],
            "stateName": feature_properties[i]["stateName"],
            "sa3Id": feature_properties[i]["sa3Id"],
            "sa3Name": feature_properties[i]["sa3Name"]
        }
        edited_props.append(temp_props)

    return edited_props

# Method to edit the properties and convert them to a string.
def property_to_string(edited_properties):
    printing_keys = ["\"sa2Id\"", "\"sa2Name\"", "\"stateName\"", "\"sa3Id\"", "\"sa3Name\""]
    test_dict = edited_properties
    output = "\"properties\":{"

    count = 0
    for key in test_dict:
        if (count < 4):
            if (key is not "sa2Id" and key is not "sa3Id"):
                output += printing_keys[count] + ":\"" + test_dict[key] + "\","
            else:
                output += printing_keys[count] + ":" + test_dict[key] + ","
        else:
            if (key is not "sa2Id" and key is not "sa3Id"):
                output += printing_keys[count] + ":\"" + test_dict[key] + "\"},"
            else:
                output += printing_keys[count] + ":" + test_dict[key] + "},"

        count = count + 1

    output += "\"id\":\"" + test_dict["sa2Id"] + "\"},\n"
    return output

# Main method to run operations
def main():
    print("Initialising operations...")
    with open('../Data/geo.json') as data_file:
        data = json.load(data_file)

    print("Fetching data...")
    feature_properties = fetch_properties(data)

    print("Editing properties...")
    edited_properties = edit_props(feature_properties)

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
            new_line += property_to_string(edited_properties[counter])
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
