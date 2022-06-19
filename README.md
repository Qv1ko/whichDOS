# MANUAL

__For the script to work correctly:__

  *You have two options when executing the python3 script.*

* Insert the script into an absolute path on your system (you can run the script from any other path).

  1. Insert the python3 script into a directory in your absolute path.
  2. Give execute permissions to the script (`chmod +x whichDOS.py`).
  3. To execute the script, you have to type the name of the script and the target ip (`whichDOS.py {target ip}`).

  Example: `whichDOS.py 10.10.10.21`

* Adding the script to a non-absolute path on your system (you must run the script in the same path where the script is located).

    1. Insert the python3 script into your current directory.
    2. To run the script, you must type python3, the name of the script and the target ip (`python3 whichDOS.py {ip target}`).

  Example: `python3 whichDOS.py 10.10.10.21`
 
 __Concepts:__
 
 * whichDOS: Which Default Operating System.
 * TTL: Time To Live. It is the time that the operating system tells the servers to store a DNS record in local memory before it is discarded. It can be modified manually.

> Author: v1c_gm
