# Manifest to install and configure an Nginx server using Puppet instead of Bash
package {'nginx':
  ensure => 'present',
}
exec {'update apt-get and install':
    command  => 'sudo apt-get update && sudo apt-get install nginx',
    path     => '/usr/bin:/usr/sbin:/bin',
    provider => shell
}

exec {'add landing page':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    path     => '/usr/bin:/usr/sbin:/bin',
    provider => shell
}

exec {'redirection':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me \/ permanent;/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'allow firewall':
    command => 'ufw allow "NGINX Full"',
    path    => '/usr/bin:/usr/sbin:/bin',
  provider  => shell,
}

exec { 'restart nginx':
    command => 'sudo service nginx restart',
    path    => '/usr/bin:/usr/sbin:/bin',
  provider  => shell,

}
