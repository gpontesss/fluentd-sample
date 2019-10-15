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

Be sure to configure your `.env` file according to the `.env.default`. After that,
you can test the application accessing `localhost:8080/<route>`. For example, using
`curl`:

```sh
$ curl -X GET http://localhost:8080/warning
...
```

You should see the logs coming out from both the `app` and `fluentd` containers.

## Acessing Kibana

Coming soon...

[fluentd]: https://docs.fluentd.org/
[elastic stack]: https://www.elastic.co/products/
[docker]: https://docs.docker.com/install/linux/docker-ce/ubuntu/
[docker compose]: https://docs.docker.com/compose/install/
