# This is a puppet script that installs the flask version 2.1.0 package
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
