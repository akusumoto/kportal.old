defmodule KPortalWeb.PartController do
  use KPortalWeb, :controller

  alias KPortal.Accounts
  alias KPortal.Accounts.Part

  action_fallback KPortalWeb.FallbackController

  def index(conn, _params) do
    parts = Accounts.list_parts()
    render(conn, "index.json", parts: parts)
  end

  def create(conn, part_params) do
    with {:ok, %Part{} = part} <- Accounts.create_part(part_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.part_path(conn, :show, part))
      |> render("show.json", part: part)
    end
  end

  def show(conn, %{"id" => id}) do
    part = Accounts.get_part!(id)
    render(conn, "show.json", part: part)
  end

  def update(conn, %{"id" => id, "part" => part_params}) do
    part = Accounts.get_part!(id)

    with {:ok, %Part{} = part} <- Accounts.update_part(part, part_params) do
      render(conn, "show.json", part: part)
    end
  end

  def delete(conn, %{"id" => id}) do
    part = Accounts.get_part!(id)

    with {:ok, %Part{}} <- Accounts.delete_part(part) do
      send_resp(conn, :no_content, "")
    end
  end
end
