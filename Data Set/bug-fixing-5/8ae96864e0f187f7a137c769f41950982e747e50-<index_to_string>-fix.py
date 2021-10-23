@deprecated('2017-01-07', 'This op will be removed after the deprecation date. Please switch to index_to_string_table_from_tensor and call the lookup method of the returned table.')
def index_to_string(tensor, mapping, default_value='UNK', name=None):
    'Maps `tensor` of indices into string values based on `mapping`.\n\n  This operation converts `int64` indices into string values. The mapping is\n  initialized from a string `mapping` tensor where each element is a value and\n  the corresponding index within the tensor is the key.\n\n  Any input which does not have a corresponding index in \'mapping\'\n  (an out-of-vocabulary entry) is assigned the `default_value`\n\n  The underlying table must be initialized by calling\n  `tf.tables_initializer.run()` once.\n\n  For example:\n\n  ```python\n  mapping_string = tf.constant(["emerson", "lake", "palmer"])\n  indices = tf.constant([1, 5], tf.int64)\n  values = tf.contrib.lookup.index_to_string(\n      indices, mapping=mapping_string, default_value="UNKNOWN")\n  ...\n  tf.tables_initializer().run()\n\n  values.eval() ==> ["lake", "UNKNOWN"]\n  ```\n\n  Args:\n    tensor: A `int64` `Tensor` with the indices to map to strings.\n    mapping: A 1-D string `Tensor` that specifies the strings to map from\n      indices.\n    default_value: The string value to use for out-of-vocabulary indices.\n    name: A name for this op (optional).\n\n  Returns:\n    The strings values associated to the indices. The resultant dense\n    feature value tensor has the same shape as the corresponding `indices`.\n  '
    table = index_to_string_table_from_tensor(mapping=mapping, default_value=default_value, name=name)
    return table.lookup(tensor)