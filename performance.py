import sys
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from markov import identify_speaker

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <max-k> <runs>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, max_k, runs = sys.argv[1:]
    max_k = int(max_k)
    runs = int(runs)

    # TODO: add code here to open files & read text
    f1 = open(filenameA).read()
    f2 = open(filenameB).read()
    f3 = open(filenameC).read()
                            
    # TODO: run performance tests as outlined in README.md
    def elapsed_hash():
        start1 = time.perf_counter()
        tup1 = identify_speaker(f1, f2, f3, max_k, use_hashtable=True)
        elapsed1 = time.perf_counter() - start1 
        return elapsed1

    def elapsed_dict():
        start2 = time.perf_counter()
        tup2 = identify_speaker(f1, f2, f3, max_k, use_hashtable=False)
        elapsed2 = time.perf_counter() - start2
        return elapsed2
    
    # Empty list for the rows in result table
    lst = []
    for i in range(1, runs+1):
        for j in range(1, max_k+1):
            lst.append({"Implementation": "hashtable", "K": j, "Run": i, "Time": elapsed_hash()})

    for i in range(1, runs+1):
        for j in range(1, max_k+1):
            lst.append({"Implementation": "dict", "K": j, "Run": i, "Time": elapsed_dict()})

    # Turn the list into result table
    result_table =  pd.DataFrame(lst)
    print(result_table)

    # Group the plots in result graph by their implementation and K value
    ave_run_times = result_table.groupby(["Implementation", "K"]).mean().reset_index()
    print(ave_run_times)
    

    # TODO: write execution_graph.png  
    result_graph = sns.pointplot(data=ave_run_times, x="K", y="Time", hue="Implementation", linestyle='-', marker='o')
    result_graph.set_title("Hash Table vs Python Dict")
    result_graph.set(xlabel="K", ylabel=f"Average Time (Runs={runs})")
    plt.savefig("execution_graph.png")
        
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          