# client.py

import socket
from ITStudent import ITStudent
from XMLHandler import XMLHandler

PORT = 8080
BUFFER_SIZE = 4096

if __name__ == "__main__":
    print("========================================")
    print("   SOCKET CONSUMER (CLIENT)")
    print("========================================\n")
    
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", PORT))
    
    print("Connected to producer!")
    print("Waiting to receive student data...\n")
    
    student_count = 0
    
    # Receive and process students
    while True:
        # Receive data length
        data_length_bytes = client_socket.recv(4)
        if not data_length_bytes:
            print("\nConnection closed by server")
            break
        
        data_length = int.from_bytes(data_length_bytes, "big", signed=True)
        
        # Check for termination signal
        if data_length == -1:
            print("\nReceived termination signal")
            break
        
        # Receive XML data
        xml_data = b""
        while len(xml_data) < data_length:
            packet = client_socket.recv(data_length - len(xml_data))
            if not packet:
                raise Exception("Connection closed prematurely")
            xml_data += packet
        
        xml_str = xml_data.decode("utf-8")
        
        student_count += 1
        print(f"[CONSUMER] Received student {student_count} data ({data_length} bytes)")
        
        # Parse XML to student object
        student = XMLHandler.parse_xml_string(xml_str)
        
        # Display student information
        student.display()
    
    print(f"\n[CONSUMER] Processed {student_count} students")
    
    # Close socket
    client_socket.close()
    
    print("\n========================================")
    print("   Client completed successfully!")
    print("========================================\n")