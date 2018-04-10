# Loveyou.py
A simple MAC changing script made in python.
        
        
***How to use:***

**Step 1. Installing the dependencies**

  You have to install ``click``, you can do that through pip
  ``pip install click`` or ``pip3 install click``, you might need root privileges.
  
  Also ``ifconfig`` is needed, you can check if it is installed by typing ``ifconfig`` in the terminal.
  
  
**Step 2. Downloading**

  You can do this either through curl or git clone, either way works.
  git clone example: ``git clone https://github.com/71ni7e/loveyou/``
                     ``cd loveyou/``


**Step 3. Running the script**

  ``python loveyou.py [MAC address you want to spoof] [Network interface]``
  
  
***Things to keep in mind***

When you restart the box, your MAC address changes back to the original one, you'll have to run the script after every reboot if you want a "permanent" new MAC address.

The Argument interpreting method I use right now (literally none at all) requires you to provide the MAC address in the following format:   ``XX:XX:XX:XX:XX:XX``, formats such as ``XXXXXXXXXXXX`` won't work.

In case you have multiple network adapters, the "Current Address" that is display at the beginning of the script might not be the one of the interface you selected, I'm not going to make the script compare it to the "new" address and parse errors accordingly unless I fix that before. I'm aware of this and working on it.


**Planned stuff**

Argument interpeting so formats with no ``:`` can still work

Making a cython fork of this, for whatever reasons

Fix that multiple interface "feature" (bug)

Random MAC address generator in case no address is provided as sys.argv[1]
