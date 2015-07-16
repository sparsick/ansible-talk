# Class: nodejs
#
# This module manages nodejs
#
# Parameters: none
#
# Actions:
#
# Requires: see Modulefile
#
# Sample Usage:
#
class nodejs {
  
  class { 'apt':  
  }
  
  exec { 'apt-get-update':  
    command     => '/usr/bin/apt-get update',
  }
  
  package {'software-properties-common' :
    ensure=> installed,
    require => Exec['apt-get-update'],
  }
  
  apt::ppa {'ppa:chris-lea/node.js' :}
  
  package { 'nodejs' :
    ensure => installed,
    require => Apt::Ppa ['ppa:chris-lea/node.js'],
    
  }
  
  

}