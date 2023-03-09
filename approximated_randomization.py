import random
import os
import matplotlib.pyplot as plt

# FigureCanvasQT.required_interactive_framwork = "qt5"

def average_difference(algo1,algo2):

    number_of_samples = len(algo1)
    average_difference = abs( (sum(algo1) / number_of_samples) - (sum(algo2)/number_of_samples) )

    return average_difference

def single_ar(algo1,algo2):

    number_of_samples = len(algo1)
    new_list_of_samples = algo1 + algo2
    random.shuffle(new_list_of_samples)
    new_algo1 = new_list_of_samples[:number_of_samples]
    new_algo2 = new_list_of_samples[number_of_samples:]

    return average_difference(new_algo1,new_algo2)

def plot_pvalues(p_value_algorithms, index, names, models, title):

    folderPath = "/home/abderrafi.abdeddine/Coverage_Aware/Simulations results/Random/reploting/"

    _, ax = plt.subplots()
    ax.fill_between(index, 0, 0.001, color='#00FF00', alpha=0.5, label='***')
    ax.fill_between(index, 0.001, 0.01, color='#339933', alpha=0.5, label='**')
    ax.fill_between(index, 0.01, 0.05, color='darkgreen', alpha=0.5, label='*')
    ax.fill_between(index, 0.05, 1, color='red', alpha=0.5, label='=')
    plt.semilogy()

    for i in range(len(p_value_algorithms)):
        plt.plot(index,p_value_algorithms[i], linestyle= 'None', marker = 'o', label=names[1:][i])

    plt.xlabel(models)
    plt.ylabel('p-values (th = 0.05)')
    plt.title(title)
    plt.grid()
    plt.legend()

    # name = os.path.join(folderPath, "AR test of the sample "+ names[0] +" to other samples.png")
    name = os.path.join("Plotting","AR test of the sample "+ names[0] +" to other samples.png")
    plt.savefig(name)
    plt.close()

def AR_test(f1, index, algorithms_names, null_distribution_length,models,title):

    algorithms_results = [[] for _ in algorithms_names]
    f = open(f1, 'r')
    for line in f:
        line = line.replace(" ","")
        line = line.replace("\n","")
        line = line.replace("[[","")
        line = line.replace("]]","")
        splited_line = line.split("=")
        if splited_line[0] in algorithms_names:
            algorithm_result = splited_line[1].split("],[")
            if len(algorithm_result) == 1 :
                algorithm_result = algorithm_result[0]
                algorithm_result = algorithm_result.replace("[","")
                algorithm_result = algorithm_result.replace("]","")
                algorithm_result = [algorithm_result]
            # the index of the algorithm
            algorithms_index =  algorithms_names.index(splited_line[0])
            # insert the algorithm result into the list 

            algorithms_results[algorithms_index] += [[float(x) for x in algorithm_result[i].split(",") ] for i in range(len(models))]

    f.close()
    algorithms_ave_diff_tasks = [ [ [average_difference(algorithms_results[0][j],algorithms_results[i][j])] for j in range(len(algorithms_results[0])) ] for i in range(1,len(algorithms_results)) ]
    algorithms_p_value_tasks = [ [ 0 for j in range(len(algorithms_results[0]))] for i in range(1,len(algorithms_results))]
    

    
    for t in range(null_distribution_length):
        for i in range(len(algorithms_results)-1):
            for j in range(len(algorithms_results[0])):
                algorithms_ave_diff_tasks[i][j].append(single_ar(algorithms_results[0][j], algorithms_results[i+1][j]))
                if algorithms_ave_diff_tasks[i][j][0] <= algorithms_ave_diff_tasks[i][j][-1]:
                    algorithms_p_value_tasks[i][j] += 1/null_distribution_length
    
    if len(algorithms_p_value_tasks) != 0 and len(algorithms_p_value_tasks[0]):
        if len(algorithms_p_value_tasks) == 1:
            print("The p-value resulting from the comparison between ", algorithms_names[0], " and ",algorithms_names[1]," is ", algorithms_p_value_tasks[0][0])
        else:
            print("The p-values resulting from the comparison between")
            for index_algorithm_name in range(1,len(algorithms_names)):

                print(algorithms_names[0], " and ",algorithms_names[index_algorithm_name],": ", algorithms_p_value_tasks[index_algorithm_name-1][0])
    else:
        plot_pvalues(algorithms_p_value_tasks, index, algorithms_names,models,title)



if __name__ == "__main__":
    # User inputs filename
    filename = input("Enter filename: ")
    bool = input("Are you camparing multiple models? (y/n): ")
    if bool =='y':
        print("You will get the p-values as a plot.")
        user_list = input("Enter the list of index of the models to put as x axis (separated with space): ")
        index_string = user_list.split()
        index = [int(_) for _ in index_string]
        title = input("Enter the title of the plot: ")
    else: 
        index = [1]
        title = ""
    bool = input("Are you comparing multiple algorithms to one? (y/n): ")
    if bool == 'y':
        main_sample = input("Enter the main sample you want to compare: ")
        user_samples = input("Enter samples names (separated with space): ")
        samples = user_samples.split()
        algorithms_names = [main_sample]+samples
    else:
        samples = input("Enter samples names (separated with space): ")
        algorithms_names = samples.split()
    nmb = int(input("Enter the number of null hypothesis sample: " ))
    # Ensure it's a string
    if not filename.isalpha():
        filename = str(filename)

    AR_test(filename, index, algorithms_names, nmb ,index, title)
