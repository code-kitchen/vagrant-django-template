# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
	# Base box to build off, and download URL for when it doesn't exist on the user's system already
	config.vm.box = "debian/wheezy64"
	config.vm.box_url = "https://codekitchen.io/files/vagrant/debian-wheezy-64.box"

	# Boot with a GUI so you can see the screen. (Default is headless)
	# config.vm.boot_mode = :gui

	# Assign this VM to a host only network IP, allowing you to access it
	# via the IP.
	# config.vm.network "33.33.33.10"

	# Forward a port from the guest to the host.
	config.vm.network "forwarded_port", guest: 8000, host: 8111

	# Share an additional folder to the guest VM.
	config.vm.synced_folder ".", "/home/vagrant/{{ project_name }}", owner: "vagrant", group: "vagrant"

	# Enable provisioning with a shell script.
	config.vm.provision :shell, :path => "etc/install/install.sh", :args => "{{ project_name }}"
end
