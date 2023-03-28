## Tags

Tags are strings associated to entities in Kong.

Tags can contain almost all UTF-8 characters, with the following exceptions:

- `,` and `/` are reserved for filtering tags with "and" and "or", so they are not allowed in tags.
- Non-printable ASCII (for example, the space character) is not allowed.

Most core entities can be *tagged* via their `tags` attribute, upon creation or edition.

Tags can be used to filter core entities as well, via the `?tags` querystring parameter.

For example: if you normally get a list of all the Services by doing:

```
GET /services
```

You can get the list of all the Services tagged `example` by doing:

```
GET /services?tags=example
```

Similarly, if you want to filter Services so that you only get the ones tagged `example` *and*
`admin`, you can do that like so:

```
GET /services?tags=example,admin
```

Finally, if you wanted to filter the Services tagged `example` *or* `admin`, you could use:

```
GET /services?tags=example/admin
```

Some notes:

* A maximum of 5 tags can be queried simultaneously in a single request with `,` or `/`
* Mixing operators is not supported: if you try to mix `,` with `/` in the same querystring,
  you will receive an error.
* You may need to quote and/or escape some characters when using them from the
  command line.
* Filtering by `tags` is not supported in foreign key relationship endpoints. For example,
  the `tags` parameter will be ignored in a request such as `GET /services/foo/routes?tags=a,b`
* `offset` parameters are not guaranteed to work if the `tags` parameter is altered or removed


### List All Tags

Returns a paginated list of all the tags in the system.

The list of entities will not be restricted to a single entity type: all the
entities tagged with tags will be present on this list.

If an entity is tagged with more than one tag, the `entity_id` for that entity
will appear more than once in the resulting list. Similarly, if several entities
have been tagged with the same tag, the tag will appear in several items of this list.


<div class="endpoint get">/tags</div>

#### Response

```
HTTP 200 OK
```

``` json
{
    {
      "data": [
        { "entity_name": "services",
          "entity_id": "acf60b10-125c-4c1a-bffe-6ed55daefba4",
          "tag": "s1",
        },
        { "entity_name": "services",
          "entity_id": "acf60b10-125c-4c1a-bffe-6ed55daefba4",
          "tag": "s2",
        },
        { "entity_name": "routes",
          "entity_id": "60631e85-ba6d-4c59-bd28-e36dd90f6000",
          "tag": "s1",
        },
        ...
      ],
      "offset": "c47139f3-d780-483d-8a97-17e9adc5a7ab",
      "next": "/tags?offset=c47139f3-d780-483d-8a97-17e9adc5a7ab",
    }
}
```


---

### List Entity Ids by Tag

Returns the entities that have been tagged with the specified tag.

The list of entities will not be restricted to a single entity type: all the
entities tagged with tags will be present on this list.


<div class="endpoint get">/tags/{tags}</div>

#### Response

```
HTTP 200 OK
```

``` json
{
    {
      "data": [
        { "entity_name": "services",
          "entity_id": "c87440e1-0496-420b-b06f-dac59544bb6c",
          "tag": "example",
        },
        { "entity_name": "routes",
          "entity_id": "8a99e4b1-d268-446b-ab8b-cd25cff129b1",
          "tag": "example",
        },
        ...
      ],
      "offset": "1fb491c4-f4a7-4bca-aeba-7f3bcee4d2f9",
      "next": "/tags/example?offset=1fb491c4-f4a7-4bca-aeba-7f3bcee4d2f9",
    }
}
```

