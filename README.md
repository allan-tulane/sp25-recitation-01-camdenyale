[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tqM-lrvp)
# CMPS 2200  Recitation 01

**Name (Team Member 1):**Camden Yale 
**Name (Team Member 2):**Emily Aymond

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

Worst case input value of key for the linear search algorithm is if the key is not in the list at all, or if the key is the very last element in the list. The algorithm will search through every element one by one and will only conclude at the very end of the list. The worst case input value for the binary search algorithm is if the key is not in the list at all, or if the key continues to cause division until the smallest possible range. Similar to the linear search algorithm, it will have to iterate through all elements and will finally find the key in the last possible range, causing a longer runtime. 

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

The best case input value of a key for the linear search algorithm is if the key is the first element in the list. The algorithm would only need to search one element and then could immedietly return the value without having to search any others. The best case input value of a key for the binary search algorithm is if the key is in the exact middle of the list. This is the first element searched in a list so it will not have to do any division or search any other element.

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

|            n |   linear |   binary |
|--------------|----------|----------|
|       10.000 |    0.003 |    0.004 |
|      100.000 |    0.005 |    0.002 |
|     1000.000 |    0.064 |    0.003 |
|    10000.000 |    0.403 |    0.003 |
|   100000.000 |    4.517 |    0.010 |
|  1000000.000 |   43.919 |    0.013 |
| 10000000.000 |  483.743 |    0.015 |

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

For linear search, as the size of n input increases, the time taken for linear search to complete should increase linearly. For input size n = 10, linear time is 0.003, when n increases to 100, linear time increases to 0.005. This continues for the rest of our linear search values, showing that our empirical results match the theoretical running times for linear search. For binary search, as n increases, binary search should increase logarithmically. From our values, we see that the binary search is signficantly less than our linear search values and increases very slow as the n input increases. For example, the binary search from 1000 and 10000 is the same. Both of our theoretical running times are supported by the results in our table.

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? 
  The worst case complexity for searching a list of $n$ elements $k$ times using linear search is $\Theta(k * n)$ or $\Theta(kn)$. This is because each search takes $\Theta(n)$ time, if you perform $k$ searches on the list, each requiring $\Theta(n)$ time, the total is $\Theta(k * n)$
  + For binary search?
      + Binary search requires $\Theta(log n)$ for each search assuming that the list is sorted. If you perform $k$ searches on the list, each requiring $\Theta(log n)$ time, the total time for $k$ searches is $\Theta(k * log n)$. However if the list is not sorted, you must include the $\Theta(n^2)$. Giving the final result of, $\Theta(n^2 + k * log n)$ 
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting?
      + For binary search to be more efficient, this must be true: $\Theta(n^2 + k * log n)$ < $\Theta(k * n)$. For large values of $k$, binary search with sorting would be better because $\Theta(n^2)$ will dominate for small values of $k$. If $k$ is really small, it might be better to use linear because the sorting time of $\Theta(n^2)$ costs a lot. 
