# ansible-talk

You can find here the slides and the sample code of my talk "Ansible für Java-Entwickler" that I presented on JUG Schweiz in Luzern at 15th October 2019.

## Running the Code Samples

The code samples are tested with Ansible 2.8.0, ansible-lint 3.4.20, testinfra 1.11.1, serverspec 2.37.2 and Molecule 3.0.

### Setup Test Infrastructure
I prepare a Vagrantfile for the setup of the test infrastructure. The only prerequires are that you have to install VirtualBox and Vagrant on your machine. Then follow these steps:

1. Open a CLI and go to the location of the file `Vagrantfile`.
2. Call `vagrant up`. Vagrant will download the necessary image for VirtualBox and it'll prepare ssh key for ansible. That will take some times.


### Run Ansible Samples
There exists three samples: server setup without roles, server setup with roles, deploy WAR file on an installed Apache Tomcat

#### Run Setup Samples Without Roles

1. Go to the folder `ansible`
2. Call `ansible-playbook -i inventories/test -u vagrant setup-db.yml`
3. Call `ansible-playbook -i inventories/test -u vagrant setup-app.yml`

#### Run Setup Sample With Roles

1. Go to the folder `ansible`
2. Call `ansible-playbook -i inventories/test -u vagrant setup-db-roles.yml`
3. Call `ansible-playbook -i inventories/test -u vagrant setup-app-roles.yml`

#### Run Ansible Lint against Playbooks
1. Go to the folder `ansible`
2. Call `ansible-lint *.yml`

#### Run Serverspec Tests for Setups

1. Go to folder `ansible`
2. Call `rake spec`

#### Run Testinfra Tests for Setups
1. Go to folder `ansible`
2. Call `py.test --connection=ansible --ansible-inventory inventories/test -v tests/*.py`

#### Run Molecule Tests for Setups
1. Go to folder `ansible`
2. Call `molecule test`

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

Sample for the Ad-hoc command to stop the tomcat service: `ansible -i inventories/test -u vagrant -m command -a "/etc/init.d/tomcat stop"`

Sample for the Ad-hoc command to start the tomcat service: `ansible -i inventories/test -u vagrant -m command -a "/etc/init.d/tomcat start"`

### QA Jenkins Pipeline
`Jenkinsfile` demonstrates how a QA pipeline for Ansible Playbooks could looks like in Jenkins.

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
2. Run ansible script with `ansible-playbook -u vagrant -i "192.168.33.10," setup-nodejs.yml`

## Further Links
* http://docs.ansible.com/
* https://github.com/willthames/ansible-lint
* https://testinfra.readthedocs.io/en/latest/
* http://serverspec.org/
