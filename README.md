# Project Title

This is Simple Queue Service(SQS) based on FIFO Cencept that means First In First Out.Here You can create your own Message Queue,send your message in your own queue and also recieve and read message and delete message.
## Requirements:
- Python 3.8 (tested python 3.8)





## Features

- Create Your Own Message Queue
- Send Message and Store Message in your Queue
- Receive and read Message from Queue
- Delete Message After Read Message
- Specific Message delete from your Queue




## Installation

Install Python 3.8
- Firstly You need to Create Your Own Queue.So go to ```queue_manager.py``` file.
- Call ```create_queue``` function with provide ```queue_name``` parameter
- After Create Queue call ```write_message_in_queue``` function  with provide ```queue_name``` and ```message``` parameter. 
- Then go to ```main.py``` file .
- Call ```read_message_from_queue``` function with provide ```queue_name``` ans ``` delete_message ```.You can see your all message by calling this function and if you set ```delete_message = True```, after read your message delete form the queue.

    