# Installs an Nginx server with custom HTTP header

exec {'update':
  command  => 'sudo apt-get -y update',
  before   => Exec['install_nginx'],
}

exec {'install_nginx':
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  environment => ["HOST=$(hostname)"],
  command     => 'sudo sed -i "/server_name _;/a add_header X-Served-By \"$HOST\";" /etc/nginx/sites-available/default',
  notifies    => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command  => 'sudo service restart nginx',
  subscribe => Exec['add_header'],
}
