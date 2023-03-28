
## Consumer Object

The Consumer object represents a consumer - or a user - of a Service. You can
either rely on Kong as the primary datastore, or you can map the consumer list
with your database to keep consistency between Kong and your existing primary
datastore.

Consumers can be both [tagged and filtered by tags](#tags).


```json
{{ page.consumer_json }}
```

### Add Consumer



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Consumer

<div class="endpoint post indent">{{ prefix }}/consumers</div>


#### Request Body

{{ page.consumer_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.consumer_json }}
```


---

### List Consumers
{:.badge .dbless}

##### List All Consumers

<div class="endpoint get indent">{{ prefix }}/consumers</div>


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.consumer_data }}
    "next": "http://localhost:8001/consumers?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Consumer
{:.badge .dbless}

##### Retrieve Consumer

<div class="endpoint get indent">{{ prefix }}/consumers/{consumer username or id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to retrieve.

{% unless page.edition == "konnect" %}
##### Retrieve Consumer Associated to a Specific Plugin

<div class="endpoint get indent">/plugins/{plugin id}/consumer</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Consumer to be retrieved.

{% endunless %}

#### Response

```
HTTP 200 OK
```

```json
{{ page.consumer_json }}
```


---
{% unless page.edition == "konnect" %}

### Update Consumer



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Consumer

<div class="endpoint patch indent">/consumers/{consumer username or id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to update.


##### Update Consumer Associated to a Specific Plugin

<div class="endpoint patch indent">/plugins/{plugin id}/consumer</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Consumer to be updated.


#### Request Body

{{ page.consumer_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.consumer_json }}
```


---
{% endunless %}
### Update Or Create Consumer



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Consumer

<div class="endpoint put indent">{{ prefix }}/consumers/{consumer username or id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to create or update.

{% unless page.edition == "konnect" %}
##### Create Or Update Consumer Associated to a Specific Plugin

<div class="endpoint put indent">/plugins/{plugin id}/consumer</div>

{:.indent}
Attributes | Description
---:| ---
`plugin id`<br>**required** | The unique identifier of the Plugin associated to the Consumer to be created or updated.

{% endunless %}
#### Request Body

{{ page.consumer_body }}


Inserts (or replaces) the Consumer under the requested resource with the
definition specified in the body. The Consumer will be identified via the `username
or id` attribute.

When the `username or id` attribute has the structure of a UUID, the Consumer being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `username`.

When creating a new Consumer without specifying `id` (neither in the URL nor in
the body), then it will be auto-generated.

Notice that specifying a `username` in the URL and a different one in the request
body is not allowed.


#### Response

```
HTTP 200 OK
```

{% unless page.edition == "konnect" %}
See POST and PATCH responses.
{% endunless %}

---

### Delete Consumer



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Consumer

<div class="endpoint delete indent">{{ prefix }}/consumers/{consumer username or id}</div>

{:.indent}
Attributes | Description
---:| ---
`consumer username or id`<br>**required** | The unique identifier **or** the username of the Consumer to delete.


#### Response

```
HTTP 204 No Content
```


---