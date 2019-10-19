defmodule KPortal.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  alias KPortal.Accounts.{Part, Type}

  @input       [:account, :password, :email, :name, :nickname, :home_address, :work_address, :emergency_number, :note, :part_id, :type_id]
  @required    [:account, :password, :email, :name, :nickname,                                                         :part_id, :type_id]
  @output [:id, :account, :password, :email, :name, :nickname, :home_address, :work_address, :emergency_number, :note, :part,    :type]

  defmacro list_input, do: @input
  defmacro list_output, do: @output
  defmacro list_required, do: @required

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
    |> cast(attrs, @input)
    |> validate_required(@required)
  end
end

defimpl Jason.Encoder, for: KPortal.Accounts.User do
  require KPortal.Accounts.User

  def encode(value, opts) do
    value
    |> Map.take(KPortal.Accounts.User.list_output)
    |> Jason.Encode.map(opts)
  end
end
