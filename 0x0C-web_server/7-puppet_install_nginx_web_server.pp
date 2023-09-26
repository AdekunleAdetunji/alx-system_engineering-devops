# Manifest to install and configure an Nginx server using Puppet instead of Bash
exec { 'update':
  path    => '/usr/bin/',
  command => 'sudo apt-get update',
  unless  => 'sudo nginx -v'
}

exec { 'nginx':
  path    => 'usr/bin',
  command => 'sudo apt-get install -y nginx',
  unless  => 'sudo ngix -v'
}

file { 'index':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n'
}

$replacement='server_name _;\n\tlocation \/redirect_me {\n\t\t return 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\n\t}'
exec { 'sed':
  path    => '/usr/bin/',
  command => "sed -i \"s/server_name _;/${replacement}/\" /etc/nginx/sites-available/default"
}


exec { 'restart':
  path    => 'usr/bin',
  command => 'sudo service nginx restart'
}
