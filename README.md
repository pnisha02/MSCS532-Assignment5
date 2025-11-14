# MSCS532-Assignment5
# Assignment 5 : Quicksort Algorithm – Implementation, Analysis, and Randomization

## Overview

This project implements two versions of the Quicksort algorithm:

- **Deterministic Quicksort** (fixed pivot)
- **Randomized Quicksort** (random pivot)

The main goal is to compare their performance on different types of input data and understand how pivot selection influences running time.

---

## Project Structure
/Quicksort-Assignment/

├── MSCS 322 Assignment5.docx #Project documentation

├── quicksort.py # Deterministic Quicksort

├── randomized_quicksort.py # Randomized Quicksort

├── compare.py # Runtime comparison script

└── README.md # Documentation

---

## How to Run the Programs

### 1. Run deterministic Quicksort

```bash
python quicksort.py
```

### 2. Run randomized Quicksort 

``` bash
 python randomized_quicksort.py
```
### 3. Run performance comparison

```
python compare.py
```

### This will automatically test both algorithms on:

- **Random Input** 
- **Sorted Input** 
- **Reverse-sorted input**

And print execution times for each.

### Example Output
```
====== n = 5000 ======
random input:
  Deterministic: 0.01241 sec
  Randomized:    0.01103 sec

sorted input:
  Deterministic: 0.09472 sec
  Randomized:    0.01285 sec

reverse input:
  Deterministic: 0.10216 sec
  Randomized:    0.01341 sec
```
### Interpretation:

- Deterministic Quicksort becomes slow on sorted and reverse inputs

- Randomized Quicksort stays consistently fast

### Deterministic vs Randomized Quicksort

| Feature             | Deterministic Quicksort                 | Randomized Quicksort |
| ------------------- | --------------------------------------- | -------------------- |
| Pivot Selection     | Always last element                     | Random element       |
| Worst Case          | When input is sorted or reverse         | Very unlikely        |
| Typical Performance | Good                                    | Excellent            |
| Time Complexity     | Best/Average: O(n log n) / Worst: O(n²) | Expected: O(n log n) |

### Key Design Choices

- Lomuto partition scheme

- Recursion limit increased to support large arrays

- In-place sorting for both algorithms

- Same test sizes used for consistent comparison

### What This Project Demonstrates

- How pivot choice affects performance

- How randomization reduces worst-case behavior

- Why randomized algorithms are more reliable for large datasets

- Practical performance differences between two Quicksort strategies

### References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. Introduction to Algorithms. MIT Press.

- Hoare, C. A. R. (1962). Quicksort. The Computer Journal, 5(1), 10–16.

- GeeksforGeeks. QuickSort Algorithm.
