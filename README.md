# pmldl-assignment-2
Repository for PMLDL course Assignment 2 by Ivan Chernakov BS21-DS-02 Student

Author:
- Ivan Chernakov
- BS21-DS-02
- i.chernakov@innopolis.university

## Requirements
Run the following command to install all the required packages:
```pip install -r requirements.txt``` if needed.

## Benchmark
To run the benchmark, run the following command:
```python benchmark/evaluate.py```

You also can specify the partition of [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/)
by adding 'ua.test' or 'ua.base' to the command:
```python benchmark/evaluate.py ua.test ua.base```, where **a** is a partition number (1-5).


## Structure
```
text-detoxification
├── README.md # The top-level README
│
├── requirements.txt # The requirements file for reproducing the analysis environment
│
├── benchmark
│   └── evaluate.py      # Script for evaluation of the model.
│
├── data 
│   └── raw      # The original, immutable data.
│
├── models       # Trained and serialized models, model predictions, or model summaries (LFS limited) 
│
├── notebooks    #  Jupyter notebooks.  
│   ├── 1.0-data-exploration.ipynb
│   ├── 2.0-alternating-least-squares.ipynb
│   └── 3.0-KNN.ipynb   
│ 
├── references # Data dictionaries, manuals, and all other explanatory materials.
│
└── reports
    ├── figures  # Generated graphics and figures to be used in reporting
    └── final-solution.md # The final solution report
```
