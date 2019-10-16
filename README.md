# Fluentd example (python)

This is an example setup for logging a web server using [fluentd] and the
[elastic stack]. It consists of a simple *Flask* server that has some routes for
generating logs and a variety of levels. The following routes are available:

+ ***GET /*** : returns a basic *JSON* message and logs some `INFO` and `DEBUG`
+ ***GET /warning*** : returns mothing and logs some `INFO`, `DEBUG` and a
  `WARNING`
+ ***GET /exception*** : returns an error message and logs some `INFO`, `DEBUG`
  and a `ERROR`

## Running

To run it you'll need [docker] and [docker compose] installed. Do the following:

```sh
$ docker-compose up
```

Be sure to configure your `.env` file according to the `.env.default`. After
that, you can test the application accessing `localhost:8080/<route>`. For
example, using `curl`:

```sh
$ curl -X GET http://localhost:8080/warning
...
```

You should see the logs coming out from both the `app` and `fluentd` containers.

## Posting custom data to fluentd

If you want to post custom data to *fluentd*, you can use its [http plugin] with
`curl`:

```sh
$ curl -X POST -d 'json={"action":"login","user":2}' \
    "http://localhost:9880/test.tag.here?time=1392021185"
...
```

You should see the output at *fluentd's* stdout.

## Acessing Kibana

To access kibana, go to http://localhost:5601. It should be all set to got.
First, you will need to setup an index pattern.

+ Go to `Management` at the left panel
+ Go to `Kibana/Index Patterns` and click on `Create index pattern`
+  Name it `logstash-*`, then click on `Next step`
+ Select `@timestamp` as the time filter field name
+ Click on `Create index pattern`

Now you should be able to inspect your logs.

+ Go to `Discover` at the left panel
+ Select the desired fields to view

Now you can explore the *Kibana* dashboard as much as you want.

[fluentd]: https://docs.fluentd.org/
[elastic stack]: https://www.elastic.co/products/
[docker]: https://docs.docker.com/install/linux/docker-ce/ubuntu/
[docker compose]: https://docs.docker.com/compose/install/
[http plugin]: https://docs.fluentd.org/v/0.12/input/http
