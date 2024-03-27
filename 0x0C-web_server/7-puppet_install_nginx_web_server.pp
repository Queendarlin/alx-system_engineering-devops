# Update package repositories
exec { 'update_package_repositories':
  command => 'apt-get update',
  path    => '/usr/bin',
  timeout => 600,
  unless  => '/usr/bin/test -e /var/lib/apt/periodic/update-success-stamp',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['update_package_repositories'],
}

# Create a test HTML file
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure 301 redirect
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('your_module/redirect_config.erb'),
  notify  => Service['nginx'],
  require => Package['nginx'],
}

# Start Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
