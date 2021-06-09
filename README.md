# CharismaIBSCalculator

There were certain steps to this code, all expalained below. Please have in mind that the codes are not optimized and I am not sure if they work in long-term run.

Note 1: Name of repository may change or the whole repository may be deleted.

Note 2: This was the test task of Charisma Group Interview. But it may not stay at this stage.

Note 3: I am not good at web developmenment (specially at front-end). So, I am sorry if things are way too ugly. :)

First of all, to run the codes, copy all the files in one directory and follow the instructions.
1. The text file "code-name-industry.csv" is the reference file needed for parts of the code. Therefore it should not modified.
2. In case "code-name-industry.csv" was tampered or damaged, run "CharismaCodeLabeler.py and wait for it to finish working before running the other parts of the program.
3. The file "CharismaCollector.py" is the data fetcher of the project. I have used packages "request", "pandas", "numpy", and "datetime" to get data and clean them. No need to run this file directly. It has 4 functions, 3 of which are for test and main function is "collector" method.
4. There are two ways of monitoring the data: 1) with Jupyter notebook. 2) with Dash and simple JS code.
5. To use Jupyter, all you need to do is open "CharismaJupyterChart" and run the cells one by one. I say one by one because you will need to fill one or two fields.
6. To use Dash, simply run "CharismaLiveGraph.py" and enter the two fields.
7. There is one more file named "CharismaTkinterUI.py" which is my failed attempt to make a simple User Interface for the code. I made the requested boxes in a frame but I failed to pass the values and call the required functions.

Note 4: The codes contain very few comments. Please contact me for more details.
Note 5: I added a screenshot of what should the result look like. The reason for straight line is that I tested the code on market close time. 
