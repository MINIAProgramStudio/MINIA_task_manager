class Task:
    id = -1  # positive integer
    data = {
        "name": "",  # string
        "description": "",  # string
        "created_by": "",  # string
        "editors": [],  # list [['editor1', timestamp],...]
        "deadline": -1,  # timestamp or -1 if undefined
        "best_to_do_before": -1,  # timestamp or -1 if undefined
        "time_to_travel_from_task_group": 0,  # seconds integer
        "regularity": {
            "repeat": 0,  # integer. if positive -- equals the number of times the task will be recreated. If -1 -- task will be recreated infinetely
            "recreate_after": -1  # time in seconds after the deadline (or best_to_do_before if deadline is not defined). If eslapsed -- task is recreated
        }
    }

    relations = {}
    '''
    relations = {Task_id: time_of_travel integer} 
    If task from same TaskGroup is not present, time will be calculated via traveling through TaskGroup. 
    If task not from same TaskGroup is not present, time of travel will be calculated via traveling through point zero.
    '''

class TaskGroup:
    id = -1
    tasks = {}  # id: Task
    data = {
        "name": "",  # string
        "description": "",  # string
        "created_by": "",  # string
        "editors": [],  # list [['editor1', timestamp],...]
        "time_to_travel": 0,  # seconds integer. Time to travel from and to the zero point
        "regularity": {
            "repeat": 0, # integer. if positive -- equals the number of times the group will be recreated. If -1 -- group will be recreated infinetely
            "recreate_after": -1
            # time in seconds after the deadline of the last task (or best_to_do_before if deadline is not defined). If eslapsed -- group is recreated
        }
    }

    relations = {}
    '''
    relations = {TaskGroup_id: time_of_travel integer} 
    If a TaskGroup is not present, time of travel will be calculated via traveling through point zero.
    '''