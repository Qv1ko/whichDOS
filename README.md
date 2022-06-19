# MANUAL

__For the script to work correctly:__

  *You have two options when executing the python3 script.*

* Embed the script in an absolute path on your system (you can run the script from any path).

  1. Insert the python3 script in a directory of its absolute path.
  2. Give the script execution permissions (```chmod +x whichDOS.py```).
  3. To run the script, you must type the name of the script and the ip of the target (```whichDOS.py {ip target}```).

  Example: ```whichDOS.py 10.10.10.21```

* Add the script to a not absolute path on your system (you must run the script in the same path where the script is located).

    1. Insert the python3 script into your current directory.
    2. To execute the script, you must type python3, the name of the script and the target ip (```python3 whichDOS.py {ip target}```).

  Example: ```python3 whichDOS.py 10.10.10.21```
 
 __Concepts:__
 
 * whichDOS: Which Default Operating System.
 * TTL: Time To Live. This is the time that the operating system tells the servers how long to store a DNS record in local memory before it is discarded. It can be modified manually. 

> Author: v1c_gm
