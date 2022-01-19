#  A simple case of time table generator
import random
import math
# import DarwinPy


# Combining genetic algorithm with simulated annealing
class HybridSimulatedAnnealing:
    pass 

# Combining genetic algorithm with stochastic annealing
class HybridStochasticHillClimbing:
    pass

# Generating time table generator
class TimeTableGenerator:

    # Valid time table
    _valid_table = {}
    # _time_of_slots_per_day = 0
    # _number_of_days = 0


    # helper function for greedy matching solution
    def _matching_function(self,
    class_,
    teacher,
    teacher_subject_dict):
        matched = set()
        path = []
        # print(class_)
        if class_ <= teacher:
            for i in range(len(class_)):
                index = random.randint(0,len(teacher)-1)
                if index in matched:
                    continue
                else:
                    matched.add(index)
                    subject = random.choice(
                        teacher_subject_dict[teacher[index]])
                    path.append((class_[i],teacher[index],subject))
        else:
            for i in range(len(teacher)):
                index = random.randint(0, len(teacher)-1)
                if index in matched:
                    continue
                else:
                    matched.add(index)
                    subject = random.choice(
                        teacher_subject_dict[teacher[index]])
                    path.append((class_[i],teacher[index]))
        return path 


    # generate a valid table using greedy algorithm
    def generate_valid_table_naive(self,
    number_of_days,
    time_slots_per_day,
    teacher_subject_dict,
    class_subject_dict):
        #  For each slot allocate teachers to class with respective subject
        teacher = [x for x in teacher_subject_dict]
        class_ = [x for x in class_subject_dict]

        # print(teacher)
        valid_table = {}
        for i in range(number_of_days):
            valid_table[i] = []
            for j in range(time_slots_per_day):
                valid_table[i].append(
                    self._matching_function(class_,
                    teacher,teacher_subject_dict)
                )
        # Stored valide table in the valid table attribute
        self._valid_table = valid_table
        # print(valid_table)
        # self._find_attempted_subject_per_class(valid_table,class_subject_dict)
        # self._cost_function(
        #     valid_table,
        #     class_subject_dict
        # )
        return valid_table
    

    # 
    def _cost_function(self,valid_table,class_subject_dict):
        result  = self._find_attempted_subject_per_class(
            valid_table,
            class_subject_dict
        )
        fitness = .0
        for key in class_subject_dict:
            if key in result:
                fitness += len(result[key])/len(class_subject_dict[key])
            else:
                fitness += 0
            pass
        # print(fitness)
        return fitness


    # Find attempted subject per class
    def _find_attempted_subject_per_class(self,valid_type,class_subject_dict):
        result = {}
        for key in valid_type:
            for slot in valid_type[key]:
                for class_ in slot:
                    if class_[0] not in result:
                        result[class_[0]] = {class_[2]:1}
                    elif class_[2] not in result[class_[0]]:
                        result[class_[0]][class_[2]] = 1
                    else:
                        continue
        # print(result)
        
        return result


    # generate a time table
    def generate_time_table(self,
    number_of_days,
    time_slots_per_day,
    teacher_subject_dict,
    class_subject_dict):
        time_best = self.generate_valid_table_naive(number_of_days,
        time_slots_per_day,
        teacher_subject_dict,
        class_subject_dict)
        number_of_class = len(class_subject_dict)
        # print(time_best)
        while not (number_of_class == self._cost_function(time_best,class_subject_dict)):
            time_temp = self.generate_valid_table_naive(number_of_days,
            time_slots_per_day,
            teacher_subject_dict,
            class_subject_dict)
            # print("ping!")
            if self._cost_function(time_best, class_subject_dict) < self._cost_function(time_temp,class_subject_dict):
                time_best = time_temp
        return time_best
