# This puppet file is used to Change the OS configuration so that it is possible
# to login with the holberton user and open a file without any error message.

exec {'command':
  provider => shell,
  command  => 'sudo sed -i "s#(5|4)#10000#g" /etc/security/limits.conf',
}
