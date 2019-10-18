defmodule KPortal.Accounts.Type do
  use Ecto.Schema
  import Ecto.Changeset

  alias KPortal.Accounts.User

  schema "types" do
    field :name, :string
    has_many :users, User

    timestamps()
  end

  @doc false
  def changeset(type, attrs) do
    type
    |> cast(attrs, [:name])
    |> validate_required([:name])
  end
end
