# This generate logs in the following format
#
#Sintra-1, 2013-10-09, 17:54.01, eagle-25, 3, 120, 0
#
# output file will be bird-log with log entries
#
#

import time
import random


def read_input_files():
    with open("input") as input_file:
        for line in input_file:
            line = line.rstrip()
            tmp_split_vals = line.split(":")

            if tmp_split_vals[0] == 'no_of_lines':
                no_of_lines = tmp_split_vals[1]

            if tmp_split_vals[0] == 'tower_ids':
                tower_ids = tmp_split_vals[1].split(",")

            if tmp_split_vals[0] == 'bird_ids':
                bird_ids = tmp_split_vals[1].split(",")

        input_file.close()

        return no_of_lines, tower_ids, bird_ids


def generate_random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    format = '%Y-%m-%d %H:%M:%S'

    startTime = int(time.time())
    endTime = time.mktime(time.strptime("2013-01-01 00:00:00", format))

    generatedTime = startTime + random.random() * (endTime - startTime)

    return time.strftime(format, time.localtime(generatedTime))


def generate_log():
    """
    sample log entry
    Sintra-1, 2013-10-09, 17:54.01, eagle-25, 3, 120, 0.
    :return:
    """
    logfile = open("bird-log", "w+");
    for x in xrange(0, int(no_of_lines)):
        randomDate = generate_random_date().split(" ");
        print("generating line no : ", x)

        bird_id = random.choice(bird_ids);

        if(bird_id == '-1'):
            logfile.writelines(random.choice(tower_ids) + ', ' + randomDate[0] + ', ' + randomDate[1] + ', '
                               + bird_id + ', ' + '0' + ', ' + '0' + ', ' +
                               str(random.randint(0, 3)) + "\n")
        elif(bird_id == '0'):
            logfile.writelines(random.choice(tower_ids) + ', ' + randomDate[0] + ', ' + randomDate[1] + ', '
                               + bird_id + ', ' + str(random.randint(1, 6)) + ', ' + str(
                random.randint(5, 200)) + ', ' +
                               str(random.randint(0, 3)) + "\n")
        else :
            logfile.writelines(random.choice(tower_ids) + ', ' + randomDate[0] + ', ' + randomDate[1] + ', '
                           + bird_id + ', ' + str(random.randint(1, 6)) + ', ' + str(
            random.randint(5, 200)) + ', ' +
                           str(random.randint(0, 3)) + "\n")

    logfile.close()


no_of_lines, tower_ids, bird_ids = read_input_files()

generate_log()