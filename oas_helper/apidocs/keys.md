## Keys Object

A Key object holds a representation of asymmetric keys in various formats.
When Kong or a Kong plugin requires a specific public or private key to perform
certain operations, it can use this entity.

Keys can be both [tagged and filtered by tags](#tags).


```json
{{ page.key_json }}
```

### Add Key



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Key

<div class="endpoint post indent">/keys</div>


##### Create Key Associated to a Specific Key Set

<div class="endpoint post indent">/key-sets/{key_set name or id}/keys</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier or the `name` attribute of the Key Set that should be associated to the newly-created Key.


#### Request Body

{{ page.key_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.key_json }}
```


---

### List Keys
{:.badge .dbless}

##### List All Keys

<div class="endpoint get indent">/keys</div>


##### List Keys Associated to a Specific Key Set

<div class="endpoint get indent">/key-sets/{key_set name or id}/keys</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier or the `name` attribute of the Key Set whose Keys are to be retrieved. When using this endpoint, only Keys associated to the specified Key Set will be listed.


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.key_data }}
    "next": "http://localhost:8001/keys?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Key
{:.badge .dbless}

##### Retrieve Key

<div class="endpoint get indent">/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to retrieve.


##### Retrieve Key Associated to a Specific Key Set

<div class="endpoint get indent">/key-sets/{key_set name or id}/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to retrieve.
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to retrieve.


#### Response

```
HTTP 200 OK
```

```json
{{ page.key_json }}
```


---

### Update Key



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Key

<div class="endpoint patch indent">/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to update.


##### Update Key Associated to a Specific Key Set

<div class="endpoint patch indent">/key-sets/{key_set name or id}/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to update.
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to update.


#### Request Body

{{ page.key_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.key_json }}
```


---

### Update Or Create Key



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Key

<div class="endpoint put indent">/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to create or update.


##### Create Or Update Key Associated to a Specific Key Set

<div class="endpoint put indent">/key-sets/{key_set name or id}/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to create or update.
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to create or update.


#### Request Body

{{ page.key_body }}


Inserts (or replaces) the Key under the requested resource with the
definition specified in the body. The Key will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Key being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Key without specifying `id` (neither in the URL nor in
the body), then it will be auto-generated.

Notice that specifying a `name` in the URL and a different one in the request
body is not allowed.


#### Response

```
HTTP 200 OK
```

See POST and PATCH responses.


---

### Delete Key



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Key

<div class="endpoint delete indent">/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to delete.


##### Delete Key Associated to a Specific Key Set

<div class="endpoint delete indent">/key-sets/{key_set name or id}/keys/{key name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to delete.
`key name or id`<br>**required** | The unique identifier **or** the name of the Key to delete.


#### Response

```
HTTP 204 No Content
```


---

## Key Sets Entity

A Key Set object holds a collection of asymmetric key objects.
This entity allows to logically group keys by their purpose.

Key Sets can be both [tagged and filtered by tags](#tags).


```json
{{ page.key_set_json }}
```

### Add Key Set



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Key Set

<div class="endpoint post indent">/key-sets</div>


#### Request Body

{{ page.key_set_body }}


#### Response

```
HTTP 201 Created
```

```json
{{ page.key_set_json }}
```


---

### List Key Sets
{:.badge .dbless}

##### List All Key Sets

<div class="endpoint get indent">/key-sets</div>


#### Response

```
HTTP 200 OK
```

```json
{
{{ page.key_set_data }}
    "next": "http://localhost:8001/key-sets?offset=6378122c-a0a1-438d-a5c6-efabae9fb969"
}
```


---

### Retrieve Key Set
{:.badge .dbless}

##### Retrieve Key Set

<div class="endpoint get indent">/key-sets/{key_set name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to retrieve.


#### Response

```
HTTP 200 OK
```

```json
{{ page.key_set_json }}
```


---

### Update Key Set




{:.note}
> **Note**: This API is not available in DB-less mode.

##### Update Key Set

<div class="endpoint patch indent">/key-sets/{key_set name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to update.


#### Request Body

{{ page.key_set_body }}


#### Response

```
HTTP 200 OK
```

```json
{{ page.key_set_json }}
```


---

### Update Or Create Key Set



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Create Or Update Key Set

<div class="endpoint put indent">/key-sets/{key_set name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to create or update.


#### Request Body

{{ page.key_set_body }}


Inserts (or replaces) the Key Set under the requested resource with the
definition specified in the body. The Key Set will be identified via the `name
or id` attribute.

When the `name or id` attribute has the structure of a UUID, the Key Set being
inserted/replaced will be identified by its `id`. Otherwise it will be
identified by its `name`.

When creating a new Key Set without specifying `id` (neither in the URL nor in
the body), then it will be auto-generated.

Notice that specifying a `name` in the URL and a different one in the request
body is not allowed.


#### Response

```
HTTP 200 OK
```

See POST and PATCH responses.


---

### Delete Key Set



{:.note}
> **Note**: This API is not available in DB-less mode.

##### Delete Key Set

<div class="endpoint delete indent">/key-sets/{key_set name or id}</div>

{:.indent}
Attributes | Description
---:| ---
`key_set name or id`<br>**required** | The unique identifier **or** the name of the Key Set to delete.


#### Response

```
HTTP 204 No Content
```


---

### List Keys Associated to A Specific Key-set
{:.badge .dbless}

Lists all keys within the specifified key set.



##### Retrieve Key Set Associated to a Specific Key

<div class="endpoint get indent">/keys/{key name or id}/set</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key associated to the Key Set to be retrieved.


#### Response

 ```
 HTTP 200 OK
 ```

 ``` json
{
   "data": [
     {
       "id": "46CA83EE-671C-11ED-BFAB-2FE47512C77A",
       "name": "my-key_set",
       "tags": ["google-keys", "mozilla-keys"],
       "created_at": 1422386534,
       "updated_at": 1422386534
   }, {
       "id": "57532ECE-6720-11ED-9297-279D4320B841",
       "name": "my-key_set",
       "tags": ["production", "staging", "development"],
       "created_at": 1422386534,
       "updated_at": 1422386534
   }]
 }
 ```


---

### Updates A Key Within A Key-set



{:.note}
> **Note**: This API is not available in DB-less mode.

Updates a key within a key-set



##### Update Key Set Associated to a Specific Key

<div class="endpoint patch indent">/keys/{key name or id}/set</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key associated to the Key Set to be updated.


#### Response

```
HTTP 201 Created
```


---

### Create A Key Within A Key-set



{:.note}
> **Note**: This API is not available in DB-less mode.

Creates a key



##### Create Or Update Key Set Associated to a Specific Key

<div class="endpoint put indent">/keys/{key name or id}/set</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key associated to the Key Set to be created or updated.


#### Response

```
HTTP 201 Created
```


---

### Delete Key Within Key-set



{:.note}
> **Note**: This API is not available in DB-less mode.

Delete a key that is associated with this key-set



##### Delete Key Set Associated to a Specific Key

<div class="endpoint delete indent">/keys/{key name or id}/set</div>

{:.indent}
Attributes | Description
---:| ---
`key name or id`<br>**required** | The unique identifier **or** the name of the Key associated to the Key Set to be deleted.


#### Response

```
HTTP 204 No Content
```