def test_input_validation(self):
    assert_raises(ValueError, check_COLA, 'hann', (- 10), 0)
    assert_raises(ValueError, check_COLA, 'hann', 10, 20)
    assert_raises(ValueError, check_COLA, np.ones((2, 2)), 10, 0)
    assert_raises(ValueError, check_COLA, np.ones(20), 10, 0)
    assert_raises(ValueError, check_NOLA, 'hann', (- 10), 0)
    assert_raises(ValueError, check_NOLA, 'hann', 10, 20)
    assert_raises(ValueError, check_NOLA, np.ones((2, 2)), 10, 0)
    assert_raises(ValueError, check_NOLA, np.ones(20), 10, 0)
    assert_raises(ValueError, check_NOLA, 'hann', 64, (- 32))
    x = np.empty(1024)
    z = stft(x)
    assert_raises(ValueError, stft, x, window=np.ones((2, 2)))
    assert_raises(ValueError, stft, x, window=np.ones(10), nperseg=256)
    assert_raises(ValueError, stft, x, nperseg=(- 256))
    assert_raises(ValueError, stft, x, nperseg=256, noverlap=1024)
    assert_raises(ValueError, stft, x, nperseg=256, nfft=8)
    assert_raises(ValueError, istft, x)
    assert_raises(ValueError, istft, z, window=np.ones((2, 2)))
    assert_raises(ValueError, istft, z, window=np.ones(10), nperseg=256)
    assert_raises(ValueError, istft, z, nperseg=(- 256))
    assert_raises(ValueError, istft, z, nperseg=256, noverlap=1024)
    assert_raises(ValueError, istft, z, nperseg=256, nfft=8)
    assert_raises(ValueError, istft, z, nperseg=256, noverlap=0, window='hann')
    assert_raises(ValueError, istft, z, time_axis=0, freq_axis=0)
    assert_raises(ValueError, _spectral_helper, x, x, mode='foo')
    assert_raises(ValueError, _spectral_helper, x[:512], x[512:], mode='stft')
    assert_raises(ValueError, _spectral_helper, x, x, boundary='foo')