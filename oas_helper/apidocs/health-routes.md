## Health Routes

### Retrieve Node Status

Retrieve usage information about a node, with some basic information
about the connections being processed by the underlying nginx process,
the status of the database connection, and node's memory usage.

If you want to monitor the Kong process, since Kong is built on top
of nginx, every existing nginx monitoring tool or agent can be used.


<div class="endpoint get">/status</div>

#### Response

```
HTTP 200 OK
```

```json
{
    "database": {
      "reachable": true
    },
    "memory": {
        "workers_lua_vms": [{
            "http_allocated_gc": "0.02 MiB",
            "pid": 18477
          }, {
            "http_allocated_gc": "0.02 MiB",
            "pid": 18478
        }],
        "lua_shared_dicts": {
            "kong": {
                "allocated_slabs": "0.04 MiB",
                "capacity": "5.00 MiB"
            },
            "kong_db_cache": {
                "allocated_slabs": "0.80 MiB",
                "capacity": "128.00 MiB"
            },
        }
    },
    "server": {
        "total_requests": 3,
        "connections_active": 1,
        "connections_accepted": 1,
        "connections_handled": 1,
        "connections_reading": 0,
        "connections_writing": 1,
        "connections_waiting": 0
    },
    "configuration_hash": "779742c3d7afee2e38f977044d2ed96b"
}
```

* `memory`: Metrics about the memory usage.
    * `workers_lua_vms`: An array with all workers of the Kong node, where each
      entry contains:
    * `http_allocated_gc`: HTTP submodule's Lua virtual machine's memory
      usage information, as reported by `collectgarbage("count")`, for every
      active worker, i.e. a worker that received a proxy call in the last 10
      seconds.
    * `pid`: worker's process identification number.
    * `lua_shared_dicts`: An array of information about dictionaries that are
      shared with all workers in a Kong node, where each array node contains how
      much memory is dedicated for the specific shared dictionary (`capacity`)
      and how much of said memory is in use (`allocated_slabs`).
      These shared dictionaries have least recent used (LRU) eviction
      capabilities, so a full dictionary, where `allocated_slabs == capacity`,
      will work properly. However for some dictionaries, e.g. cache HIT/MISS
      shared dictionaries, increasing their size can be beneficial for the
      overall performance of a Kong node.
  * The memory usage unit and precision can be changed using the querystring
    arguments `unit` and `scale`:
      * `unit`: one of `b/B`, `k/K`, `m/M`, `g/G`, which will return results
        in bytes, kibibytes, mebibytes, or gibibytes, respectively. When
        "bytes" are requested, the memory values in the response will have a
        number type instead of string. Defaults to `m`.
      * `scale`: the number of digits to the right of the decimal points when
        values are given in human-readable memory strings (unit other than
        "bytes"). Defaults to `2`.
      You can get the shared dictionaries memory usage in kibibytes with 4
      digits of precision by doing: `GET /status?unit=k&scale=4`
* `server`: Metrics about the nginx HTTP/S server.
    * `total_requests`: The total number of client requests.
    * `connections_active`: The current number of active client
      connections including Waiting connections.
    * `connections_accepted`: The total number of accepted client
      connections.
    * `connections_handled`: The total number of handled connections.
      Generally, the parameter value is the same as accepts unless
      some resource limits have been reached.
    * `connections_reading`: The current number of connections
      where Kong is reading the request header.
    * `connections_writing`: The current number of connections
      where nginx is writing the response back to the client.
    * `connections_waiting`: The current number of idle client
      connections waiting for a request.
* `database`: Metrics about the database.
    * `reachable`: A boolean value reflecting the state of the
      database connection. Please note that this flag **does not**
      reflect the health of the database itself.
* `configuration_hash`: The hash of the current configuration. This
  field is only returned when the Kong node is running in DB-less
  or data-plane mode. The special return value "00000000000000000000000000000000"
  means Kong does not currently have a valid configuration loaded.
