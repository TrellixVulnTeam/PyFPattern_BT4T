def test_clip(self, datetime_series):
    val = datetime_series.median()
    assert (datetime_series.clip_lower(val).min() == val)
    assert (datetime_series.clip_upper(val).max() == val)
    assert (datetime_series.clip(lower=val).min() == val)
    assert (datetime_series.clip(upper=val).max() == val)
    result = datetime_series.clip((- 0.5), 0.5)
    expected = np.clip(datetime_series, (- 0.5), 0.5)
    assert_series_equal(result, expected)
    assert isinstance(expected, Series)