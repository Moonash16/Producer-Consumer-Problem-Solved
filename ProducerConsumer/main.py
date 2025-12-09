# main.py

import os
import time
import random
import threading
from ITStudent import ITStudent
from XMLHandler import XMLHandler
from Buffer import Buffer

# the Global shared buffer
shared_buffer = Buffer()

# Sharing directory for XML files
SHARED_DIR = "./shared_directory/"

# number of items to produce/consume/ITstudents
NUM_ITEMS = 10

def producer():
    print("\n[PRODUCER] Started\n")
    
    for i in range(1, NUM_ITEMS + 1):
        # Creating a new student with random data
        student = ITStudent()
        student.generate_random_data()
        
        # Generating the filename
        filename = os.path.join(SHARED_DIR, f"student{i}.xml")
        
        # Wrapping the student data into XML file
        if XMLHandler.wrap_to_xml(student, filename):
            print(f"[PRODUCER] Created {filename}")
            
            # Adding file number to our buffer
            shared_buffer.produce(i)
            
            # Sleeping for a bit to simulate production time...for a bit
            time.sleep(1)
        else:
            print(f"[PRODUCER] Failed to create {filename}", file=os.sys.stderr)
    
    print(f"\n[PRODUCER] Finished producing {NUM_ITEMS} items\n")

def consumer():
    print("\n[CONSUMER] Started\n")
    
    for i in range(NUM_ITEMS):
        # Getting our file number from buffer
        file_num = shared_buffer.consume()
        
        # again generating filename
        filename = os.path.join(SHARED_DIR, f"student{file_num}.xml")
        
        print(f"[CONSUMER] Processing {filename}")
        
        # Unwrapping the XML file to student object
        student = XMLHandler.unwrap_from_xml(filename)
        
        # Displaying our student information
        student.display()
        
        # Deleting the XML file after processing
        try:
            os.remove(filename)
            print(f"[CONSUMER] Deleted {filename}")
        except Exception as e:
            print(f"[CONSUMER] Failed to delete {filename}: {e}", file=os.sys.stderr)
        
        # Sleep for a bit to simulate consumption time now not production
        time.sleep(1)
    
    print(f"\n[CONSUMER] Finished consuming {NUM_ITEMS} items\n")

if __name__ == "__main__":
    random.seed(time.time())
    
    print("========================================")
    print("   PRODUCER-CONSUMER PROBLEM")
    print("   CSC411 - Mini Project")
    print("========================================\n")
    
    # Create shared directory if it doesn't exist
    os.makedirs(SHARED_DIR, exist_ok=True)
    
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    print("Creating threads...\n")
    
    # Start threads
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for threads to complete
    producer_thread.join()
    consumer_thread.join()
    
    print("\n========================================")
    print("   All threads completed successfully!")

    print("========================================\n")
    
