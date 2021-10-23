@wrap_name_default('lstm_group')
def lstmemory_group(input, size=None, name=None, out_memory=None, reverse=False, param_attr=None, act=None, gate_act=None, state_act=None, input_proj_bias_attr=None, input_proj_layer_attr=None, lstm_bias_attr=None, lstm_layer_attr=None):
    "\n    lstm_group is a recurrent_group version of Long Short Term Memory. It\n    does exactly the same calculation as the lstmemory layer (see lstmemory in\n    layers.py for the maths) does. A promising benefit is that LSTM memory\n    cell states(or hidden states) in every time step are accessible to the\n    user. This is especially useful in attention model. If you do not need to\n    access the internal states of the lstm and merely use its outputs,\n    it is recommended to use the lstmemory, which is relatively faster than\n    lstmemory_group.\n\n    NOTE: In PaddlePaddle's implementation, the following input-to-hidden\n    multiplications:\n    :math:`W_{x_i}x_{t}` , :math:`W_{x_f}x_{t}`,\n    :math:`W_{x_c}x_t`, :math:`W_{x_o}x_{t}` are not done in lstmemory_unit to\n    speed up the calculations. Consequently, an additional mixed_layer with\n    full_matrix_projection must be included before lstmemory_unit is called.\n\n    The example usage is:\n\n    ..  code-block:: python\n\n        lstm_step = lstmemory_group(input=[layer1],\n                                    size=256,\n                                    act=TanhActivation(),\n                                    gate_act=SigmoidActivation(),\n                                    state_act=TanhActivation())\n\n    :param input: input layer.\n    :type input: LayerOutput\n    :param size: lstmemory group size.\n    :type size: int\n    :param name: name of lstmemory group.\n    :type name: basestring\n    :param out_memory: output of previous time step.\n    :type out_memory: LayerOutput | None\n    :param reverse: process the input in a reverse order or not.\n    :type reverse: bool\n    :param param_attr: parameter attribute, None means default attribute.\n    :type param_attr: ParameterAttribute\n    :param act: last activiation type of lstm.\n    :type act: BaseActivation\n    :param gate_act: gate activiation type of lstm.\n    :type gate_act: BaseActivation\n    :param state_act: state activiation type of lstm.\n    :type state_act: BaseActivation\n    :param lstm_bias_attr: bias parameter attribute of lstm layer.\n                           False means no bias, None means default bias.\n    :type lstm_bias_attr: ParameterAttribute|False|None\n    :param input_proj_bias_attr: bias attribute for input to hidden projection.\n                False means no bias, None means default bias.\n    :type input_proj_bias_attr: ParameterAttribute|False|None\n    :param input_proj_layer_attr: extra layer attribute for input to hidden\n                projection of the LSTM unit, such as dropout, error clipping.\n    :type input_proj_layer_attr: ExtraLayerAttribute\n    :param lstm_layer_attr: lstm layer's extra attribute.\n    :type lstm_layer_attr: ExtraLayerAttribute\n    :return: the lstmemory group.\n    :rtype: LayerOutput\n    "

    def __lstm_step__(ipt):
        return lstmemory_unit(input=ipt, name=name, size=size, act=act, gate_act=gate_act, state_act=state_act, out_memory=out_memory, input_proj_bias_attr=input_proj_bias_attr, input_proj_layer_attr=input_proj_layer_attr, param_attr=param_attr, lstm_layer_attr=lstm_layer_attr, lstm_bias_attr=lstm_bias_attr)
    return recurrent_group(name=('%s_recurrent_group' % name), step=__lstm_step__, reverse=reverse, input=input)