defmodule KPortal.Accounts.Type do
  use Ecto.Schema
  import Ecto.Changeset

  alias KPortal.Accounts.User

  @input [:name]
  @required [:name]
  @output [:id, :name]

  defmacro list_input, do: @input
  defmacro list_output, do: @output
  defmacro list_required, do: @required

  schema "types" do
    field :name, :string
    has_many :users, User

    timestamps()
  end

  @doc false
  def changeset(type, attrs) do
    type
    |> cast(attrs, @input)
    |> validate_required(@required)
  end

end

defimpl Jason.Encoder, for: KPortal.Accounts.Type do
  require KPortal.Accounts.Type

  def encode(value, opts) do
    value
    |> Map.take(KPortal.Accounts.Type.list_output)
    |> Jason.Encode.map(opts)
  end
end
