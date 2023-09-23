# A puppet file that makes changes to ssh configuration file
$change = 'Host remote-server\n\tPasswordAuthentication no\nIdentityFile ~/.ssh/school'
exec { 'ssh_config':
  path    => '/usr/bin:/bin',
  command => "echo '${change}' >> /etc/ssh/ssh_config"
}
