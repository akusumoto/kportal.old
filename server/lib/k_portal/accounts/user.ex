defmodule KPortal.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  alias KPortal.Accounts.{Part, Type}

  schema "users" do
    field :account, :string
    field :password, :string
    field :name, :string
    field :nickname, :string
    belongs_to :part, Part
    field :email, :string
    field :home_address, :string
    field :work_address, :string
    belongs_to :type, Type
    field :emergency_number, :string
    field :note, :string

    timestamps()
  end

  @doc false
  def changeset(user, attrs) do
    user
    |> cast(attrs, [:account, :password, :name, :nickname, :email, :home_address, :work_address, :emergency_number, :note, :part_id, :type_id])
    |> validate_required([:account, :password, :email, :name, :nickname, :part_id, :type_id])
  end
end
