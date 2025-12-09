# Producer-Consumer-Problem-Solved

So our software package serves the purpose of implementing the classic producer consumer problem using a shared buffer.

THE PRODUCER
So what the producer does is to generate random IT student data inclusive of a Name, 8 digit ID, Programme, Courses and Marks, then wraps it into XML files. It then pushes the corresponding file number into a shared buffer.

THE CONSUMER 
The consumer then reads and unwraps the XML files, reconstructs the IT Student object, deletes the processsed file and removes the matching integer from the buffer. It then goes on to compute the student's average mark and determine th epass or fail status before printing the full student details.

THE BUFFER
Then bounded buffer that has a maxsize of 10 ensures proper synchronization where:
      -The producer waits when the buffer is full
      -The consumer waits when the buffer is empty
      -Mutual exclusion is enforced for all buffer operations

      
