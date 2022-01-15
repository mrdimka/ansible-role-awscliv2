Ansible Role: awscliv2
=========

Installs AWS Command Line Interface version 2 (AWS CLI).

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html

Based on https://github.com/deekayen/ansible-role-awscli2

Requirements
------------

Role Variables
--------------

    awscli_version: '2.3.4'
The version of awscli v2 that should be installed. By default is commented out and latest one is installed 

    executable_temp_dir: /tmp
Where should be the installer be downloaded and unarchived at.
  
    awscli_install_dir: /opt/aws-cli/
Where should awscli should be installed

Dependencies
------------
