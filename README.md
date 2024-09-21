Overview

This Python script is designed to help keep your programming skills sharp by regularly presenting you 
with a programming-related URL more often than not. The script runs on startup, waits for 5 
minutes (configurable), and then has a configurable chance of opening a random URL from a list of URLs 
that you provide. These URLs can point to programming challenges, tutorials, or any resources you believe 
will help improve your coding skills.

The script works best if you set it and forget it, allowing it to run in the background each time your 
computer starts. Over time, it will help you stay engaged with programming challenges without you having 
to actively remember to visit programming resources.

Note: This python file has been saved as .pyw to be able to run without the console popping up.

How It Works

- The script generates a random number between 0 and 100.
- If the number is less than or equal to a user-configured percentchance, a random URL is selected from 
    the randomquestions.txt file and opened in your preferred web browser.
- If the number is greater than percentchance, the script ends with no action.


Running the Script at Startup

To ensure the script runs every time you start your computer, follow these steps:
1. Navigate to the folder where your script (startup_script.pyw) is located.
2. Right-click the script and choose Create shortcut.
3. Press Win + R to open the Run dialog.
4. Type shell:startup and hit Enter. This opens the Windows Startup folder.
5. Drag and drop the shortcut you created into this folder.

The next time you restart your computer, the script will automatically execute after the delay you’ve 
configured.


Configuration

Setting the Percent Chance

The variable percentchance controls how likely it is for the script to open a URL. 
The default is set to 50, meaning there is a 80% chance of opening a URL every time the script runs.

To adjust this:
1. Open the script file (startup_script.py) in a text editor or code editor of your choice.
2. Locate the line:
    percentchance = 80  # Example: 80% chance
3. Change the number 80 to any value between 0 and 100. This value represents the percentage likelihood 
    of opening a URL.

Customizing the Delay Time

By default, the script waits for 5 minutes (300 seconds) before checking whether to open a URL to give 
time for startup. You can customize this delay to suit your needs.

To change the delay:
1. Open the script file (startup_script.py) in a text editor.
2. Locate the line:
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
3. Change 300 to the desired number of seconds

Providing URLs

You are responsible for populating the randomquestions.txt file with URLs. The script will randomly 
select from this list when opening a URL.

Steps:
1. Create a text file named randomquestions.txt in the same folder as the script.
2. Add one URL per line.
3. Save the file
