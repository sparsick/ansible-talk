def test_mariadb_is_installed(host):
    mariadb = host.package("mariadb-server")
    assert mariadb.is_installed

def test_mariadb_service_is_running(host):
    mariadb = host.service("mariadb")
    assert mariadb.is_enabled
    assert mariadb.is_running

def test_mariadb_config_parameter_exists(host):
    mariadb_conf = host.file("/etc/mysql/mariadb.conf.d/50-server.cnf")
    assert mariadb_conf.contains("bind-address = 0.0.0.0")
