

@tf_export('batch_to_space', v1=[])
def batch_to_space_v2(input, block_shape, crops, name=None):
    'BatchToSpace for N-D tensors of type T.\n\n  This operation reshapes the "batch" dimension 0 into `M + 1` dimensions of\n  shape `block_shape + [batch]`, interleaves these blocks back into the grid\n  defined by the spatial dimensions `[1, ..., M]`, to obtain a result with the\n  same rank as the input.  The spatial dimensions of this intermediate result\n  are then optionally cropped according to `crops` to produce the output.  This\n  is the reverse of SpaceToBatch.  See below for a precise description.\n\n  Args:\n    input: A `Tensor`. N-D with shape `input_shape = [batch] + spatial_shape +\n      remaining_shape`, where spatial_shape has M dimensions.\n    block_shape: A `Tensor`. Must be one of the following types: `int32`,\n      `int64`. 1-D with shape `[M]`, all values must be >= 1. For backwards\n      compatibility with TF 1.0, this parameter may be an int, in which case it\n      is converted to `numpy.array([block_shape, block_shape],\n      dtype=numpy.int64)`.\n    crops: A `Tensor`. Must be one of the following types: `int32`, `int64`. 2-D\n      with shape `[M, 2]`, all values must be >= 0. `crops[i] = [crop_start,\n      crop_end]` specifies the amount to crop from input dimension `i + 1`,\n      which corresponds to spatial dimension `i`.  It is required that\n      `crop_start[i] + crop_end[i] <= block_shape[i] * input_shape[i + 1]`.\n      This operation is equivalent to the following steps:\n      1. Reshape `input` to `reshaped` of shape: [block_shape[0], ...,\n        block_shape[M-1], batch / prod(block_shape), input_shape[1], ...,\n        input_shape[N-1]]  \n      2. Permute dimensions of `reshaped` to produce `permuted` of shape \n         [batch / prod(block_shape),  input_shape[1], block_shape[0], ..., \n         input_shape[M], block_shape[M-1], input_shape[M+1],\n        ..., input_shape[N-1]]  \n      3. Reshape `permuted` to produce `reshaped_permuted` of shape \n         [batch / prod(block_shape), input_shape[1] * block_shape[0], ..., \n         input_shape[M] * block_shape[M-1], input_shape[M+1], ..., \n         input_shape[N-1]]  \n      4. Crop the start and end of dimensions `[1, ..., M]` of `reshaped_permuted` \n         according to `crops` to produce the output of shape: \n         [batch / prod(block_shape),  input_shape[1] *\n           block_shape[0] - crops[0,0] - crops[0,1], ..., input_shape[M] *\n           block_shape[M-1] - crops[M-1,0] - crops[M-1,1],  input_shape[M+1],\n           ..., input_shape[N-1]]\n      Some examples:  (1) For the following input of shape `[4, 1, 1, 1]`,\n          `block_shape = [2, 2]`, and `crops = [[0, 0], [0, 0]]`:  ``` [[[[1]]],\n            [[[2]]], [[[3]]], [[[4]]]] ```\n      The output tensor has shape `[1, 2, 2, 1]` and value:  ``` x = [[[[1],\n        [2]], [[3], [4]]]] ```  (2) For the following input of shape `[4, 1, 1,\n        3]`,\n          `block_shape = [2, 2]`, and `crops = [[0, 0], [0, 0]]`:  ``` [[[1, 2,\n            3]], [[4, 5, 6]], [[7, 8, 9]], [[10, 11, 12]]] ```\n      The output tensor has shape `[1, 2, 2, 3]` and value:  ``` x = [[[[1, 2,\n        3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]] ```  (3) For the following\n        input of shape `[4, 2, 2, 1]`,\n          `block_shape = [2, 2]`, and `crops = [[0, 0], [0, 0]]`:  ``` x =\n            [[[[1], [3]], [[9], [11]]], [[[2], [4]], [[10], [12]]], [[[5], [7]],\n            [[13], [15]]], [[[6], [8]], [[14], [16]]]] ```\n      The output tensor has shape `[1, 4, 4, 1]` and value:  ``` x = [[[1], [2],\n        [3],  [4]], [[5],   [6],  [7],  [8]], [[9],  [10], [11],  [12]], [[13],\n        [14], [15],  [16]]] ```  (4) For the following input of shape `[8, 1, 3,\n        1]`,\n          `block_shape = [2, 2]`, and `crops = [[0, 0], [2, 0]]`:  ``` x =\n            [[[[0], [1], [3]]], [[[0], [9], [11]]], [[[0], [2], [4]]], [[[0],\n            [10], [12]]], [[[0], [5], [7]]], [[[0], [13], [15]]], [[[0], [6],\n            [8]]], [[[0], [14], [16]]]] ```\n      The output tensor has shape `[2, 2, 4, 1]` and value:  ``` x = [[[[1],\n        [2],  [3],  [4]], [[5],   [6],  [7],  [8]]], [[[9],  [10], [11],  [12]],\n        [[13], [14], [15],  [16]]]] ```\n    name: A name for the operation (optional).\n\n  Returns:\n    A `Tensor`. Has the same type as `input`.\n  '
    if isinstance(block_shape, int):
        block_shape = np.array([block_shape, block_shape], dtype=np.int64)
    return batch_to_space_nd(input=input, block_shape=block_shape, crops=crops, name=name)