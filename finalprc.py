import re 
import operator 
import csv
import sys 

error_log = {}
user_log = {}

log_file = 'finalprc.txt'
user_stats = 'user_stats.txt'
error_stats = 'error_stats.txt'

pattern = r'(?P<messageType>INFO|ERROR):?\s*(?P<message>.*?)\((?P<username>\w+?.\w+)\)$'




with open(log_file, 'r') as f:
    for line in f.readlines():
        result = re.search(pattern, line)
        if result:
            message_type = result.group('messageType')
            message = result.group('message')
            username = result.group('username')
            if message_type == 'ERROR':
                error_log.setdefault(message, 0)
                error_log[message] +=1
                user_log.setdefault(username, [0, 0])[1] +=1
            else:
                user_log.setdefault(username, [0, 0])[0] +=1

sorted_error_stats=sorted(error_log.items(), key = operator.itemgetter(1), reverse = True )
sorted_user_stats = sorted(user_log.items())

with open(user_stats, 'w', newline='') as ereport:
    writer = csv.writer(ereport)
    writer.writerow(["Error", "Count"])
    writer.writerows(sorted_error_stats)

with open(error_stats, 'w', newline='') as ureport:
    writer = csv.writer(ureport)
    writer.writerow(["Userame", "INFO", "ERROR"])
    for item in sorted_user_stats:
        onerow = [item[0], item[1][0], item[1][1]]
        writer.writerow(onerow)    
