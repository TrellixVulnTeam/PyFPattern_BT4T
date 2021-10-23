def get_hosts(self, config):
    '\n        Determine the list of docker hosts we need to talk to.\n\n        :param config: dictionary read from config file. can be empty.\n        :return: list of connection dictionaries\n        '
    hosts = list()
    hosts_list = config.get('hosts')
    defaults = config.get('defaults', dict())
    self.log('defaults:')
    self.log(defaults, pretty_print=True)
    def_host = defaults.get('host')
    def_tls = defaults.get('tls')
    def_tls_verify = defaults.get('tls_verify')
    def_tls_hostname = defaults.get('tls_hostname')
    def_ssl_version = defaults.get('ssl_version')
    def_cert_path = defaults.get('cert_path')
    def_cacert_path = defaults.get('cacert_path')
    def_key_path = defaults.get('key_path')
    def_version = defaults.get('version')
    def_timeout = defaults.get('timeout')
    def_ip = defaults.get('default_ip')
    def_ssh_port = defaults.get('private_ssh_port')
    if hosts_list:
        for host in hosts_list:
            docker_host = (host.get('host') or def_host or self._args.docker_host or self._env_args.docker_host or DEFAULT_DOCKER_HOST)
            api_version = (host.get('version') or def_version or self._args.api_version or self._env_args.api_version or DEFAULT_DOCKER_API_VERSION)
            tls_hostname = (host.get('tls_hostname') or def_tls_hostname or self._args.tls_hostname or self._env_args.tls_hostname or DEFAULT_TLS_HOSTNAME)
            tls_verify = (host.get('tls_verify') or def_tls_verify or self._args.tls_verify or self._env_args.tls_verify or DEFAULT_TLS_VERIFY)
            tls = (host.get('tls') or def_tls or self._args.tls or self._env_args.tls or DEFAULT_TLS)
            ssl_version = (host.get('ssl_version') or def_ssl_version or self._args.ssl_version or self._env_args.ssl_version)
            cert_path = (host.get('cert_path') or def_cert_path or self._args.cert_path or self._env_args.cert_path)
            if (cert_path and (cert_path == self._env_args.cert_path)):
                cert_path = os.path.join(cert_path, 'cert.pem')
            cacert_path = (host.get('cacert_path') or def_cacert_path or self._args.cacert_path or self._env_args.cert_path)
            if (cacert_path and (cacert_path == self._env_args.cert_path)):
                cacert_path = os.path.join(cacert_path, 'ca.pem')
            key_path = (host.get('key_path') or def_key_path or self._args.key_path or self._env_args.cert_path)
            if (key_path and (key_path == self._env_args.cert_path)):
                key_path = os.path.join(key_path, 'key.pem')
            timeout = (host.get('timeout') or def_timeout or self._args.timeout or self._env_args.timeout or DEFAULT_TIMEOUT_SECONDS)
            default_ip = (host.get('default_ip') or def_ip or self._env_args.default_ip or self._args.default_ip_address or DEFAULT_IP)
            default_ssh_port = (host.get('private_ssh_port') or def_ssh_port or self._args.private_ssh_port or DEFAULT_SSH_PORT)
            host_dict = dict(docker_host=docker_host, api_version=api_version, tls=tls, tls_verify=tls_verify, tls_hostname=tls_hostname, cert_path=cert_path, cacert_path=cacert_path, key_path=key_path, ssl_version=ssl_version, timeout=timeout, default_ip=default_ip, default_ssh_port=default_ssh_port)
            hosts.append(host_dict)
    else:
        docker_host = (def_host or self._args.docker_host or self._env_args.docker_host or DEFAULT_DOCKER_HOST)
        api_version = (def_version or self._args.api_version or self._env_args.api_version or DEFAULT_DOCKER_API_VERSION)
        tls_hostname = (def_tls_hostname or self._args.tls_hostname or self._env_args.tls_hostname or DEFAULT_TLS_HOSTNAME)
        tls_verify = (def_tls_verify or self._args.tls_verify or self._env_args.tls_verify or DEFAULT_TLS_VERIFY)
        tls = (def_tls or self._args.tls or self._env_args.tls or DEFAULT_TLS)
        ssl_version = (def_ssl_version or self._args.ssl_version or self._env_args.ssl_version)
        cert_path = (def_cert_path or self._args.cert_path or self._env_args.cert_path)
        if (cert_path and (cert_path == self._env_args.cert_path)):
            cert_path = os.path.join(cert_path, 'cert.pem')
        cacert_path = (def_cacert_path or self._args.cacert_path or self._env_args.cert_path)
        if (cacert_path and (cacert_path == self._env_args.cert_path)):
            cacert_path = os.path.join(cacert_path, 'ca.pem')
        key_path = (def_key_path or self._args.key_path or self._env_args.cert_path)
        if (key_path and (key_path == self._env_args.cert_path)):
            key_path = os.path.join(key_path, 'key.pem')
        timeout = (def_timeout or self._args.timeout or self._env_args.timeout or DEFAULT_TIMEOUT_SECONDS)
        default_ip = (def_ip or self._env_args.default_ip or self._args.default_ip_address or DEFAULT_IP)
        default_ssh_port = (def_ssh_port or self._args.private_ssh_port or DEFAULT_SSH_PORT)
        host_dict = dict(docker_host=docker_host, api_version=api_version, tls=tls, tls_verify=tls_verify, tls_hostname=tls_hostname, cert_path=cert_path, cacert_path=cacert_path, key_path=key_path, ssl_version=ssl_version, timeout=timeout, default_ip=default_ip, default_ssh_port=default_ssh_port)
        hosts.append(host_dict)
    self.log('hosts: ')
    self.log(hosts, pretty_print=True)
    return hosts