## Debug Routes


### Set Node Log Level of All Control Plane Nodes

{:.note}
> **Note**: This API is not available in DB-less mode.

 Change the log level of all Control Plane nodes deployed in Hybrid
 (CP/DP) cluster.

 See http://nginx.org/en/docs/ngx_core_module.html#error_log for a
 list of accepted values.

 Care must be taken when changing the log level of a node to `debug`
 in a production environment because the disk could fill up
 quickly. As soon as the debug logging finishes, revert
 back to a higher level such as `notice`.

 It's currently not possible to change the log level of DP and
 DB-less nodes.

 If using Kong Gateway Enterprise, this endpoint can be [RBAC-protected](https://docs.konghq.com/gateway/latest/admin-api/rbac/reference/#add-a-role-endpoint-permission)

 If using Kong Gateway Enterprise, changes to the log level will be reflected in the [Audit Logs](https://docs.konghq.com/gateway/latest/kong-enterprise/audit-log/).

 The log level change is propagated to all Nginx workers of a node,
 including to newly spawned workers.

 Currently, when a user dynamically changes the log level for the
 entire cluster, if a new node joins the cluster, the new node will
 run at the previous log level, not at the log level that was
previously set dynamically for the entire cluster. To work around that, make
 sure the new node starts with the proper level by setting the
 startup `kong.conf` setting [KONG_LOG_LEVEL](https://docs.konghq.com/gateway/latest/reference/configuration/#log_level).


<div class="endpoint put indent">/debug/cluster/control-planes-nodes/log-level/{log_level}</div>

#### Response

```
HTTP 200 OK
```

```json
{
    "message": "log level changed"
}
```


---

### Set Node Log Level of All Nodes

{:.note}
> **Note**: This API is not available in DB-less mode.

Change the log level of all nodes in a cluster.

See http://nginx.org/en/docs/ngx_core_module.html#error_log for a
list of accepted values.

Care must be taken when changing the log level of a node to `debug`
in a production environment because the disk could fill up
quickly. As soon as the debug logging finishes, ensure to revert
back to a higher level such as `notice`.

It's currently not possible to change the log level of DP and
DB-less nodes.

If using Kong Gateway Enterprise, this endpoint can be [RBAC-protected](https://docs.konghq.com/gateway/latest/admin-api/rbac/reference/#add-a-role-endpoint-permission)

If using Kong Gateway Enterprise, changes to the log level will be reflected in the [Audit Logs](https://docs.konghq.com/gateway/latest/kong-enterprise/audit-log/).

The log level change is propagated to all Nginx workers of a node,
including to newly spawned workers.

Currently, when a user dynamically changes the log level for the
entire cluster, if a new node joins a cluster the new node will
run at the previous log level, not at the log level that was
previously set dynamically for the entire cluster. To work around that, make
sure the new node starts with the proper level by setting the
startup `kong.conf` setting [KONG_LOG_LEVEL](https://docs.konghq.com/gateway/latest/reference/configuration/#log_level).


<div class="endpoint put indent">/debug/cluster/log-level/{log_level}</div>

#### Response

```
HTTP 200 OK
```

```json
{
    "message": "log level changed"
}
```


---

### Retrieve Node Log Level of A Node
{:.badge .dbless}

Retrieve the current log level of a node.

See http://nginx.org/en/docs/ngx_core_module.html#error_log for
the list of possible return values.


<div class="endpoint get">/debug/node/log-level</div>

#### Response

```
HTTP 200 OK
```

```json
{
    "message": "log level: debug"
}
```


---

### Set Log Level of A Single Node

{:.note}
> **Note**: This API is not available in DB-less mode.

Change the log level of a node.

See http://nginx.org/en/docs/ngx_core_module.html#error_log for a
list of accepted values.

Care must be taken when changing the log level of a node to `debug`
in a production environment because the disk could fill up
quickly. As soon as the debug logging finishes, revert
back to a higher level such as `notice`.

It's currently not possible to change the log level of DP and
DB-less nodes.

If using Kong Gateway Enterprise, this endpoint can be [RBAC-protected](https://docs.konghq.com/gateway/latest/admin-api/rbac/reference/#add-a-role-endpoint-permission)

If using Kong Gateway Enterprise, changes to the log level will be reflected in the [Audit Logs](https://docs.konghq.com/gateway/latest/kong-enterprise/audit-log/).

The log level change is propagated to all Nginx workers of a node,
including to newly spawned workers.


<div class="endpoint put indent">/debug/node/log-level/{log_level}</div>

#### Response

```
HTTP 200 OK
```

```json
{
    "message": "log level changed"
}
```

{% endunless %}
