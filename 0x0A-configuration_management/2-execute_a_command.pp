# Puppet manifest that kills a process named "killmenow" using `exec` resource
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
}
