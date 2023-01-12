import json
import uuid
import os,sys
class MessageHandler:
    def __init__(self,queue_name = '',message_body='') -> None:
        self.queue_name = queue_name
        self.message_body = message_body
        
    def generate_uuid(self):
        try:
            get_uuid = uuid.uuid4()
            return str(get_uuid)
        except:
            return None
        
    def read_message(self):
        try:
            filename = '{}.json'.format(self.queue_name)
            with open(filename, 'r') as f:
                data = json.load(f)
                if len(data) < 1:
                    return 'Your Queue is Currently Empty'
                print(type(data))
                return data
        except Exception as e:
            print(e)
            return 'SomeThing Wrong For Read Message'
    
    def build_message_body(self):
        try:
            data = {}
            data['id'] = self.generate_uuid() if self.generate_uuid() else uuid.uuid4()
            data['body'] = self.message_body
            return data
        
        except Exception as e:
            print(e.args[0])
            return {}
        
            
    def write_message(self):
        try:
            filename = '{}.json'.format(self.queue_name)
            
            is_null = lambda field: (str(field) == " ") or (str(field) == "") or (field == None)
            
            if is_null(self.message_body):
                return 'Please Insert Your Message'
            
            build_message_data = self.build_message_body()
            print(build_message_data)
            
            with open(filename, 'r') as f:
                data = json.load(f)
            data.append(build_message_data)
            
            print(data)
            
            with open(filename, 'w') as f:
                json.dump(data, f,indent=2)
                
            return "Your Message Insert Successfully in Queue"
        
        except Exception as e:
            exception_message = str(e)
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = os.path.split(
                exception_traceback.tb_frame.f_code.co_filename)[1]
            print('Raised error due to ' +
                (f"An Exception Occured. \n Exception Type: {str(exception_type)}. Arguments: [{exception_message}]. File Name: {filename}, Line no: {exception_traceback.tb_lineno}"))
            return "Message Insert Failed.Please try again"
