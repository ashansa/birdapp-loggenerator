__author__ = 'shelan'

import json
import datetime
import glob
import os

def question2_output(input):
    log_table = {}


    for filename in glob.iglob(os.path.join(input, '*')):
        log_file = open(filename)

        with log_file as input_file:
            for line in input_file:
                line = line.strip()
                tmp_split_vals = line.split(",")

                key = tmp_split_vals[1].strip() + "@" + tmp_split_vals[0].strip()
                if not (log_table.has_key(key)):
                    log_table[key] = tmp_split_vals[4]

                else:
                        log_table[key] =  int(log_table[key]) + int(tmp_split_vals [4])


    json.dump(log_table, open("q2-answer.json", "w+"))


def question1_output(input):

    log_table = {}

    for filename in glob.iglob(os.path.join(input, '*')):

        log_file = open(filename)
        with log_file as input_file:
            for line in input_file:
                line = line.rstrip()
                tmp_split_vals = line.split(",")

                if(tmp_split_vals[6].strip() == "2"):

                    if not (log_table.has_key(tmp_split_vals[1])):
                        log_table[tmp_split_vals[1]] = {'tower_id': tmp_split_vals[0], 'wing_span': tmp_split_vals[5]}

                    else:
                        value = log_table[tmp_split_vals[1]]
                        if (int(value['wing_span']) < int(tmp_split_vals[5])):
                            value['wing_span'] = int(tmp_split_vals[5])
                            value['tower_id'] = (tmp_split_vals[0])
                        log_table[tmp_split_vals[1]] = value

    json.dump(log_table, open("q1-answer.json", "w+"))


def question3_output(input):
    log_table = {}

    for filename in glob.iglob(os.path.join(input, '*')):
        log_file = open(filename)

        with log_file as input_file:
            for line in input_file:
                line = line.rstrip()
                tmp_split_vals = line.split(",")

                if(tmp_split_vals[3].strip()=='0' or tmp_split_vals[3].strip()=='-1'):
                    break


                if not (log_table.has_key(tmp_split_vals[3])):
                    log_table[tmp_split_vals[3]] = tmp_split_vals[1]

                else:

                    current_date_arr = str(log_table[tmp_split_vals[3]]).split("-");
                    current_date = datetime.date(int(current_date_arr[0]), int(current_date_arr [1]), int (current_date_arr[2]))

                    new_date_arr = str(tmp_split_vals[1]).split("-")
                    new_date = datetime.date(int(new_date_arr[0]), int(new_date_arr [1]), int(new_date_arr[2]))

                    if (new_date > current_date):
                        log_table[tmp_split_vals[3]] = tmp_split_vals[1]

    json.dump(log_table, open("q3-answer.json", "w+"))


file_name = raw_input("Please enter your folder: ")
question1_output(file_name)
question2_output(file_name)
question3_output(file_name)