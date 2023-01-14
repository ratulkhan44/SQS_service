#Python Impots
import json
import uuid
import sys

""" Responsible for Message Handling """
class MessageHandler:
    def __init__(self,queue_name = '',message_body='',message_id= '') -> None:
        self.queue_name = queue_name
        self.message_body = message_body
        self.message_id = message_id
        
    """ Generate uuid for Message id """    
    def generate_uuid(self):
        try:
            get_uuid = uuid.uuid4()
            return str(get_uuid)
        except:
            return None
        
    """ Responsible for build message body with an id and message  """
    def build_message_body(self):
        try:
            data = {}
            data['id'] = self.generate_uuid() if self.generate_uuid() else uuid.uuid4()
            data['body'] = self.message_body
            return data
        
        except Exception as e:
            return {}
        
    """ Responsible for Write Message in queue"""
    def write_message(self):
        try:
            filename = '{}.json'.format(self.queue_name)
            
            is_null = lambda field: (str(field) == " ") or (str(field) == "") or (field == None)
            
            if is_null(self.message_body):
                return 'Please Insert Your Message'
            
            build_message_data = self.build_message_body()
            
            with open(filename, 'r') as f:
                data = json.load(f)
            data.append(build_message_data)
            
            
            with open(filename, 'w') as f:
                json.dump(data, f,indent=2)
                
            return "Your Message Insert Successfully in Queue"
        
        except Exception as e:
            return "Message Insert Failed.Please try again"

    """ Responsible for read all message from queue """
    def read_message(self):
        try:
            filename = '{}.json'.format(self.queue_name)
            with open(filename, 'r') as f:
                data = json.load(f)
                return data
        except Exception as e:
            return []


    """ Responsible for delete specific message from queue """
    def delete_message(self):
        try:
            filename = '{}.json'.format(self.queue_name)

            is_null = lambda field: (str(field) == " ") or (str(field) == "") or (field == None)
                
            if is_null(self.message_id):
                return False

            with open(filename, 'r') as f:
                data = json.load(f)
                id_list = []
                if len(data) < 1:
                    sys.stdout.write('Your Queue is Empty'+'\n')
                    return False
                
                for message in data:
                    if message['id'] not in id_list:
                        id_list.append(message['id'])
                
                if self.message_id not in id_list:
                        return False
                
                for message in data:
                    if message['id'] == self.message_id:
                        data.remove(message)
                    
                        
            with open(filename, 'w') as f:
                json.dump(data, f,indent=2)
                return True
                
        except Exception as e:
            return False
                    

        

        
