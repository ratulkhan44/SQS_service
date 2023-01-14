#Python Imports
import sys

#Project Imports
from handler import MessageHandler


    
""" Responsible for read message from queue.This is wrapper function """
def read_message_from_queue(queue_name = '',delete_message=False):
    try:
        call_message_handler = MessageHandler(queue_name=queue_name)
        messages = call_message_handler.read_message()
        if len(messages) < 1:
            sys.stdout.write('Your Queue is Currently Empty'+'\n')
            return
        for message in messages:
            sys.stdout.write("(Message Id:"+ message.get('id') + "  " + "Message Body:" + message.get('body') +")" +'\n' )
            delete_response = delete_message_in_queue(queue_name = queue_name,id = message.get('id')) if delete_message else False 
            if delete_response:
                sys.stdout.write('After Read Message "{0}" Delete Successfully'.format(message.get('id')) +'\n')
            else:
                sys.stdout.write('Message doesn\'t Delete'+'\n')
            return
    except Exception as e:
        print(e.args[0])
        sys.stdout.write("Something Wrong for read message --")
        

def delete_message_in_queue(queue_name = '',id=''):
    try:
        call_message_handler = MessageHandler(queue_name = queue_name,message_id = id)
        delete_response = call_message_handler.delete_message()
        if delete_response:
                sys.stdout.write( '"{0}" Delete Successfully'.format(id) +'\n')
        else:
            sys.stdout.write('Message doesn\'t Delete'+'\n')
        return
    except Exception as e:
        print(e.args[0])
        sys.stdout.write('Message doesn\'t Delete'+'\n')
        return

""" Using this function you can receieve your message from the queue.Obviously you can pass the queue name and if you delete message then pass delete message True.
    Note: After call this function delete all message from the queue.
    Example : read_message_from_queue(queue_name='test',delete_message=False)
"""

# read_message_from_queue(queue_name='test',delete_message=False)


"""
    You can delete specific message from your queue by passing the message id.
    Example : delete_message_in_queue(queue_name='test',id= '394a931c-5c60-49e7-8af8-610794ebd1')

"""
# delete_message_in_queue(queue_name='test',id= '2dec6bc5-9f26-4365-8128-2a8f072238c7')
