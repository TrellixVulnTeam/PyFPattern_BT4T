

def add_execution_callback(callback):
    'Add an execution callback to the default eager context.\n\n  An execution callback is invoked immediately after an eager operation or\n  function has finished execution, providing access to the op\'s type, name\n  input and output tensors. Multiple execution callbacks can be added, in\n  which case the callbacks will be invoked in the order in which they are\n  added. To clear all execution callbacks that have been added, use\n  `clear_execution_callbacks()`.\n\n  Example:\n  ```python\n  def print_even_callback(op_type, op_name, attrs, inputs, outputs):\n    # A callback that prints only the even output values.\n    if outputs[0].numpy() % 2 == 0:\n      print("Even output from %s: %s" % (op_name or op_type,  outputs))\n  tfe.add_execution_callback(print_even_callback)\n\n  x = tf.pow(2.0, 3.0) - 3.0\n  y = tf.multiply(x, tf.add(1.0, 5.0))\n  # When the line above is run, you will see all intermediate outputs that are\n  # even numbers printed to the console.\n\n  tfe.clear_execution_callbacks()\n  ```\n\n  Args:\n    callback: a callable of the signature\n      `f(op_type, op_name, attrs, inputs, outputs)`.\n      `op_type` is the type of the operation that was just executed (e.g.,\n        `MatMul`).\n      `op_name` is the name of the operation that has was just executed. This\n        name is set by the client who created the operation and can be `None` if\n        it is unset.\n      `attrs` contains the attributes of the operation as a `tuple` of\n        alternating attribute name and attribute value.\n      `inputs` is the `list` of input `Tensor`(s) to the op.\n      `outputs` is the `list` of output `Tensor`(s) from the op.\n       Return value(s) from the callback are ignored.\n  '
    execute.execute = execute.execute_with_callbacks
    context.get_default_context().add_post_execution_callback(callback)