def traffic_data_generator():
    traffic_records = [
        {"vehicle": "MH12AB1234", "speed": 60},
        {"vehicle": "MH14CD5678", "speed": 45},
        {"vehicle": "MH15EF9012", "speed": 70},
        {"vehicle": "MH16GH3456", "speed": 50},
        {"vehicle": "MH17IJ7890", "speed": 40}
    ]

    for record in traffic_records:
        yield record


traffic_data = traffic_data_generator()

for record in traffic_data:
    print(record)