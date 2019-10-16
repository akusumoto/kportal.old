defmodule KPortalWeb.PartControllerTest do
  use KPortalWeb.ConnCase

  alias KPortal.Accounts
  alias KPortal.Accounts.Part

  @create_attrs %{
    name: "some name"
  }
  @update_attrs %{
    name: "some updated name"
  }
  @invalid_attrs %{name: nil}

  def fixture(:part) do
    {:ok, part} = Accounts.create_part(@create_attrs)
    part
  end

  setup %{conn: conn} do
    {:ok, conn: put_req_header(conn, "accept", "application/json")}
  end

  describe "index" do
    test "lists all parts", %{conn: conn} do
      conn = get(conn, Routes.part_path(conn, :index))
      assert json_response(conn, 200)["data"] == []
    end
  end

  describe "create part" do
    test "renders part when data is valid", %{conn: conn} do
      conn = post(conn, Routes.part_path(conn, :create), part: @create_attrs)
      assert %{"id" => id} = json_response(conn, 201)["data"]

      conn = get(conn, Routes.part_path(conn, :show, id))

      assert %{
               "id" => id,
               "name" => "some name"
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn} do
      conn = post(conn, Routes.part_path(conn, :create), part: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "update part" do
    setup [:create_part]

    test "renders part when data is valid", %{conn: conn, part: %Part{id: id} = part} do
      conn = put(conn, Routes.part_path(conn, :update, part), part: @update_attrs)
      assert %{"id" => ^id} = json_response(conn, 200)["data"]

      conn = get(conn, Routes.part_path(conn, :show, id))

      assert %{
               "id" => id,
               "name" => "some updated name"
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn, part: part} do
      conn = put(conn, Routes.part_path(conn, :update, part), part: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "delete part" do
    setup [:create_part]

    test "deletes chosen part", %{conn: conn, part: part} do
      conn = delete(conn, Routes.part_path(conn, :delete, part))
      assert response(conn, 204)

      assert_error_sent 404, fn ->
        get(conn, Routes.part_path(conn, :show, part))
      end
    end
  end

  defp create_part(_) do
    part = fixture(:part)
    {:ok, part: part}
  end
end
