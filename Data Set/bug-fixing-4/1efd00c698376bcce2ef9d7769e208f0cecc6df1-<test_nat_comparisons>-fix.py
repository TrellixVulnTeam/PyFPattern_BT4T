@pytest.mark.parametrize('pair', [([pd.Timestamp('2011-01-01'), NaT, pd.Timestamp('2011-01-03')], [NaT, NaT, pd.Timestamp('2011-01-03')]), ([pd.Timedelta('1 days'), NaT, pd.Timedelta('3 days')], [NaT, NaT, pd.Timedelta('3 days')]), ([pd.Period('2011-01', freq='M'), NaT, pd.Period('2011-03', freq='M')], [NaT, NaT, pd.Period('2011-03', freq='M')])])
@pytest.mark.parametrize('reverse', [True, False])
@pytest.mark.parametrize('dtype', [None, object])
def test_nat_comparisons(self, dtype, index_or_series, reverse, pair):
    box = index_or_series
    (l, r) = pair
    if reverse:
        (l, r) = (r, l)
    left = Series(l, dtype=dtype)
    right = box(r, dtype=dtype)
    expected = Series([False, False, True])
    tm.assert_series_equal((left == right), expected)
    expected = Series([True, True, False])
    tm.assert_series_equal((left != right), expected)
    expected = Series([False, False, False])
    tm.assert_series_equal((left < right), expected)
    expected = Series([False, False, False])
    tm.assert_series_equal((left > right), expected)
    expected = Series([False, False, True])
    tm.assert_series_equal((left >= right), expected)
    expected = Series([False, False, True])
    tm.assert_series_equal((left <= right), expected)