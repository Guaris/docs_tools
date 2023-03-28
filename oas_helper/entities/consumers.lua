local typedefs = require "kong.db.schema.typedefs"

local description = [[
  Service entities are abstractions of of individual upstream services. Examples of Services would be a data transformation microservice, a billing API, etc.
  - [Documentation](https://docs.konghq.com/gateway/latest/admin-api/#service-object)

]]
return {
  name         = "consumers",
  primary_key  = { "id" },
  endpoint_key = "username",
  workspaceable = true,

  fields = {
    { id             = typedefs.uuid, },
    { created_at     = typedefs.auto_timestamp_s },
    { updated_at     = typedefs.auto_timestamp_s },
    { username       = { type = "string",  unique = true, description: "test" }, },
    { custom_id      = { type = "string",  unique = true }, },
    { tags           = typedefs.tags },
  },

  entity_checks = {
    { at_least_one_of = { "custom_id", "username" } },
  },
}
