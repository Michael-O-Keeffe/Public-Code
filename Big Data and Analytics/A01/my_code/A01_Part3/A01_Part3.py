#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import os
import codecs
import sys
import bisect


# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # 1. We create the output variable
    res = ()

    # 2. We get the parameter list from the line
    params_list = line.strip().split(",")

    # (00) start_time => A String representing the time the trip started at <%d/%m/%Y %H:%M:%S>. Example: “2019/05/02 10:05:00”
    # (01) stop_time => A String representing the time the trip finished at <%d/%m/%Y %H:%M:%S>. Example: “2019/05/02 10:10:00”
    # (02) trip_duration => An Integer representing the duration of the trip. Example: 300
    # (03) start_station_id => An Integer representing the ID of the CityBike station the trip started from. Example: 150
    # (04) start_station_name => A String representing the name of the CitiBike station the trip started from. Example: “E 2 St &; Avenue C”.
    # (05) start_station_latitude => A Float representing the latitude of the CitiBike station the trip started from. Example: 40.7208736
    # (06) start_station_longitude => A Float representing the longitude of the CitiBike station the trip started from. Example:  -73.98085795
    # (07) stop_station_id => An Integer representing the ID of the CityBike station the trip stopped at. Example: 150
    # (08) stop_station_name => A String representing the name of the CitiBike station the trip stopped at. Example: “E 2 St &; Avenue C”.
    # (09) stop_station_latitude => A Float representing the latitude of the CitiBike station the trip stopped at. Example: 40.7208736
    # (10) stop_station_longitude => A Float representing the longitude of the CitiBike station the trip stopped at. Example:  -73.98085795
    # (11) bike_id => An Integer representing the id of the bike used in the trip. Example:  33882
    # (12) user_type => A String representing the type of user using the bike (it can be either “Subscriber” or “Customer”). Example: “Subscriber”.
    # (13) birth_year => An Integer representing the birth year of the user using the bike. Example:  1990
    # (14) gender => An Integer representing the gender of the user using the bike (it can be either 0 => Unknown; 1 => male; 2 => female). Example:  2.
    # (15) trip_id => An Integer representing the id of the trip. Example:  190

    # 3. If the list contains the right amount of parameters
    if (len(params_list) == 16):
        # 3.1. We set the right type for the parameters
        params_list[2] = int(params_list[2])
        params_list[3] = int(params_list[3])
        params_list[5] = float(params_list[5])
        params_list[6] = float(params_list[6])
        params_list[7] = int(params_list[7])
        params_list[9] = float(params_list[9])
        params_list[10] = float(params_list[10])
        params_list[11] = int(params_list[11])
        params_list[13] = int(params_list[13])
        params_list[14] = int(params_list[14])
        params_list[15] = int(params_list[15])

        # 3.2. We assign res
        res = tuple(params_list)

    # 4. We return res
    return res


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_folder, output_file, bike_id):
    input = os.listdir(input_folder)

    trip_dict = {}
    trip_count = 0

    for item in input:
        input_data = open(input_folder + item, "r")
        for line in input_data:
            parameters = process_line(line)
            trip_bike_id = parameters[11]
            start_station = parameters[4]
            start_time = parameters[0]
            finish_station = parameters[8]
            finish_time = parameters[1]

            if trip_bike_id == bike_id:
                trip_dict[trip_count] = {"start_station": start_station, "start_time": start_time,
                                         "finish_station": finish_station, "finish_time": finish_time}
                trip_count += 1
        input_data.close()
    # for i in trip_dict:
    # print(trip_dict[i])
    trucked_dict = {}
    trucked_count = 0
    for i in range(trip_count-1):
        if trip_dict[i]["finish_station"] != trip_dict[i + 1]["start_station"]:
            trucked_dict[trucked_count] = {"start_move_time": trip_dict[i]["finish_time"],
                                           "start_move_station": trip_dict[i]["finish_station"],
                                           "finish_move_time": trip_dict[i+1]["start_time"],
                                           "finish_move_station": trip_dict[i+1]["start_station"]}
            trucked_count += 1

    if os.path.exists(output_file):
        os.remove(output_file)

    output_data = open(output_file, "w")
    trucked_dict = trucked_dict.items()

    for trip in trucked_dict:
        #print(trip[1])
        output = "By_Truck\t(" + str(trip[1]["start_move_time"]) + ", " + str(trip[1]["start_move_station"]) + ", " + str(trip[1]["finish_move_time"]) + ", " + str(trip[1]["finish_move_station"]) + ")\n"
        output_data.write(output)
    output_data.close()


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    input_folder = "../../my_dataset/"
    output_file = "../../my_results/A01_Part3/result.txt"
    bike_id = 35143

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        input_folder = sys.argv[1]
        output_file = sys.argv[2]

    # 2. We call to my_main
    my_main(input_folder, output_file, bike_id)
