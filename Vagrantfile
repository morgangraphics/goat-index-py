# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  #Ubuntu
  config.vm.define "scrapyd" do |nodeubuntu|
    nodeubuntu.vm.box = "bento/ubuntu-16.04"
    nodeubuntu.vm.box_check_update = true
    nodeubuntu.vm.hostname = "scrapyd"
    nodeubuntu.vm.network "private_network", ip: "192.168.0.15"

    nodeubuntu.vm.provider "virtualbox" do |v|
      v.name = "scrapyd"
      v.memory = "512"
    end

    # Unless ansible.inventory_path is explicitly defined here, it will fail when
    # running the role. (Ansible defaults to python 2.7 and where ever Python2 is located)
    # Python 3 defaulted OS's (Fedora) will blow up
    config.vm.provision "ansible" do |ansible|
     ansible.playbook = "../ansible-playbooks/scrapyd/playbook.yml"
     ansible.inventory_path = "inventory"
     ansible.verbose = "-vvv"
    end

  end

end
