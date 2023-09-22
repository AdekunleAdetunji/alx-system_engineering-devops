# Send a signal to kill a running process named killmenow
exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
