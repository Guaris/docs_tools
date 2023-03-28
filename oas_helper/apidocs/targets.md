
## Target Object

A target is an ip address/hostname with a port that identifies an instance of a backend
service. Every upstream can have many targets, and the targets can be
dynamically added, modified, or deleted. Changes take effect on the fly.

To disable a target, post a new one with `weight=0`;
alternatively, use the `DELETE` convenience method to accomplish the same.

The current target object definition is the one with the latest `created_at`.

Targets can be both [tagged and filtered by tags](#tags).


```json
{{ page.target_json }}
```

{% unless page.edition == "konnect" %}

### Update Target



{:.note}
> **Note**: This API is not available in DB-less mode.

Update a target.


<div class="endpoint patch indent">/upstreams/{upstream name or id}/targets/{host:port or id}</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the upstream for which to update the target.
`host:port or id`<br>**required** | The host:port combination element of the target to update, or the `id` of an existing target entry.


#### Response

```
HTTP 201 Created
```

{% endunless %}

---

### Delete Target



{:.note}
> **Note**: This API is not available in DB-less mode.

Remove a target from the load balancer.


<div class="endpoint delete indent">{{ prefix }}/upstreams/{upstream name or id}/targets/{host:port or id}</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the upstream for which to delete the target.
`host:port or id`<br>**required** | The host:port combination element of the target to remove, or the `id` of an existing target entry.


#### Response

```
HTTP 204 No Content
```


---

{% unless page.edition == "konnect" %}

### Set Target Address As Healthy



{:.note}
> **Note**: This API is not available in DB-less mode.

Set the current health status of an individual address resolved by a target
in the load balancer to "healthy" in the entire Kong cluster.

This endpoint can be used to manually re-enable an address resolved by a
target that was previously disabled by the upstream's [health checker][healthchecks].
Upstreams only forward requests to healthy nodes, so this call tells Kong
to start using this address again.

This resets the health counters of the health checkers running in all workers
of the Kong node, and broadcasts a cluster-wide message so that the "healthy"
status is propagated to the whole Kong cluster.

Note: This API is not available when Kong is running in Hybrid mode.


<div class="endpoint put indent">/upstreams/{upstream name or id}/targets/{target or id}/{address}/healthy</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the upstream.
`target or id`<br>**required** | The host/port combination element of the target to set as healthy, or the `id` of an existing target entry.
`address`<br>**required** | The host/port combination element of the address to set as healthy.


#### Response

```
HTTP 204 No Content
```


---

### Set Target Address As Unhealthy



{:.note}
> **Note**: This API is not available in DB-less mode.

Set the current health status of an individual address resolved by a target
in the load balancer to "unhealthy" in the entire Kong cluster.

This endpoint can be used to manually disable an address and have it stop
responding to requests. Upstreams only forward requests to healthy nodes, so
this call tells Kong to start skipping this address.

This call resets the health counters of the health checkers running in all
workers of the Kong node, and broadcasts a cluster-wide message so that the
"unhealthy" status is propagated to the whole Kong cluster.

[Active health checks][active] continue to execute for unhealthy
addresses. Note that if active health checks are enabled and the probe detects
that the address is actually healthy, it will automatically re-enable it again.
To permanently remove a target from the balancer, you should [delete a
target](#delete-target) instead.

Note: This API is not available when Kong is running in Hybrid mode.


<div class="endpoint put indent">/upstreams/{upstream name or id}/targets/{target or id}/unhealthy</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the upstream.
`target or id`<br>**required** | The host/port combination element of the target to set as unhealthy, or the `id` of an existing target entry.


#### Response

```
HTTP 204 No Content
```


---

### Set Target As Healthy
{:.badge .dbless}

Set the current health status of a target in the load balancer to "healthy"
in the entire Kong cluster. This sets the "healthy" status to all addresses
resolved by this target.

This endpoint can be used to manually re-enable a target that was previously
disabled by the upstream's [health checker][healthchecks]. Upstreams only
forward requests to healthy nodes, so this call tells Kong to start using this
target again.

This resets the health counters of the health checkers running in all workers
of the Kong node, and broadcasts a cluster-wide message so that the "healthy"
status is propagated to the whole Kong cluster.

Note: This API is not available when Kong is running in Hybrid mode.


<div class="endpoint put indent">/upstreams/{upstream name or id}/targets/{target or id}/healthy</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the upstream.
`target or id`<br>**required** | The host/port combination element of the target to set as healthy, or the `id` of an existing target entry.


#### Response

```
HTTP 204 No Content
```


---

### Set Target As Unhealthy
{:.badge .dbless}

Set the current health status of a target in the load balancer to "unhealthy"
in the entire Kong cluster. This sets the "unhealthy" status to all addresses
resolved by this target.

This endpoint can be used to manually disable a target and have it stop
responding to requests. Upstreams only forward requests to healthy nodes, so
this call tells Kong to start skipping this target.

This call resets the health counters of the health checkers running in all
workers of the Kong node, and broadcasts a cluster-wide message so that the
"unhealthy" status is propagated to the whole Kong cluster.

[Active health checks][active] continue to execute for unhealthy
targets. Note that if active health checks are enabled and the probe detects
that the target is actually healthy, it will automatically re-enable it again.
To permanently remove a target from the balancer, you should [delete a
target](#delete-target) instead.

Note: This API is not available when Kong is running in Hybrid mode.


<div class="endpoint put indent">/upstreams/{upstream name or id}/targets/{target or id}/unhealthy</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the upstream.
`target or id`<br>**required** | The host/port combination element of the target to set as unhealthy, or the `id` of an existing target entry.


#### Response

```
HTTP 204 No Content
```


---

{% endunless %}

### List All Targets
{:.badge .dbless}

Lists all targets of the upstream. Multiple target objects for the same
target may be returned, showing the history of changes for a specific target.
The target object with the latest `created_at` is the current definition.


<div class="endpoint get indent">/upstreams/{name or id}/targets/all</div>

{:.indent}
Attributes | Description
---:| ---
`name or id`<br>**required** | The unique identifier **or** the name of the upstream for which to list the targets.


#### Response

```
HTTP 200 OK
```

```json
{
    "total": 2,
    "data": [
        {
            "created_at": 1485524883980,
            "id": "18c0ad90-f942-4098-88db-bbee3e43b27f",
            "target": "127.0.0.1:20000",
            "upstream_id": "07131005-ba30-4204-a29f-0927d53257b4",
            "weight": 100
        },
        {
            "created_at": 1485524914883,
            "id": "6c6f34eb-e6c3-4c1f-ac58-4060e5bca890",
            "target": "127.0.0.1:20002",
            "upstream_id": "07131005-ba30-4204-a29f-0927d53257b4",
            "weight": 200
        }
    ]
}
```
