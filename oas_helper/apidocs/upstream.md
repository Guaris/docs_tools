
## Upstream Object

The upstream object represents a virtual hostname and can be used to loadbalance
incoming requests over multiple services (targets). So for example an upstream
named `service.v1.xyz` for a Service object whose `host` is `service.v1.xyz`.
Requests for this Service would be proxied to the targets defined within the upstream.

An upstream also includes a [health checker][healthchecks], which is able to
enable and disable targets based on their ability or inability to serve
requests. The configuration for the health checker is stored in the upstream
object, and applies to all of its targets.

Upstreams can be both [tagged and filtered by tags](#tags).


```json
{{ page.upstream_json }}
```

### Add Upstream



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Upstream

<div class="endpoint post indent">{{ prefix }}/upstreams</div>

{% unless page.edition == "konnect" %}

##### Create Upstream Associated to a Specific Certificate

<div class="endpoint post indent">/certificates/{certificate name or id}/upstreams</div>

{:.indent}
Attributes | Description
---:| ---
`certificate name or id`<br>**required** | The unique identifier or the `name` attribute of the Certificate that should be associated to the newly-created Upstream.

{% endunless %}

#### Request Body

{{ page.upstream_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.upstream_json }}
```


---

### List Upstreams
{:.badge .dbless}

##### List All Upstreams

<div class="endpoint get indent">{{ prefix }}/upstreams</div>

{% unless page.edition == "konnect" %}

##### List Upstreams Associated to a Specific Certificate

<div class="endpoint get indent">/certificates/{certificate name or id}/upstreams</div>

{:.indent}
Attributes | Description
---:| ---
`certificate name or id`<br>**required** | The unique identifier or the `name` attribute of the Certificate whose Upstreams are to be retrieved. When using this endpoint, only Upstreams associated to the specified Certificate will be listed.

{% endunless %}

#### Response

```
HTTP 200 OK
```

```json
{
{{ page.upstream_data }}
    "next": "http://localhost:8001/upstreams?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Upstream
{:.badge .dbless}

##### Retrieve Upstream

<div class="endpoint get indent">{{ prefix }}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to retrieve.

{% unless page.edition == "konnect" %}

##### Retrieve Upstream Associated to a Specific Certificate

<div class="endpoint get indent">/certificates/{certificate id}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to retrieve.
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to retrieve.

{% endunless %}

#### Response

```
HTTP 200 OK
```

```json
{{ page.upstream_json }}
```


---

### Update Upstream


{% unless page.edition == "konnect" %}

{:.note}
> **Note**: This API is not available in DB-less mode.



##### Update Upstream

<div class="endpoint patch indent">/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to update.


##### Update Upstream Associated to a Specific Certificate

<div class="endpoint patch indent">/certificates/{certificate id}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to update.
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to update.

#### Request Body

{{ page.upstream_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.upstream_json }}
```



---
{% endunless %}

### Update Or Create Upstream



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Upstream

<div class="endpoint put indent">{{ prefix }}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to create or update.

{% unless page.edition == "konnect" %}

##### Create Or Update Upstream Associated to a Specific Certificate

<div class="endpoint put indent">/certificates/{certificate id}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to create or update.
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to create or update.

{% endunless %}

#### Request Body

{{ page.upstream_body }}


Inserts (or replaces) the Upstream under the requested resource with the
definition specified in the body. The Upstream will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Upstream being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Upstream without specifying `id` (neither in the URL nor in
the body), then it will be auto-generated.

Notice that specifying a `name` in the URL and a different one in the request
body is not allowed.


#### Response

```
HTTP 200 OK
```
{% unless page.edition == "konnect" %}
See POST and PATCH responses.
{% endunless %}
---

### Delete Upstream



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Upstream

<div class="endpoint delete indent">{{ prefix }}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to delete.

{% unless page.edition == "konnect" %}
##### Delete Upstream Associated to a Specific Certificate

<div class="endpoint delete indent">/certificates/{certificate id}/upstreams/{upstream name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to delete.
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream to delete.

{% endunless %}

#### Response

```
HTTP 204 No Content
```

{% unless page.edition == "konnect" %}

---

### Show Upstream Health for Node
{:.badge .dbless}

Displays the health status for all Targets of a given Upstream, or for
the whole Upstream, according to the perspective of a specific Kong node.
Note that, being node-specific information, making this same request
to different nodes of the Kong cluster may produce different results.
For example, one specific node of the Kong cluster may be experiencing
network issues, causing it to fail to connect to some Targets: these
Targets will be marked as unhealthy by that node (directing traffic from
this node to other Targets that it can successfully reach), but healthy
to all others Kong nodes (which have no problems using that Target).

The `data` field of the response contains an array of Target objects.
The health for each Target is returned in its `health` field:

* If a Target fails to be activated in the balancer due to DNS issues,
  its status displays as `DNS_ERROR`.
* When [health checks][healthchecks] are not enabled in the Upstream
  configuration, the health status for active Targets is displayed as
  `HEALTHCHECKS_OFF`.
* When health checks are enabled and the Target is determined to be healthy,
  either automatically or [manually](#set-target-as-healthy),
  its status is displayed as `HEALTHY`. This means that this Target is
  currently included in this Upstream's load balancer execution.
* When a Target has been disabled by either active or passive health checks
  (circuit breakers) or [manually](#set-target-as-unhealthy),
  its status is displayed as `UNHEALTHY`. The load balancer is not directing
  any traffic to this Target via this Upstream.

When the request query parameter `balancer_health` is set to `1`, the
`data` field of the response refers to the Upstream itself, and its `health`
attribute is defined by the state of all of Upstream's Targets, according
to the field `healthchecks.threshold`.


<div class="endpoint get indent">/upstreams/{name or id}/health</div>

{:.indent}
Attributes | Description
---:| ---
`name or id`<br>**required** | The unique identifier **or** the name of the Upstream for which to display Target health.


#### Request Querystring Parameters

Attributes | Description
---:| ---
`balancer_health`<br>*optional* | If set to 1, Kong will return the health status of the Upstream itself. See the `healthchecks.threshold` property.


#### Response

```
HTTP 200 OK
```

```json
{
    "total": 2,
    "node_id": "cbb297c0-14a9-46bc-ad91-1d0ef9b42df9",
    "data": [
        {
            "id": "18c0ad90-f942-4098-88db-bbee3e43b27f",
            "health": "HEALTHY",
            "data": {
                "dns": "ttl=0, virtual SRV",
                "addresses": [
                    {
                        "weight": 100,
                        "ip": "127.0.0.1",
                        "port": 20000,
                        "health": "HEALTHY"
                    }
                ],
                "weight": {
                    "unavailable": 0,
                    "available": 100,
                    "total": 100
                },
                "port": 20000,
                "host": "127.0.0.1",
                "nodeWeight": 100
            },
            "weight": 100,
            "target": "127.0.0.1:20000",
            "created_at": 1485524883980,
            "upstream": {
                "id": "07131005-ba30-4204-a29f-0927d53257b4"
            },
            "tags": null
        },
        {
            "id": "6c6f34eb-e6c3-4c1f-ac58-4060e5bca890",
            "health": "UNHEALTHY",
            "data": {
                "dns": "ttl=0, virtual SRV",
                "addresses": [
                    {
                        "weight": 100,
                        "ip": "127.0.0.1",
                        "port": 20002,
                        "health": "UNHEALTHY"
                    }
                ],
                "weight": {
                    "unavailable": 100,
                    "available": 0,
                    "total": 100
                },
                "port": 20002,
                "host": "127.0.0.1",
                "nodeWeight": 100
            },
            "weight": 100,
            "target": "127.0.0.1:20002",
            "created_at": 1485524914883,
            "upstream": {
                "id": "07131005-ba30-4204-a29f-0927d53257b4"
            },
            "tags": null
        }
    ]
}
```

If `balancer_health=1`:
```
HTTP 200 OK
```

```json
{
    "data": {
        "health": "HEALTHY",
        "id": "07131005-ba30-4204-a29f-0927d53257b4"
    },
    "next": null,
    "node_id": "cbb297c0-14a9-46bc-ad91-1d0ef9b42df9"
}
```
{% endunless %}
