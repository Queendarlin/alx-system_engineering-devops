# Configuration Management with Puppet

This project focuses on using Puppet for configuration management tasks. Puppet is a powerful tool for automating infrastructure management and ensuring consistency across systems.

## Tasks

### Task 0: Create a File

Create a file with specific permissions, owner, group, and content in the `/tmp` directory.

Manifest: `0-create_a_file.pp`

### Task 1: Install a Package

Install Flask version 2.1.0 using pip3.

Manifest: `1-install_a_package.pp`

### Task 2: Execute a Command

Create a manifest to kill a process named "killmenow" using the `exec` resource and `pkill`.

Manifest: `2-execute_a_command.pp`

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the directory containing the Puppet manifests.
3. Run `puppet apply` followed by the filename of the manifest you want to execute. For example:
   ```bash
   puppet apply 0-create_a_file.pp
