# server.py

import socket
import time
import random
from ITStudent import ITStudent
from XMLHandler import XMLHandler

PORT = 8080
BUFFER_SIZE = 4096

if __name__ == "__main__":
    random.seed(time.time())
    
    print("========================================")
    print("   SOCKET PRODUCER (SERVER)")
    print("========================================\n")
    
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.listen(1)
    
    print(f"Server listening on port {PORT}...")
    print("Waiting for consumer to connect...\n")
    
    # Accept connection
    client_socket, addr = server_socket.accept()
    print("Consumer connected!")
    print("Starting to produce student data...\n")
    
    # Produce and send 10 students
    for i in range(1, 11):
        # Generate random student
        student = ITStudent()
        student.generate_random_data()
        
        print(f"[PRODUCER] Generating student {i}")
        
        # Convert to XML
        xml_data = XMLHandler.generate_xml_string(student)
        
        # Send XML data length first
        data_length = len(xml_data)
        client_socket.send(data_length.to_bytes(4, "big"))
        
        # Send XML data
        client_socket.send(xml_data.encode("utf-8"))
        
        print(f"[PRODUCER] Sent student {i} data ({data_length} bytes)")
        
        time.sleep(2)  # Simulate production delay
    
    print(f"\n[PRODUCER] Finished sending all 10 students")
    
    # Send termination signal
    termination_signal = -1
    client_socket.send(termination_signal.to_bytes(4, "big", signed=True))
    
    print("Closing connection...")
    
    # Close sockets
    client_socket.close()
    server_socket.close()
    
    print("\n========================================")
    print("   Server completed successfully!")
    print("========================================\n")