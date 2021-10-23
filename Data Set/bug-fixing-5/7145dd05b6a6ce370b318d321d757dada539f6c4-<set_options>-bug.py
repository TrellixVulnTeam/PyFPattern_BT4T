def set_options(self, task_keys=None, var_options=None, direct=None):
    super(CallbackModule, self).set_options(task_keys=task_keys, var_options=var_options, direct=direct)
    self.FOREMAN_URL = self.get_option('url')
    self.FOREMAN_SSL_CERT = (self.get_option['ssl_cert'], self.get_option['ssl_key'])
    self.FOREMAN_SSL_VERIFY = str(self.get_option['verify_certs'])
    self.ssl_verify = self._ssl_verify()
    if HAS_REQUESTS:
        requests_major = int(requests.__version__.split('.')[0])
        if (requests_major < 2):
            self._disable_plugin('The `requests` python module is too old.')
    else:
        self._disable_plugin('The `requests` python module is not installed.')
    if self.FOREMAN_URL.startswith('https://'):
        if (not os.path.exists(self.FOREMAN_SSL_CERT[0])):
            self._disable_plugin(('FOREMAN_SSL_CERT %s not found.' % self.FOREMAN_SSL_CERT[0]))
        if (not os.path.exists(self.FOREMAN_SSL_CERT[1])):
            self._disable_plugin(('FOREMAN_SSL_KEY %s not found.' % self.FOREMAN_SSL_CERT[1]))