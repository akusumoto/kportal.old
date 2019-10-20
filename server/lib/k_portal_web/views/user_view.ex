defmodule KPortalWeb.UserView do
  use KPortalWeb, :view
  alias KPortalWeb.UserView

  def render("index.json", %{users: users}) do
    render_many(users, UserView, "user.json")
  end

  def render("show.json", %{user: user}) do
    render_one(user, UserView, "user.json")
  end

  def render("user.json", %{user: user}) do
    %{id: user.id,
      account: user.account,
      password: user.password,
      name: user.name,
      nickname: user.nickname,
      email: user.email,
      part: %{id: user.part.id,
              name: user.part.name},
      type: %{id: user.type.id,
              name: user.type.name},
      home_address: user.home_address,
      work_address: user.work_address,
      emergency_number: user.emergency_number,
      note: user.note
    }
  end
end
