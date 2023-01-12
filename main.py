from generate_queue import QueueHandler
from handler import MessageHandler
import os,sys
import pathlib,json
def create_queue(queue_name = ''):
    try:
        call_queue_handler = QueueHandler(queue_name)
        response_from_queue_handler = call_queue_handler.generate_queue()
        return response_from_queue_handler
    except Exception as e:
        return response_from_queue_handler
    

def read_message_from_queue(queue_name = ''):
    try:
        call_message_handler = MessageHandler(queue_name=queue_name)
        messages = call_message_handler.read_message()
        print(type(messages))
        for message in messages:
            print('sasas',message.get('body'))
        return messages
    except Exception as e:
        print(e)
        
def write_message_in_queue(queue_name = '',message=''):
    try:
        call_message_handler = MessageHandler(queue_name = queue_name,message_body = message)
        message_response = call_message_handler.write_message()
        return message_response
    except Exception as e:
        exception_message = str(e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(
            exception_traceback.tb_frame.f_code.co_filename)[1]
        print('Raised error due to ' +
              (f"An Exception Occured. \n Exception Type: {str(exception_type)}. Arguments: [{exception_message}]. File Name: {filename}, Line no: {exception_traceback.tb_lineno}"))
        return message_response


print(read_message_from_queue(queue_name='test'))
# print(create_queue(queue_name='test'))
# print(write_message_in_queue(queue_name='test',message ='Hello One'))
