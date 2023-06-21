import csv
from datetime import datetime

ocean_time = 0
rocket_time = 0
estec_time = 0
sentinel6_time = 0
earth_time = 0
venice_time = 0
estecvideo_time = 0
rocketvideo_time = 0
satellitevideo_time = 0
earthvideo_time = 0
venicevideo_time = 0

with open('p20.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    rows = list(reader)

for index in range(len(rows)):
    timestamp = rows[index]['Time']
    label = rows[index]['Actor Label']

    if label == '/ocean':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/ocean':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            ocean_time += (end_time - start_time).total_seconds()
    elif label == '/Falcon 9 Rocket':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/Falcon 9 Rocket':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            rocket_time += (end_time - start_time).total_seconds()
    elif label == '/estec':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/estec':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            estec_time += (end_time - start_time).total_seconds()
    elif label == '/Sentinel-6 satellite':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/Sentinel-6 satellite':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            sentinel6_time += (end_time - start_time).total_seconds()
    elif label == '/Earth':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/Earth':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            earth_time += (end_time - start_time).total_seconds()
    elif label == '/Venice city':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/Venice city':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            venice_time += (end_time - start_time).total_seconds()
    elif label == '/estecvideo':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/estecvideo':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            estecvideo_time += (end_time - start_time).total_seconds()
    elif label == '/rocketvideo':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/rocketvideo':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            rocketvideo_time += (end_time - start_time).total_seconds()
    elif label == '/satellitevideo':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/satellitevideo':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            satellitevideo_time += (end_time - start_time).total_seconds()
    elif label == '/earthevideo':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/earthevideo':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            earthvideo_time += (end_time - start_time).total_seconds()
    elif label == '/veniceevideo':
        start_time = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S:%f")
        if index < len(rows) - 1 and rows[index + 1]['Actor Label'] == '/veniceevideo':
            end_time = datetime.strptime(rows[index + 1]['Time'], "%Y:%m:%d:%H:%M:%S:%f")
            venicevideo_time += (end_time - start_time).total_seconds()


print("estec:", estec_time)
print("Falcon 9 Rocket:", rocket_time)
print("Sentinel-6 satellite:", sentinel6_time)
print("ocean:", ocean_time)
print("Earth:", earth_time)
print("Venice city:", venice_time)
print("estecvideo:", estecvideo_time)
print("rocketvideo:", rocketvideo_time)
print("satellitevideo:", satellitevideo_time)
print("earthvideo:", earthvideo_time)
print("venicevideo:", venicevideo_time)
