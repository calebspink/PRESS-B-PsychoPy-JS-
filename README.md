PRESS-B: PsychoPy/JS Version
Written by Caleb Spink, B.S.

For questions or concerns, please send me an email at css0121@auburn.edu

PRESS-B.psyexp is a PsychoPy experiment that can run in both Python and JavaScript for in-person and remote sessions, respectively.

Task Analyses:
Installing PsychoPy: https://www.psychopy.org/download.html
Forking experiments on Pavlovia: https://pavlovia.org/docs/experiments/create-fork 

Using PRESS-B:
1. Open the PsychoPy Builder
*If the Runner or Coder are opened instead, click the cube in the "Views" section of the screen
2. Go to File -> Open -> PRESS-B.psyexp
3. If an error message pops-up, exit out of it. I designed it in a manner where I had to override a lot of the JS in order to make it work. Welcome, Trial, and Goodbye are required for the experiment to run and are active.
4. To add a routine, click "Insert Routine" and select the routine you would like to add. Place it where you want it to go. You can remove a routine by right-clicking it and selecting "remove". Do not remove routines deleting the routine code (i.e., clicking 'x' under "routines").
5. The order of trials can be set via the "Selection_type" loop. By default it will run trials set in the CSV sequentially and once. To randomize the order, click "Selection_type" loop and select "random".
You may have a trial block repeat by setting "Num. repeats" to a value greater than 1. 
6. Run (green) or pilot (orange) the experiment by toggling it. The Python version should now work. If it does not run, there is likely an issue with the CSV file. Do not hesitate to contact me for help troubleshooting!
JavaScript Only Steps:
8. Upload all files via the gear button (i.e., settings) -> Online -> and adding documents and stimuli to the "Additional resources" list. If you change something in the CSV, you need to reupload it.
9. If you change any code, make the code compile by clicking the yellow square labeled "JS". To test the experiment, set it to pilot mode and click the orange arrow above the "Browser" section of the screen. The project needs to be synced in order to run participants online. For debugging messages, right-click the screen while the experiment is running and click "Inspect". Reload the experiment with ctrl + r to refresh the resources.

Known Issues:
1. Not everything is in JS
2. Use of the JS version periodically requires running "netstat -ano | findstr :[value]" and "taskkill /PID [digit] /F" to clear the port. I need to make it so the port is cleared upon termination of the experiment.
3. Find out how to connect Pavlovia to Sona
4. Tutorial sequences aren't in JS yet
5. Presses that would be associated with reinforcement outside of a changeover delay is marked as a '1' rather than a '0'.

Future Plans:
1. Fix issues
2. Add more features (suggestions welcome!)
