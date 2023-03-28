
## Certificate Object

A certificate object represents a public certificate, and can be optionally paired with the
corresponding private key. These objects are used by Kong to handle SSL/TLS termination for
encrypted requests, or for use as a trusted CA store when validating peer certificate of
client/service. Certificates are optionally associated with SNI objects to
tie a cert/key pair to one or more hostnames.

If intermediate certificates are required in addition to the main
certificate, they should be concatenated together into one string according to
the following order: main certificate on the top, followed by any intermediates.

Certificates can be both [tagged and filtered by tags](#tags).


```json
{{ page.certificate_json }}
```

### Add Certificate



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Certificate

<div class="endpoint post indent">{{ prefix }}/certificates</div>


#### Request Body

{{ page.certificate_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.certificate_json }}
```


---

### List Certificates
{:.badge .dbless}

##### List All Certificates

<div class="endpoint get indent">{{ prefix }}/certificates</div>


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.certificate_data }}
    "next": "http://localhost:8001/certificates?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Certificate
{:.badge .dbless}

##### Retrieve Certificate

<div class="endpoint get indent">{{ prefix }}/certificates/{certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to retrieve.

{% unless page.edition == "konnect" %}

##### Retrieve Certificate Associated to a Specific Upstream

<div class="endpoint get indent">/upstreams/{upstream name or id}/client_certificate</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream associated to the Certificate to be retrieved.

{% endunless %}
#### Response

```
HTTP 200 OK
```

```json
{{ page.certificate_json }}
```


---

### Update Certificate


{% unless page.edition == "konnect" %}

{:.note}
> **Note**: This API is not available in DB-less mode.
##### Update Certificate

<div class="endpoint patch indent">/certificates/{certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to update.


##### Update Certificate Associated to a Specific Upstream

<div class="endpoint patch indent">/upstreams/{upstream name or id}/client_certificate</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream associated to the Certificate to be updated.


#### Request Body

{{ page.certificate_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.certificate_json }}
```

{% endunless %}
---

### Update Or Create Certificate



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Certificate

<div class="endpoint put indent">{{ prefix }}/certificates/{certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to create or update.

{% unless page.edition == "konnect" %}

##### Create Or Update Certificate Associated to a Specific Upstream

<div class="endpoint put indent">/upstreams/{upstream name or id}/client_certificate</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream associated to the Certificate to be created or updated.
{% endunless %}

#### Request Body

{{ page.certificate_body }}


Inserts (or replaces) the Certificate under the requested resource with the
definition specified in the body. The Certificate will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Certificate being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Certificate without specifying `id` (neither in the URL nor in
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

### Delete Certificate



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Certificate

<div class="endpoint delete indent">{{ prefix }}/certificates/{certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`certificate id`<br>**required** | The unique identifier of the Certificate to delete.

{% unless page.edition == "konnect" %}

##### Delete Certificate Associated to a Specific Upstream

<div class="endpoint delete indent">/upstreams/{upstream name or id}/client_certificate</div>

{:.indent}
Attributes | Description
---:| ---
`upstream name or id`<br>**required** | The unique identifier **or** the name of the Upstream associated to the Certificate to be deleted.

{% endunless %}

#### Response

```
HTTP 204 No Content
```


---

## CA Certificate Object

A CA certificate object represents a trusted CA. These objects are used by Kong to
verify the validity of a client or server certificate.

CA Certificates can be both [tagged and filtered by tags](#tags).


```json
{{ page.ca_certificate_json }}
```

### Add CA Certificate



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create CA Certificate

<div class="endpoint post indent">{{ prefix }}/ca_certificates</div>


#### Request Body

{{ page.ca_certificate_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.ca_certificate_json }}
```


---

### List CA Certificates
{:.badge .dbless}

##### List All CA Certificates

<div class="endpoint get indent">{{ prefix }}/ca_certificates</div>


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.ca_certificate_data }}
    "next": "http://localhost:8001/ca_certificates?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve CA Certificate
{:.badge .dbless}

##### Retrieve CA Certificate

<div class="endpoint get indent">{{ prefix }}/ca_certificates/{ca_certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`ca_certificate id`<br>**required** | The unique identifier of the CA Certificate to retrieve.


#### Response

```
HTTP 200 OK
```

```json
{{ page.ca_certificate_json }}
```


---

### Update CA Certificate


{% unless page.edition == "konnect" %}

{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update CA Certificate

<div class="endpoint patch indent">/ca_certificates/{ca_certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`ca_certificate id`<br>**required** | The unique identifier of the CA Certificate to update.


#### Request Body

{{ page.ca_certificate_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.ca_certificate_json }}
```

{% endunless %}
---

### Update Or Create CA Certificate



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update CA Certificate

<div class="endpoint put indent">{{ prefix }}/ca_certificates/{ca_certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`ca_certificate id`<br>**required** | The unique identifier of the CA Certificate to create or update.


#### Request Body

{{ page.ca_certificate_body }}


Inserts (or replaces) the CA Certificate under the requested resource with the
definition specified in the body. The CA Certificate will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the CA Certificate being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new CA Certificate without specifying `id` (neither in the URL nor in
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

### Delete CA Certificate



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete CA Certificate

<div class="endpoint delete indent">{{ prefix }}/ca_certificates/{ca_certificate id}</div>

{:.indent}
Attributes | Description
---:| ---
`ca_certificate id`<br>**required** | The unique identifier of the CA Certificate to delete.


#### Response

```
HTTP 204 No Content
```

