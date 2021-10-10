#
import json
#from shutil import copyfile


# Needed properties in geo.json
needed_props = {
    "sa2Id": "num",
    "sa2Name": "region name",
    "stateName": "state",
    "sa3Id": "num",
    "sa3Name": "region name"
}

# Needed id number in geo.json
needed_id = {
    "id": "num"
}

# Current prop names
current_props = {
"SA2_CODE21":"101021007", # Need this
"SA2_NAME21":"Braidwood", # Need this
"CHG_FLAG21":"0",
"CHG_LBL21":"No change",
"SA3_CODE21":"10102", # Need this
"SA3_NAME21":"Queanbeyan", # Need this
"SA4_CODE21":"101",
"SA4_NAME21":"Capital Region",
"GCC_CODE21":"1RNSW",
"GCC_NAME21":"Rest of NSW",
"STE_CODE21":"1",
"STE_NAME21":"New South Wales", # Need this
"AUS_CODE21":"AUS",
"AUS_NAME21":"Australia",
"AREASQKM21":3418.3525,
"LOCI_URI21":"http://linked.data.gov.au/dataset/asgsed3/SA2/101021007"
}

def fetch_properties(data):
    feature_properties = []

    # Commented out for testing
    for i in range(len(data["features"])):
        feature_properties.append(data["features"][i]["properties"])

    return feature_properties

def edit_properties(feature_properties):
    edited_properties = []

    # Commented out for testing
    for i in range(len(feature_properties)):
        temp_props = {
            "sa2Id": feature_properties[i]["SA2_CODE21"],
            "sa2Name": feature_properties[i]["SA2_NAME21"],
            "stateName": feature_properties[i]["STE_NAME21"],
            "sa3Id": feature_properties[i]["SA3_CODE21"],
            "sa3Name": feature_properties[i]["SA3_NAME21"]
        }
        edited_properties.append(temp_props)

    return edited_properties

def property_to_string(edited_properties):
    printing_keys = ["\"sa2Id\"", "\"sa2Name\"", "\"stateName\"", "\"sa3Id\"", "\"sa3Name\""]
    test_dict = edited_properties
    output = "\"properties\":{"

    count = 0
    for key in test_dict:
        if (count < 4):
            output += printing_keys[count] + ":\"" + test_dict[key] + "\","
        else:
            output += printing_keys[count] + ":\"" + test_dict[key] + "\"},"

        count = count + 1

    output += "\"id\":\"" + test_dict["sa2Id"] + "\"},\n"
    return output


def main():
    print("Initialising operations...")
    with open('../Data/SA2_2021_AUST_GDA2020.json') as data_file:
        data = json.load(data_file)

    print("Fetching data...")
    feature_properties = fetch_properties(data)

    print("Editing properties...")
    edited_properties = edit_properties(feature_properties)

    data_file.close()
    print("Data operations complete.")

    file = open('../data/SA2_2021_AUST_GDA2020.json', 'r')
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
    output_file = open("../data/geo.json", 'w')
    for line in output_data:
        output_file.write(line)

    output_file.close()
    print("Operation complete. Program shutting down.")

# Run operations
main()
