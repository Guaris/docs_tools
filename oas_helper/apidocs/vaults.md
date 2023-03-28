
## Vaults Object

Vault object are used to configure different Vault connectors. Examples of
Vaults are Environment Variables, Hashicorp Vault and AWS Secrets Manager.

Configuring a Vault allows referencing the secrets with other entities. For
example a certificate entity can store a reference to a certificate and key,
stored in a vault, instead of storing the certificate and key within the
entity. This allows a proper separation of secrets and configuration and
prevents secret sprawl.

Vaults can be both [tagged and filtered by tags](#tags).


```json
{{ page.vault_json }}
```

### Add Vault



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Vault

<div class="endpoint post indent">{{ prefix }}/vaults</div>


#### Request Body

{{ page.vault_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.vault_json }}
```


---

### List Vaults
{:.badge .dbless}

##### List All Vaults

<div class="endpoint get indent">{{ prefix }}/vaults</div>


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.vault_data }}
    "next": "http://localhost:8001/vaults?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Vault
{:.badge .dbless}

##### Retrieve Vault

<div class="endpoint get indent">{{ prefix }}/vaults/{vault prefix or id}</div>

{:.indent}
Attributes | Description
---:| ---
`vault prefix or id`<br>**required** | The unique identifier **or** the prefix of the Vault to retrieve.


#### Response

```
HTTP 200 OK
```

```json
{{ page.vault_json }}
```


---

### Update Vault


{% unless page.edition == "konnect" %}

{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Vault

<div class="endpoint patch indent">/vaults/{vault prefix or id}</div>

{:.indent}
Attributes | Description
---:| ---
`vault prefix or id`<br>**required** | The unique identifier **or** the prefix of the Vault to update.


#### Request Body

{{ page.vault_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.vault_json }}
```


---
{% endunless %}

### Update Or Create Vault



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Vault

<div class="endpoint put indent">{{ prefix }}/vaults/{vault prefix or id}</div>

{:.indent}
Attributes | Description
---:| ---
`vault prefix or id`<br>**required** | The unique identifier **or** the prefix of the Vault to create or update.


#### Request Body

{{ page.vault_body }}


Inserts (or replaces) the Vault under the requested resource with the
definition specified in the body. The Vault will be identified via the `prefix
or id` attribute.

When the `prefix or id` attribute has the structure of a UUID, the Vault being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `prefix`.

When creating a new Vault without specifying `id` (neither in the URL nor in
the body), then it will be auto-generated.

Notice that specifying a `prefix` in the URL and a different one in the request
body is not allowed.


#### Response

```
HTTP 200 OK
```
{% unless page.edition == "konnect" %}
See POST and PATCH responses.
{% endunless %}

---

### Delete Vault



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Vault

<div class="endpoint delete indent">{{ prefix }}/vaults/{vault prefix or id}</div>

{:.indent}
Attributes | Description
---:| ---
`vault prefix or id`<br>**required** | The unique identifier **or** the prefix of the Vault to delete.


#### Response

```
HTTP 204 No Content
```

