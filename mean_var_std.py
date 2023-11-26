import numpy as np


def calculate(array):
    if len(array) != 9:
        raise ValueError("List must contain nine numbers.")

    return_dict = {}
    matrix = np.array(array).reshape((3, 3))
    mean_axis0 = np.mean(matrix, axis=0).tolist()
    mean_axis1 = np.mean(matrix, axis=1).tolist()
    mean_axis_flattened = np.mean(matrix, axis=None)

    variance_axis0 = np.var(matrix, axis=0).tolist()
    variance_axis1 = np.var(matrix, axis=1).tolist()
    variance_axis_flattened = np.var(matrix, axis=None)

    std_axis0 = np.std(matrix, axis=0).tolist()
    std_axis1 = np.std(matrix, axis=1).tolist()
    std_axis_flattened = np.std(matrix, axis=None)

    max_axis0 = np.max(matrix, axis=0).tolist()
    max_axis1 = np.max(matrix, axis=1).tolist()
    max_axis_flattened = np.max(matrix, axis=None)

    min_axis0 = np.min(matrix, axis=0).tolist()
    min_axis1 = np.min(matrix, axis=1).tolist()
    min_axis_flattened = np.min(matrix, axis=None)

    sum_axis0 = np.sum(matrix, axis=0).tolist()
    sum_axis1 = np.sum(matrix, axis=1).tolist()
    sum_axis_flattened = np.sum(matrix, axis=None)

    return_dict['mean'] = [mean_axis0, mean_axis1, mean_axis_flattened]
    return_dict['variance'] = [variance_axis0, variance_axis1, variance_axis_flattened]
    return_dict['standard deviation'] = [std_axis0, std_axis1, std_axis_flattened]
    return_dict['max'] = [max_axis0, max_axis1, max_axis_flattened]
    return_dict['min'] = [min_axis0, min_axis1, min_axis_flattened]
    return_dict['sum'] = [sum_axis0, sum_axis1, sum_axis_flattened]
    return return_dict


print(calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))
