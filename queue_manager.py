#Python Imports
import sys

#Project imports
from generate_queue import QueueHandler
from handler import MessageHandler

""" Responsible for Create Queue.This is a wrapper function """
def create_queue(queue_name = ''):
    try:
        call_queue_handler = QueueHandler(queue_name)
        response_from_queue_handler = call_queue_handler.generate_queue()
        sys.stdout.write(response_from_queue_handler+'\n')
    except Exception as e:
        sys.stdout.write(response_from_queue_handler+'\n')

""" Responsible for Write message in Queue.This is a wrapper function """
def write_message_in_queue(queue_name = '',message=''):
    try:
        call_message_handler = MessageHandler(queue_name = queue_name,message_body = message)
        message_response = call_message_handler.write_message()
        sys.stdout.write(message_response+'\n')
    except Exception as e:
        sys.stdout.write(message_response+'\n')

"""
    Create Your queue by using this function with passing queue name
    create_queue(queue_name='test')

"""
# create_queue(queue_name='test')




"""
    Write message in  Your queue by using this function with passing queue name & message
    write_message_in_queue(queue_name='test',message ='Hello World')

"""

# write_message_in_queue(queue_name='test',message ='Hello World')