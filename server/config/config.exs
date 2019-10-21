# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :k_portal,
  ecto_repos: [KPortal.Repo]

# Configures the endpoint
config :k_portal, KPortalWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "04UwcRkv+E4eUrijAjlJDyRy82fnfXe33Rp71/T7UUtosXiS6wVaOGr8vPYgrY7V",
  render_errors: [view: KPortalWeb.ErrorView, accepts: ~w(json)],
  pubsub: [name: KPortal.PubSub, adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

config :guardian, Guardian,
  issuer: "KPortalWebId",
  secret_key: Mix.env(),
  serializer: KPortal.GuardianSerializer

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
