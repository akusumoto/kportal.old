defmodule KPortal.Repo.Migrations.CreateUsers do
  use Ecto.Migration

  def change do
    create table(:parts) do
      add :name, :string

      timestamps()
    end

    create table(:types) do
      add :name, :string

      timestamps()
    end

    create table(:users) do
      add :account, :string
      add :password, :string
      add :name, :string
      add :nickname, :string
      add :part_id, references(:parts)
      add :email, :string
      add :home_address, :string
      add :work_address, :string
      add :type_id, references(:types)
      add :emergency_number, :string
      add :note, :text

      timestamps()
    end

  end
end
