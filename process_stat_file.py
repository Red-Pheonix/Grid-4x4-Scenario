from lxml import etree

root = etree.parse('stat.xml')

vehicles_inserted = int(root.find(".//vehicles").attrib['inserted'])
vehicles_waiting = int(root.find(".//vehicles").attrib['waiting'])
depart_delay = float(root.find(".//vehicleTripStatistics").attrib['departDelay'])
depart_delay_waiting = float(root.find(".//vehicleTripStatistics").attrib['departDelayWaiting'])

vehicle_count = float(root.find(".//vehicleTripStatistics").attrib['count'])
vehicle_duration = float(root.find(".//vehicleTripStatistics").attrib['duration'])
bike_count = float(root.find(".//bikeTripStatistics").attrib['count'])
bike_duration = float(root.find(".//bikeTripStatistics").attrib['duration'])

# avg_duration = (vehicle_duration * vehicle_count + bike_duration * bike_count) / (vehicle_count + bike_count)
avg_duration = vehicle_duration



totalTravelTimeAndDelay = vehicles_inserted * (avg_duration + depart_delay) + vehicles_waiting * depart_delay_waiting

print(totalTravelTimeAndDelay/(vehicle_count+vehicles_waiting))