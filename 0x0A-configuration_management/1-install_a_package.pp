# Puppet manifest to install flask from pip3

# Install Python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
}

# Install pip for Python 3
package { 'python3-pip':
  ensure => installed,
}

# Install Flask 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install Werkzeug 2.1.1 using system-wide pip (not pip3)
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}
