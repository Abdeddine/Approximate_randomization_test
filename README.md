# Approximated_randomization_test

This is a Python implementation of the Approximated Randomization Test, which can be used to compare multiple samples or multiple models to a main sample. All data sampling should have the same size and be written in one file.

# Usage
Clone this repository and navigate to the project directory.
Prepare your data file according to the format specified below.
Execute the code by running the following command in your terminal:
```bash
python approximated_randomization.py
```
Follow the prompts and enter the requested information. An example execution is provided below.
# Data Format
For comparing multiple samples, the data should be formatted as follows:

```
sample1 = [ [x,x,x,x,x], [x,x,x,x,x], ... ]
sample2 = [ [x,x,x,x,x], [x,x,x,x,x], ... ]
...
```
For comparing single model, the data should be formatted as follows:

```
sample1 = [x,x,x,x,x]
sample2 = [x,x,x,x,x]
...
```

# Example Execution

```bash
Enter filename: General.txt
Are you comparing multiple models? (y/n): y
You will get the p-values as a plot

Enter the list of index of the models to put as x axis (separated with space): 1 2 3 4 5
Enter the title of the plot: AR_test
Are you comparing multiple algorithms to one? (y/n): y
Enter the main sample you want to compare: A
Enter samples names (separated with space): B C D
Enter the number of null hypothesis sample: 1000
```
# Plotting
If you are comparing multiple models, the code will plot the p-values and save the plot in the "Plotting" repository.
## Contact
For any questions or feedback, please feel free to reach out to us at Abderrafiabdeddine@gmail.com.
