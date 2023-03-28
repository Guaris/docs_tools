
## Plugin Object

A Plugin entity represents a plugin configuration that will be executed during
the HTTP request/response lifecycle. It is how you can add functionalities
to Services that run behind Kong, like Authentication or Rate Limiting for
example. You can find more information about how to install and what values
each plugin takes by visiting the [Kong Hub](https://docs.konghq.com/hub/).

When adding a Plugin Configuration to a Service, every request made by a client to
that Service will run said Plugin. If a Plugin needs to be tuned to different
values for some specific Consumers, you can do so by creating a separate
plugin instance that specifies both the Service and the Consumer, through the
`service` and `consumer` fields.

Plugins can be both [tagged and filtered by tags](#tags).


```json
{{ page.plugin_json }}
```

See the [Precedence](#precedence) section below for more details.

#### Precedence

A plugin will always be run once and only once per request. But the
configuration with which it will run depends on the entities it has been
configured for.
{% unless page.edition == "konnect" %}
Plugins can be configured for various entities, combination of entities, or
even globally. This is useful, for example, when you wish to configure a plugin
a certain way for most requests, but make _authenticated requests_ behave
slightly differently.

Therefore, there exists an order of precedence for running a plugin when it has
been applied to different entities with different configurations. The rule of
thumb is: the more specific a plugin is with regards to how many entities it
has been configured on, the higher its priority.

The complete order of precedence when a plugin has been configured multiple
times is:

1. Plugins configured on a combination of: a Route, a Service, and a Consumer.
    (Consumer means the request must be authenticated).
2. Plugins configured on a combination of a Route and a Consumer.
    (Consumer means the request must be authenticated).
3. Plugins configured on a combination of a Service and a Consumer.
    (Consumer means the request must be authenticated).
4. Plugins configured on a combination of a Route and a Service.
5. Plugins configured on a Consumer.
    (Consumer means the request must be authenticated).
6. Plugins configured on a Route.
7. Plugins configured on a Service.
8. Plugins configured to run globally.
{% endunless %}
**Example**: if the `rate-limiting` plugin is applied twice (with different
configurations): for a Service (Plugin config A), and for a Consumer (Plugin
config B), then requests authenticating this Consumer will run Plugin config B
and ignore A. However, requests that do not authenticate this Consumer will
fallback to running Plugin config A. Note that if config B is disabled
(its `enabled` flag is set to `false`), config A will apply to requests that
would have otherwise matched config B.


### Add Plugin



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Plugin

<div class="endpoint post indent">{{ prefix }}/plugins</div>


##### Create Plugin Associated to a Specific Route

<div class="endpoint post indent">{{ prefix }}/routes/{route name or id}/plugins</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier or the `name` attribute of the Route that should be associated to the newly-created Plugin.


##### Create Plugin Associated to a Specific Service

<div class="endpoint post indent">{{ prefix }}/services/{service name or id}/plugins</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier or the `name` attribute of the Service that should be associated to the newly-created Plugin.


##### Create Plugin Associated to a Specific Consumer

<div class="endpoint post indent">{{ prefix }}/consumers/{consumer name or id}/plugins</div>

{:.indent}
Attributes | Description
---:| ---
`consumer name or id`<br>**required** | The unique identifier or the `name` attribute of the Consumer that should be associated to the newly-created Plugin.


#### Request Body

{{ page.plugin_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.plugin_json }}
```


---

### List Plugins
{:.badge .dbless}

##### List All Plugins

<div class="endpoint get indent">{{ prefix }}/plugins</div>


##### List Plugins Associated to a Specific Route

<div class="endpoint get indent">{{ prefix }}/routes/{route name or id}/plugins</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier or the `name` attribute of the Route whose Plugins are to be retrieved. When using this endpoint, only Plugins associated to the specified Route will be listed.


##### List Plugins Associated to a Specific Service

<div class="endpoint get indent">{{ prefix }}/services/{service name or id}/plugins</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier or the `name` attribute of the Service whose Plugins are to be retrieved. When using this endpoint, only Plugins associated to the specified Service will be listed.


##### List Plugins Associated to a Specific Consumer

<div class="endpoint get indent">{{ prefix }}/consumers/{consumer name or id}/plugins</div>

{:.indent}
Attributes | Description
---:| ---
`consumer name or id`<br>**required** | The unique identifier or the `name` attribute of the Consumer whose Plugins are to be retrieved. When using this endpoint, only Plugins associated to the specified Consumer will be listed.


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.plugin_data }}
    "next": "http://localhost:8001/plugins?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Plugin
{:.badge .dbless}

##### Retrieve Plugin

<div class="endpoint get indent">{{ prefix }}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin to retrieve.


##### Retrieve Plugin Associated to a Specific Route

<div class="endpoint get indent">{{ prefix }}/routes/{route name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to retrieve.
`plugin id`<br>**required** | The unique identifier of the Plugin to retrieve.


##### Retrieve Plugin Associated to a Specific Service

<div class="endpoint get indent">{{ prefix }}/services/{service name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to retrieve.
`plugin id`<br>**required** | The unique identifier of the Plugin to retrieve.


##### Retrieve Plugin Associated to a Specific Consumer

<div class="endpoint get indent">{{ prefix }}/consumers/{consumer username or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to retrieve.
`plugin id`<br>**required** | The unique identifier of the Plugin to retrieve.


#### Response

```
HTTP 200 OK
```

```json
{{ page.plugin_json }}
```


---
{% unless page.edition == "konnect" %}

### Update Plugin



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Plugin

<div class="endpoint patch indent">/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin to update.


##### Update Plugin Associated to a Specific Route

<div class="endpoint patch indent">/routes/{route name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to update.
`plugin id`<br>**required** | The unique identifier of the Plugin to update.


##### Update Plugin Associated to a Specific Service

<div class="endpoint patch indent">/services/{service name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to update.
`plugin id`<br>**required** | The unique identifier of the Plugin to update.


##### Update Plugin Associated to a Specific Consumer

<div class="endpoint patch indent">/consumers/{consumer username or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to update.
`plugin id`<br>**required** | The unique identifier of the Plugin to update.


#### Request Body

{{ page.plugin_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.plugin_json }}
```

{% endunless %}
---

### Update Or Create Plugin



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Plugin

<div class="endpoint put indent">{{ prefix }}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin to create or update.


##### Create Or Update Plugin Associated to a Specific Route

<div class="endpoint put indent">{{ prefix }}/routes/{route name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to create or update.
`plugin id`<br>**required** | The unique identifier of the Plugin to create or update.


##### Create Or Update Plugin Associated to a Specific Service

<div class="endpoint put indent">{{ prefix }}/services/{service name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to create or update.
`plugin id`<br>**required** | The unique identifier of the Plugin to create or update.


##### Create Or Update Plugin Associated to a Specific Consumer

<div class="endpoint put indent">{{ prefix }}/consumers/{consumer username or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to create or update.
`plugin id`<br>**required** | The unique identifier of the Plugin to create or update.


#### Request Body

{{ page.plugin_body }}


Inserts (or replaces) the Plugin under the requested resource with the
definition specified in the body. The Plugin will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Plugin being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Plugin without specifying `id` (neither in the URL nor in
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

### Delete Plugin



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Plugin

<div class="endpoint delete indent">{{ prefix }}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin to delete.


##### Delete Plugin Associated to a Specific Route

<div class="endpoint delete indent">{{ prefix }}/routes/{route name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route to delete.
`plugin id`<br>**required** | The unique identifier of the Plugin to delete.


##### Delete Plugin Associated to a Specific Service

<div class="endpoint delete indent">{{ prefix }}/services/{service name or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to delete.
`plugin id`<br>**required** | The unique identifier of the Plugin to delete.


##### Delete Plugin Associated to a Specific Consumer

<div class="endpoint delete indent">{{ prefix }}/consumers/{consumer username or id}/plugins/{plugin id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to delete.
`plugin id`<br>**required** | The unique identifier of the Plugin to delete.


#### Response

```
HTTP 204 No Content
```


---
{% unless page.edition == "konnect" %}

### Retrieve Enabled Plugins
{:.badge .dbless}

Retrieve a list of all installed plugins on the Kong node.

<div class="endpoint get">/plugins/enabled</div>

#### Response

```
HTTP 200 OK
```

```json
{
    "enabled_plugins": [
        "jwt",
        "acl",
        "cors",
        "oauth2",
        "tcp-log",
        "udp-log",
        "file-log",
        "http-log",
        "key-auth",
        "hmac-auth",
        "basic-auth",
        "ip-restriction",
        "request-transformer",
        "response-transformer",
        "request-size-limiting",
        "rate-limiting",
        "response-ratelimiting",
        "aws-lambda",
        "bot-detection",
        "correlation-id",
        "datadog",
        "galileo",
        "ldap-auth",
        "loggly",
        "statsd",
        "syslog"
    ]
}
```

