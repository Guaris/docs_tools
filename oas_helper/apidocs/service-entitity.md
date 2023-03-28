## Service Object

Service entities, as the name implies, are abstractions of each of your own
upstream services. Examples of Services would be a data transformation
microservice, a billing API, etc.

The main attribute of a Service is its URL (where Kong should proxy traffic
to), which can be set as a single string or by specifying its `protocol`,
`host`, `port` and `path` individually.

Services are associated to Routes (a Service can have many Routes associated
with it). Routes are entry-points in Kong and define rules to match client
requests. Once a Route is matched, Kong proxies the request to its associated
Service. See the [Proxy Reference][proxy-reference] for a detailed explanation
of how Kong proxies traffic.

Services can be both [tagged and filtered by tags](#tags).


```json
{{ page.service_json }}
```

### Add Service



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Service

<div class="endpoint post indent">{{ prefix }}/services</div>

{% unless page.edition == "konnect" %}
##### Create Service Associated to a Specific Certificate

<div class="endpoint post indent">/certificates/{certificate name or id}/services</div>

{:.indent}
Attributes | Description
---:| ---
`certificate name or id`<br>**required** | The unique identifier or the `name` attribute of the Certificate that should be associated to the newly-created Service.

{% endunless %}
#### Request Body

{{ page.service_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.service_json }}
```


---

### List Services
{:.badge .dbless}

##### List All Services

<div class="endpoint get indent">{{ prefix }}/services</div>

{% unless page.edition == "konnect" %}
##### List Services Associated to a Specific Certificate

<div class="endpoint get indent">/certificates/{certificate name or id}/services</div>

{:.indent}
Attributes | Description
---:| ---
`certificate name or id`<br>**required** | The unique identifier or the `name` attribute of the Certificate whose Services are to be retrieved. When using this endpoint, only Services associated to the specified Certificate will be listed.

{% endunless %}
#### Response

```
HTTP 200 OK
```

```json
{
{{ page.service_data }}
    "next": "http://localhost:8001/services?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Service
{:.badge .dbless}

##### Retrieve Service

<div class="endpoint get indent">{{ prefix }}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to retrieve.

{% unless page.edition == "konnect" %}
##### Retrieve Service Associated to a Specific Certificate

<div class="endpoint get indent">/certificates/{certificate id}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to retrieve.
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to retrieve.


##### Retrieve Service Associated to a Specific Route

<div class="endpoint get indent">/routes/{route name or id}/service</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route associated to the Service to be retrieved.


##### Retrieve Service Associated to a Specific Plugin

<div class="endpoint get indent">/plugins/{plugin id}/service</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Service to be retrieved.

{% endunless %}
#### Response

```
HTTP 200 OK
```

```json
{{ page.service_json }}
```


---

### Update Service

{% unless page.edition == "konnect" %}

{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Service

<div class="endpoint patch indent">/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to update.


##### Update Service Associated to a Specific Certificate

<div class="endpoint patch indent">/certificates/{certificate id}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to update.
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to update.


##### Update Service Associated to a Specific Route

<div class="endpoint patch indent">/routes/{route name or id}/service</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route associated to the Service to be updated.


##### Update Service Associated to a Specific Plugin

<div class="endpoint patch indent">/plugins/{plugin id}/service</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Service to be updated.


#### Request Body

{{ page.service_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.service_json }}
```


---
{% endunless %}
### Update Or Create Service


{% unless page.edition == "konnect" %}
{:.note}
> **Note**: This API is not available in DB-less mode.
{% endunless %}
##### Create Or Update Service

<div class="endpoint put indent">{{ prefix }}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to create or update.

{% unless page.edition == "konnect" %}
##### Create Or Update Service Associated to a Specific Certificate

<div class="endpoint put indent">/certificates/{certificate id}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to create or update.
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to create or update.


##### Create Or Update Service Associated to a Specific Route

<div class="endpoint put indent">/routes/{route name or id}/service</div>

{:.indent}
Attributes | Description
---:| ---
`route name or id`<br>**required** | The unique identifier **or** the name of the Route associated to the Service to be created or updated.


##### Create Or Update Service Associated to a Specific Plugin

<div class="endpoint put indent">/plugins/{plugin id}/service</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Service to be created or updated.

{% endunless %}
#### Request Body

{{ page.service_body }}


Inserts (or replaces) the Service under the requested resource with the
definition specified in the body. The Service will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Service being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Service without specifying `id` (neither in the URL nor in
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

### Delete Service



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Service

<div class="endpoint delete indent">{{ prefix }}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to delete.

{% unless page.edition == "konnect" %}
##### Delete Service Associated to a Specific Certificate

<div class="endpoint delete indent">/certificates/{certificate id}/services/{service name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to delete.
`service name or id`<br>**required** | The unique identifier **or** the name of the Service to delete.
{% endunless %}
#### Response

```
HTTP 204 No Content
```



