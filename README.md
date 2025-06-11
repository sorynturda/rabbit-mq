to start the rabbitmq server run the following

```bash
$ docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=sorin -e RABBITMQ_DEFAULT_PASS=sorin rabbitmq:4-management
```
