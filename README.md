# ioflo_microservice_example
How to setup the environment and run an app: <br />
Load ioflo_microservice_example as zip, extract it and put into the folder <br />
$ cd folder <br />
$ pip3 install -e .   <br />
Open new terminal and do: <br />
$ microservice
then using an app Postman: <br />
select POST using url http://localhost:8080/reputee, select Body -> raw -> and from drowpdown JSON(application/json), <br />
first paste(type) json as described in the problem and hit SEND <br />
then for GET request select GET: <br />
and change url to http://localhost:8000/reputee/nr1 and click SEND
