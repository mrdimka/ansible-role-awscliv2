import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_awscliv2_install_dir(host):
    assert host.file("/opt/aws-cli/").is_directory
    

def test_awscliv2_files(host):
    assert host.file("/usr/local/bin/aws").is_symlink
    assert host.file("/usr/local/bin/aws_completer").is_symlink

def test_awscliv2_version(host):
    os = host.system_info.distribution  
    
    if os == 'debian':
        command = host.run("aws --version")
        assert command.rc == 0

    elif os =='redhat':
        command = host.run("export PATH=/usr/local/bin:$PATH ; aws --version")
        assert command.rc == 0
      