# portScanner-Server

This is a simple repo that contains (2) items; a java server and a python port scanner.

Code Followed: https://www.youtube.com/watch?v=FGdiSJakIS4&t=2667s by freeCodeCamp.org

<details>
  <summary><b>Server</b></summary>
The server is run by java using java.net and java.io. After creating a socket object, it actively listens on port 8888 and sends a message upon proper handling of messages. If an exception occurs, the server will close and print "An error has occured!"
</details>

<details>
   <summary><b>portScanner</b></summary>
This portScanner is directly taken from the source referenced above. It is an entry-level project to socket programming and multi-threading. Instead of sequentially scanning each port, multi-threading allows you to perform multiple exeuctions at the same time. This can greatly reduce time wait and allow responsive systems. In this code, we create a worker thread of ~1000 and a queue that holds 1 - 8888 ports inclusively. Iterating through each 1000 ports, each thread calls portScan(port) and returns true if an opening has been found.
</details>
