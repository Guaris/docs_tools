
## SNI Object

An SNI object represents a many-to-one mapping of hostnames to a certificate.
That is, a certificate object can have many hostnames associated with it; when
Kong receives an SSL request, it uses the SNI field in the Client Hello to
lookup the certificate object based on the SNI associated with the certificate.

SNIs can be both [tagged and filtered by tags](#tags).


```json
{{ page.sni_json }}
```

### Add SNI



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create SNI

<div class="endpoint post indent">{{ prefix }}/snis</div>


##### Create SNI Associated to a Specific Certificate

<div class="endpoint post indent">{{ prefix }}/certificates/{certificate name or id}/snis</div>

{:.indent}
Attributes | Description
---:| ---
`certificate name or id`<br>**required** | The unique identifier or the `name` attribute of the Certificate that should be associated to the newly-created SNI.


#### Request Body

{{ page.sni_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.sni_json }}
```


---

### List SNIs
{:.badge .dbless}

##### List All SNIs

<div class="endpoint get indent">{{ prefix }}/snis</div>


##### List SNIs Associated to a Specific Certificate

<div class="endpoint get indent">{{ prefix }}/certificates/{certificate name or id}/snis</div>

{:.indent}
Attributes | Description
---:| ---
`certificate name or id`<br>**required** | The unique identifier or the `name` attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed.


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.sni_data }}
    "next": "http://localhost:8001/snis?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve SNI
{:.badge .dbless}

##### Retrieve SNI

<div class="endpoint get indent">{{ prefix }}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to retrieve.


##### Retrieve SNI Associated to a Specific Certificate

<div class="endpoint get indent">{{ prefix }}/certificates/{certificate id}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to retrieve.
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to retrieve.


#### Response

```
HTTP 200 OK
```

```json
{{ page.sni_json }}
```


---

### Update SNI


{% unless page.edition == "konnect" %}

{:.note}
> **Note**: This API is not available in DB-less mode.


##### Update SNI

<div class="endpoint patch indent">/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to update.


##### Update SNI Associated to a Specific Certificate

<div class="endpoint patch indent">/certificates/{certificate id}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to update.
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to update.


#### Request Body

{{ page.sni_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.sni_json }}
```


---
{% endunless %}

### Update Or Create SNI



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update SNI

<div class="endpoint put indent">{{ prefix }}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to create or update.


##### Create Or Update SNI Associated to a Specific Certificate

<div class="endpoint put indent">{{ prefix }}/certificates/{certificate id}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to create or update.
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to create or update.


#### Request Body

{{ page.sni_body }}


Inserts (or replaces) the SNI under the requested resource with the
definition specified in the body. The SNI will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the SNI being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new SNI without specifying `id` (neither in the URL nor in
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

### Delete SNI



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete SNI

<div class="endpoint delete indent">{{ prefix }}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to delete.


##### Delete SNI Associated to a Specific Certificate

<div class="endpoint delete indent">{{ prefix }}/certificates/{certificate id}/snis/{sni name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to delete.
`sni name or id`<br>**required** | The unique identifier **or** the name of the SNI to delete.


#### Response

```
HTTP 204 No Content
```

