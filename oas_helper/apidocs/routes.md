## Route Object

Route entities define rules to match client requests. Each Route is
associated with a Service, and a Service may have multiple Routes associated to
it. Every request matching a given Route will be proxied to its associated
Service.

The combination of Routes and Services (and the separation of concerns between
them) offers a powerful routing mechanism with which it is possible to define
fine-grained entry-points in Kong leading to different upstream services of
your infrastructure.

You need at least one matching rule that applies to the protocol being matched
by the Route. Depending on the protocols configured to be matched by the Route
(as defined with the `protocols` field), this means that at least one of the
following attributes must be set:

* For `http`, at least one of `methods`, `hosts`, `headers` or `paths`;
* For `https`, at least one of `methods`, `hosts`, `headers`, `paths` or `snis`;
* For `tcp`, at least one of `sources` or `destinations`;
* For `tls`, at least one of `sources`, `destinations` or `snis`;
* For `tls_passthrough`, set `snis`;
* For `grpc`, at least one of `hosts`, `headers` or `paths`;
* For `grpcs`, at least one of `hosts`, `headers`, `paths` or `snis`;
* For `ws`, at least one of `hosts`, `headers` or `paths`; <span class="badge enterprise"></span>
* For `wss`, at least one of `hosts`, `headers`, `paths` or `snis`. <span class="badge enterprise"></span>

A route can't have both `tls` and `tls_passthrough` protocols at same time.

The 3.0.x release introduces a new router implementation: `atc-router`.
The router adds:

* Reduced router rebuild time when changing Kong’s configuration
* Increased runtime performance when routing requests
* Reduced P99 latency from 1.5s to 0.1s with 10,000 routes

Learn more about the router:

[Configure routes using expressions](/gateway/{{page.kong_version}}/key-concepts/routes/expressions)
[Router Expressions language reference](/gateway/{{page.kong_version}}/reference/router-expressions-language/)


#### Path handling algorithms

{:.note}
> **Note**: Path handling algorithms v1 was deprecated in Kong 3.0. From Kong 3.0, when `router_flavor`
> is set to `expressions`, `route.path_handling` will be unconfigurable and the path handling behavior
> will be `"v0"`; when `router_flavor` is set to `traditional_compatible`, the path handling behavior
> will be `"v0"` regardless of the value of `route.path_handling`. Only `router_flavor` = `traditional`
> will support `path_handling` `"v1'` behavior.

`"v0"` is the behavior used in Kong 0.x, 2.x and 3.x. It treats `service.path`, `route.path` and request path as
*segments* of a URL. It will always join them via slashes. Given a service path `/s`, route path `/r`
and request path `/re`, the concatenated path will be `/s/re`. If the resulting path is a single slash,
no further transformation is done to it. If it's longer, then the trailing slash is removed.

`"v1"` is the behavior used in Kong 1.x. It treats `service.path` as a *prefix*, and ignores the initial
slashes of the request and route paths. Given service path `/s`, route path `/r` and request path `/re`,
the concatenated path will be `/sre`.

Both versions of the algorithm detect "double slashes" when combining paths, replacing them by single
slashes.

The following table shows the possible combinations of path handling version, strip path, and request:

| `service.path` | `route.path` | `request` |`route.strip_path` | `route.path_handling` | request path | upstream path |
|----------------|--------------|-----------|-------------------|-----------------------|--------------|---------------|
| `/s`           | `/fv0`       | `req`     | `false`           | `v0`                  |  `/fv0/req`  | `/s/fv0/req`  |
| `/s`           | `/fv0`       | `blank`   | `false`           | `v0`                  |  `/fv0`      | `/s/fv0`      |
| `/s`           | `/fv1`       | `req`     | `false`           | `v1`                  |  `/fv1/req`  | `/sfv1/req`   |
| `/s`           | `/fv1`       | `blank`   | `false`           | `v1`                  |  `/fv1`      | `/sfv1`       |
| `/s`           | `/tv0`       | `req`     | `true`            | `v0`                  |  `/tv0/req`  | `/s/req`      |
| `/s`           | `/tv0`       | `blank`   | `true`            | `v0`                  |  `/tv0`      | `/s`          |
| `/s`           | `/tv1`       | `req`     | `true`            | `v1`                  |  `/tv1/req`  | `/s/req`      |
| `/s`           | `/tv1`       | `blank`   | `true`            | `v1`                  |  `/tv1`      | `/s`          |
| `/s`           | `/fv0/`      | `req`     | `false`           | `v0`                  |  `/fv0/req`  | `/s/fv0/req`  |
| `/s`           | `/fv0/`      | `blank`   | `false`           | `v0`                  |  `/fv0/`     | `/s/fv01/`    |
| `/s`           | `/fv1/`      | `req`     | `false`           | `v1`                  |  `/fv1/req`  | `/sfv1/req`   |
| `/s`           | `/fv1/`      | `blank`   | `false`           | `v1`                  |  `/fv1/`     | `/sfv1/`      |
| `/s`           | `/tv0/`      | `req`     | `true`            | `v0`                  |  `/tv0/req`  | `/s/req`      |
| `/s`           | `/tv0/`      | `blank`   | `true`            | `v0`                  |  `/tv0/`     | `/s/`         |
| `/s`           | `/tv1/`      | `req`     | `true`            | `v1`                  |  `/tv1/req`  | `/sreq`       |
| `/s`           | `/tv1/`      | `blank`   | `true`            | `v1`                  |  `/tv1/`     | `/s`          |


Routes can be both [tagged and filtered by tags](#tags).


```json
{{ page.route_json }}
```

### Add Route



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Route

<div class="endpoint post indent">{{ prefix }}/routes</div>


##### Create Route Associated to a Specific Service

<div class="endpoint post indent">{{ prefix }}/services/{service name or id}/routes</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier or the `name` attribute of the Service that should be associated to the newly-created Route.


#### Request Body

{{ page.route_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.route_json }}
```


---

### List Routes
{:.badge .dbless}

##### List All Routes

<div class="endpoint get indent">{{ prefix }}/routes</div>


##### List Routes Associated to a Specific Service

<div class="endpoint get indent">{{ prefix }}/services/{service name or id}/routes</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier or the `name` attribute of the Service whose Routes are to be retrieved. When using this endpoint, only Routes associated to the specified Service will be listed.


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.route_data }}
    "next": "http://localhost:8001/routes?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Route
{:.badge .dbless}

##### Retrieve Route

<div class="endpoint get indent">{{ prefix }}/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to retrieve.


##### Retrieve Route Associated to a Specific Service

<div class="endpoint get indent">{{ prefix }}/services/{service name or id}/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to retrieve.
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to retrieve.

{% unless page.edition == "konnect" %}
##### Retrieve Route Associated to a Specific Plugin

<div class="endpoint get indent">/plugins/{plugin id}/route</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Route to be retrieved.

{% endunless %}
#### Response

```
HTTP 200 OK
```

```json
{{ page.route_json }}
```


---
{% unless page.edition == "konnect" %}
### Update Route



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Route

<div class="endpoint patch indent">/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to update.


##### Update Route Associated to a Specific Service

<div class="endpoint patch indent">/services/{service name or id}/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to update.
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to update.


##### Update Route Associated to a Specific Plugin

<div class="endpoint patch indent">/plugins/{plugin id}/route</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Route to be updated.


#### Request Body

{{ page.route_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.route_json }}
```


---
{% endunless %}
### Update Or Create Route



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Route

<div class="endpoint put indent">{{ prefix }}/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to create or update.


##### Create Or Update Route Associated to a Specific Service

<div class="endpoint put indent">{{ prefix }}/services/{service name or id}/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to create or update.
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to create or update.

{% unless page.edition == "konnect" %}
##### Create Or Update Route Associated to a Specific Plugin

<div class="endpoint put indent">/plugins/{plugin id}/route</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Route to be created or updated.

{% endunless %}
#### Request Body

{{ page.route_body }}


Inserts (or replaces) the Route under the requested resource with the
definition specified in the body. The Route will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Route being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Route without specifying `id` (neither in the URL nor in
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

### Delete Route



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Route

<div class="endpoint delete indent">{{ prefix }}/routes/{route name or id}</div>#

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to delete.

{% unless page.edition == "konnect" %}
##### Delete Route Associated to a Specific Service

<div class="endpoint delete indent">/services/{service name or id}/routes/{route name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to delete.
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to delete.
{% endunless %}


#### Response

```
HTTP 204 No Content
```

