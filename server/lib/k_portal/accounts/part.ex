defmodule KPortal.Accounts.Part do
  use Ecto.Schema
  import Ecto.Changeset

  alias KPortal.Accounts.User

  schema "parts" do
    field :name, :string
    has_many :users, User

    timestamps()
  end

  @doc false
  def changeset(part, attrs) do
    part
    |> cast(attrs, [:name])
    |> validate_required([:name])
  end
end
