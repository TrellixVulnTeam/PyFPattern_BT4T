def test_apply_broadcast(self, float_frame, int_frame_const_col):
    result = float_frame.apply(np.mean, result_type='broadcast')
    expected = DataFrame([float_frame.mean()], index=float_frame.index)
    tm.assert_frame_equal(result, expected)
    result = float_frame.apply(np.mean, axis=1, result_type='broadcast')
    m = float_frame.mean(axis=1)
    expected = DataFrame({c: m for c in float_frame.columns})
    tm.assert_frame_equal(result, expected)
    result = float_frame.apply((lambda x: list(range(len(float_frame.columns)))), axis=1, result_type='broadcast')
    m = list(range(len(float_frame.columns)))
    expected = DataFrame(([m] * len(float_frame.index)), dtype='float64', index=float_frame.index, columns=float_frame.columns)
    tm.assert_frame_equal(result, expected)
    result = float_frame.apply((lambda x: list(range(len(float_frame.index)))), result_type='broadcast')
    m = list(range(len(float_frame.index)))
    expected = DataFrame({c: m for c in float_frame.columns}, dtype='float64', index=float_frame.index)
    tm.assert_frame_equal(result, expected)
    df = int_frame_const_col
    result = df.apply((lambda x: [1, 2, 3]), axis=1, result_type='broadcast')
    tm.assert_frame_equal(result, df)
    df = int_frame_const_col
    result = df.apply((lambda x: Series([1, 2, 3], index=list('abc'))), axis=1, result_type='broadcast')
    expected = df.copy()
    tm.assert_frame_equal(result, expected)