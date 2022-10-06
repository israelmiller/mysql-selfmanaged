# mysql-selfmanaged
 Assignment 5 HHA 504: Cloud Computing


## Setting up the VM and MySQL:
- This mysql server is running on a self managed instance on GCP.
    - In GCP the configuration should be as follows:
        - 2 vCPU
        - 4 GB RAM
        - 10 GB SSD
        - Ubuntu 18.04 LTS
        - Allow HTTP traffic
        - Allow HTTPS traffic
        - Allow SSH traffic and upload your public key
        - Allow MySQL traffic
            - TO allow MySQL traffic, you need to add a new rule to the firewall settings at the project level. This can be done by searching for Firewall in the search bar at the top of the page.
            - Click on "Create fiewall rule". The rule should be as follows:
                - Name: mysql
                - Target tags: mysql
                - Source IP ranges: 0.0.0.0/0
                - Protocols and ports: tcp:3306
- Once the VM has been created with the appropriate confiuuration, you can SSH into the VM using the following command:
    - `ssh -i <path to private key> <username>@<public IP address>`
-  Once you are logged into the VM, you should update the system using the following command:
    - `sudo apt-get update`
- Next, you should install MySQL client and server using the following command (by default version 5.7 is installed):s
    - `sudo apt-get install mysql-server mysql-client`
- Next, you should start the MySQL server using the following command:
    - `sudo service mysql start`
- Next, you should open the MySQL shell using the following command:
    - `sudo mysql`
- Next, you should create a new user using the following command:
    - `CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';`
    - This will create a new user called newuser with the password password. The '%' indicates that the user can connect from any IP address.
- Next, you should grant the new user all privileges using the following command:
    - `GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%' WITH GRANT OPTION;`
- Next, log out of the MySQL shell using the following command:
    - `exit`
- Log back into the MySQL shell with your new user account using the following command:
    - `mysql -u newuser -p`
- Next, you should create a new database using the following command:
    - `CREATE DATABASE database_name;`
    - You can show all databases using the following command:
        - `SHOW DATABASES;`
- Next, select the database you just created using the following command:
    - `USE database_name;`
- Next, you should create a new table using the following command:
    - `CREATE TABLE table_name (column1 datatype, column2 datatype, column3 datatype, ...);`
    - You can show all tables using the following command:
        - `SHOW TABLES;`
- Once your configuration is complete, you can exit the MySQL shell using the following command:
    - `exit`
- Next, you should bind the MySQL server to the public IP address. To do this, you need to edit the MySQL configuration file using the following command:
    - `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`
    - You should change the bind address from 127.0.0.0 to 0.0.0.0 by changing the following line:
        - bind-address =
    -Save the file and exit the editor
- Finally, you should restart the MySQL server using the following command:
    - `sudo service mysql restart`
## Uploading data to the MySQL server:
