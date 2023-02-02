users = ['oren', 'mcintosh', 'bpacheco', 'blossom.poop', 'l.vaida']

with open('finalprc.txt', 'w+', newline='') as file:
    for i in range(4):
        file.write("ubuntu.local ticky: ERROR Timeout while retrieving information ({})\n".format(users[i]))
        file.write("ubuntu.local ticky: INFO Commented on ticket [#3813] ({})\n".format(users[i]))
        file.write("ubuntu.local ticky: ERROR Connection to DB failed ({})\n".format(users[i]))
        file.write("ubuntu.local ticky: ERROR The ticket was modified while updating ({})\n".format(users[i]))
        file.write("ubuntu.local ticky: ERROR Connection to DB failed ({})\n".format(users[i]))
        file.write("ubuntu.local ticky: INFO Closed ticket [#8604] ({})\n".format(users[i]))
        