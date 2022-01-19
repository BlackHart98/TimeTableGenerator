from unittest import result
import TimeTableGenerator


def parse_data(class_subject,teacher_subject):
    data_0 = class_subject.split("\n")
    data_1 = teacher_subject.split("\n")
    header_0 = data_0[0]
    header_1 = data_1[0]
    class_subject_rawdata = data_0[1:]
    teacher_subject_rawdata = data_1[1:]
    class_subject_data = {}
    for data in class_subject_rawdata:
        splited_data = data.split(",")
        if splited_data[1] not in class_subject_data:
            class_subject_data[splited_data[1]] = [splited_data[2]]
        else:
            class_subject_data[splited_data[1]].append(splited_data[2])
    
    teacher_subject_data = {}
    for data in teacher_subject_rawdata:
        splited_data = data.split(",")
        if splited_data[1] not in teacher_subject_data:
            teacher_subject_data[splited_data[1]] = [splited_data[2]]
        else:
            teacher_subject_data[splited_data[1]].append(splited_data[2])
    return (header_0,header_1,class_subject_data,teacher_subject_data)


def generate_time_table_csv(combined_table):
    output = open("testcase/time_table.csv","w+")
    output.write("id,day,time_slot,class_id,teacher_id,subject\n")
    id = 0
    for day in combined_table:
        slot_val = 0
        for slot in combined_table[day]:
            for class_ in slot:
                output.write("{0},{1},{2},{3},{4},{5}\n".format(id,day,slot_val,class_[0],class_[1],class_[2]))
                id += 1
            slot_val += 1
        pass



if __name__ == '__main__':

    time_slots_per_day = 3
    number_of_days = 4


    file_obj = open("testcase/class_subject.csv","r")
    class_subject = file_obj.read()
    file_obj = open("testcase/teacher_subject.csv","r")
    teacher_subject = file_obj.read()
    file_obj.close()

    data = parse_data(class_subject,teacher_subject)


    table_gen = TimeTableGenerator.TimeTableGenerator()

    teacher_subject_dict = data[3]
    class_subject_dict = data[2]
    

    # generate time table
    combined_table = table_gen.generate_time_table(number_of_days,
    time_slots_per_day,
    teacher_subject_dict,
    class_subject_dict
    )

    generate_time_table_csv(combined_table)




    


