# ansible-talk

You can find here the slides and the sample code of my talk "Ansible für Entwickler" that I presented on JUGSaxony in Dresden at 20th September 2016.

## Running the Code Samples

The code samples are tested with Ansible 2.1.1.0 and serverspec 2.31.0 .

### Setup Test infrastructure
I prepare a Vagrantfile for the setup of the test infrastructure. The only prerequires are that you have to install VirtualBox and Vagrant on your machine. Then follow these steps:

1. Open a CLI and go to the location of the file `Vagrantfile`.
2. Call `vagrant up`. Vagrant will download the necessary image for VirtualBox. That will take some times.
3. Then copy your public key for the authentication that is needed for a SSH login.
```
ssh-copy-id -i ~/.ssh/id_rsa vagrant@192.168.33.10
```
Hint: Public and private keys can be generated with the following command: `ssh-keygen`

### Run Ansible Samples
There exists three samples: server setup without roles, server setup with roles, deploy WAR file on an installed Apache Tomcat

#### Run Setup Samples Without Roles 

1. Go to the folder `ansible`
2. Call `ansible-playbook -i inventories/test -u vagrant setup-db.yml`
3. Call `ansible-playbook -i inventories/test -u vagrant setup-app.yml`

#### Run Setup Sample With Roles

1. Go to the folder `ansible`
2. Call `ansible-playbook -i inventories/test -u vagrant setup-roles.yml`

#### Run Serverspec Tests For Setups

1. Go to folder `ansible`
2. Call `rake spec`

#### Run Deploy Sample

1. Go to the folder `ansible`
2. Build demo app 
```
cd demo-app-ansible-deploy
mvn clean install
```
3. Call `ansible-playbook -i inventories/test -u vagrant deploy-demo.yml `
4. Cal URL http://192.168.33.10:8080/demo/

#### Run Ad-hoc Command Sample

Sample for the Ad-hoc command to stop the tomcat service: `ansible -i inventories/test -u vagrant -m command -a "service tomcat stop"`

Sample for the Ad-hoc command to start the tomcat service: `ansible -i inventories/test -u vagrant -m command -a "service tomcat start"`

### Run Ansible vs Puppet Samples
The comparision shows how a script for a node.js installation looks in Ansible and in Puppet.

#### Puppet Sample

1. Go to the location of the `Vagrantfile`
2. Log on the test server with `vagrant ssh`
3. Install Puppet package with `sudo apt-get install puppet`
4. Go to `/vagrant/puppet-vs-ansible/puppet/manifest/`
5. Install needed Puppet modules with `puppet module install puppetlabs/apt --modulepath ../modules`
6. Run puppet script with `puppet site.pp --modulepath ../modules`

#### Ansible Sample

1. Go to `puppet-vs-ansible/ansible`
2. Run ansible script with `ansible-playbook -u vagrant site.yml`

