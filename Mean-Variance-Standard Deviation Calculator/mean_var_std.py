import numpy as np
""""Create a function named calculate() in mean_var_std.py
that uses Numpy to output the mean, variance,
standard deviation, max, min, and sum of the rows,
columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits."""


def calculate(list):
    """The function should convert the list into a 3 x 3
    Numpy array, and then return a dictionary containing the mean,
    variance, standard deviation, max, min, and sum along both axes
    and for the flattened matrix."""
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list).reshape(3, 3)
    output = {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)],
        'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)],
        'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)],
        'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), max(np.max(arr, axis=1))],
        'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), min(np.min(arr, axis=1))],
        'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), sum(np.sum(arr, axis=1))]
    }
    return output
