defmodule KPortal.Repo do
  use Ecto.Repo,
    otp_app: :k_portal,
    adapter: Ecto.Adapters.Postgres
end
