# Graph Project

### **Grafiteiros Team**

> - Lucas Fernandes </br>
> - Luiz Fernando </br>
> - Maryelem Rodrigues </br>
> - Miguel Cabral </br>
> - Pedro Dantas </br>
> - Pedro Henrique </br>

</br>

### **Languages and Tools Used**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### **Frameworks**

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

</br>

## Clone Project

```bash
$ git clone https://github.com/LucasLBF/trabalho-grafos.git folder
$ cd folder
```

## Creating a Virtual Enviroment

Marking a virtual enviroment with python to install all dependencies.
```bash
$ python -m venv venv
```

#### **MacOS & Linux**

> How to activate the virtual enviroment in MacOS 
```bash
$ source venv/bin/activate
```

#### **Windows**

> How to activate the virtual enviroment in Linux 
```bash
$ .\venv\Scripts\activate
```

## Dependencies

To install the dependencies on the system, generally speaking, execute the following command:
```bash
$ pip install -r requirements.txt
```

## Compiling
To compile the project, execute the following command:
```bash
$ python manage.py migrate
```
and then
```bash
$ python manage.py runserver
```
## Running
To run the project, open a browser and go to http://localhost:8000.

or use the existing deployment: http://grafiteiros.duckdns.org:8099.


## Cleaning

```bash
$ python manage.py clean
```
This command will remove all files generated by the project, including temporary files, compilation files, and log files.