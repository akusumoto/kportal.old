defmodule KPortal.Accounts.Part do
  use Ecto.Schema
  import Ecto.Changeset

  alias KPortal.Accounts.User

  @input [:name]
  @required [:name]
  @output [:id, :name]

  defmacro list_input, do: @input
  defmacro list_output, do: @output
  defmacro list_required, do: @required

  schema "parts" do
    field :name, :string
    has_many :users, User

    timestamps()
  end

  @doc false
  def changeset(part, attrs) do
    part
    |> cast(attrs, @input)
    |> validate_required(@required)
  end
end

defimpl Jason.Encoder, for: KPortal.Accounts.Part do
  require KPortal.Accounts.Part

  def encode(value, opts) do
    value
    |> Map.take(KPortal.Accounts.Part.list_output)
    |> Jason.Encode.map(opts)
  end
end
