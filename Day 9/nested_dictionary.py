travel_log = {
    "Indonesia": ["Jakarta", "Bandung", "Malang", "Bali"],
    "Japan": ["Tokyo", "Kyoto", "Osaka", "Akibahara"]
}

# print the item on the nested list
print(travel_log["Indonesia"][1])

# nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# nested nested dictionary
travel_log_new = {
    "Indonesia": {
        "total_visits": 10,
        "cities_visited": ["Jakarta", "Bandung", "Malang", "Bali"]
    },
    "Japan": {
        "total_visits": 10,
        "cities_visited": ["Tokyo", "Kyoto", "Osaka", "Akibahara"]
    } 
}

print(travel_log_new["Japan"]["cities_visited"][3]) # print the akibahara on the nested nested dictionary list