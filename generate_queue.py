import json
from os.path import exists as file_exists


class QueueHandler:
    
    def __init__(self,queue_name = '') -> None:
        self.queue_name = queue_name


    def generate_queue(self):
        try:
            data = []
            filename = '{}.json'.format(self.queue_name)

            check_file = file_exists(filename)
            
            if check_file:
                return 'This Queue is already exist'
            
            with open(filename, 'w') as f:
                f.write(json.dumps(data,ensure_ascii=False))
                
            return 'Your Queue is successfully Created'
        
                
        except Exception as e:
            return 'Something Wrong to Create Queue.Please Try Again.'
            
        
