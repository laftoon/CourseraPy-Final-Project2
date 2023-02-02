import re 
import operator 
import csv
import sys 

error_log = {}  #create dictionaries that will store the stats
user_log = {}

log_file = 'finalprc.txt'  #rename as needed for log file and destinations
user_stats = 'user_stats.txt'
error_stats = 'error_stats.txt'

pattern = r'(?P<messageType>INFO|ERROR):?\s*(?P<message>.*?)\((?P<username>\w+?.\w+)\)$'  #regex universal pattern grouping




with open(log_file, 'r') as f:
    for line in f.readlines():
        result = re.search(pattern, line)
        if result:
            message_type = result.group('messageType')  #extract data and group it 
            message = result.group('message')
            username = result.group('username')
            if message_type == 'ERROR':
                error_log.setdefault(message, 0)
                error_log[message] +=1
                user_log.setdefault(username, [0, 0])[1] +=1
            else:
                user_log.setdefault(username, [0, 0])[0] +=1

sorted_error_stats=sorted(error_log.items(), key = operator.itemgetter(1), reverse = True )  #sort data as required
sorted_user_stats = sorted(user_log.items())

with open(user_stats, 'w', newline='') as ereport:  #export reports
    writer = csv.writer(ereport)
    writer.writerow(["Error", "Count"])
    writer.writerows(sorted_error_stats)

with open(error_stats, 'w', newline='') as ureport:
    writer = csv.writer(ureport)
    writer.writerow(["Userame", "INFO", "ERROR"])
    for item in sorted_user_stats:
        onerow = [item[0], item[1][0], item[1][1]]
        writer.writerow(onerow)    
