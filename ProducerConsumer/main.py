# main.py

import os
import time
import random
import threading
from ITStudent import ITStudent
from XMLHandler import XMLHandler
from Buffer import Buffer

# Global shared buffer
shared_buffer = Buffer()

# Shared directory for XML files
SHARED_DIR = "./shared_directory/"

# Number of items to produce/consume
NUM_ITEMS = 10

def producer():
    print("\n[PRODUCER] Started\n")
    
    for i in range(1, NUM_ITEMS + 1):
        # Create a new student with random data
        student = ITStudent()
        student.generate_random_data()
        
        # Generate filename
        filename = os.path.join(SHARED_DIR, f"student{i}.xml")
        
        # Wrap student data to XML file
        if XMLHandler.wrap_to_xml(student, filename):
            print(f"[PRODUCER] Created {filename}")
            
            # Add file number to buffer
            shared_buffer.produce(i)
            
            # Sleep for a bit to simulate production time
            time.sleep(1)
        else:
            print(f"[PRODUCER] Failed to create {filename}", file=os.sys.stderr)
    
    print(f"\n[PRODUCER] Finished producing {NUM_ITEMS} items\n")

def consumer():
    print("\n[CONSUMER] Started\n")
    
    for i in range(NUM_ITEMS):
        # Get file number from buffer
        file_num = shared_buffer.consume()
        
        # Generate filename
        filename = os.path.join(SHARED_DIR, f"student{file_num}.xml")
        
        print(f"[CONSUMER] Processing {filename}")
        
        # Unwrap XML file to student object
        student = XMLHandler.unwrap_from_xml(filename)
        
        # Display student information
        student.display()
        
        # Delete the XML file after processing
        try:
            os.remove(filename)
            print(f"[CONSUMER] Deleted {filename}")
        except Exception as e:
            print(f"[CONSUMER] Failed to delete {filename}: {e}", file=os.sys.stderr)
        
        # Sleep for a bit to simulate consumption time
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