defmodule KPortal.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :account, :string
    field :password, :string
    field :name, :string
    field :nickname, :string
    belongs_to :part, KPortal.Accounts.Part
    field :email, :string
    field :home_address, :string
    field :work_address, :string
    belongs_to :type, KPortal.Accounts.Type
    field :emergency_number, :string
    field :note, :string

    timestamps()
  end

  @doc false
  def changeset(user, attrs) do
    user
    |> cast(attrs, [:account,
                    :password,
                    :name,
                    :nickname,
                    :part,
                    :email,
                    :home_address,
                    :work_address,
                    :type,
                    :emergency_number,
                    :note])
    |> validate_required([:account, :password, :email, :name, :nickname, :type, :part])
  end
end
