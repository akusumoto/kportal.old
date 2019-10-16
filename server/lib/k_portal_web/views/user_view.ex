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
      part: user.part,
      nickname: user.nickname,
      account: user.account,
      password: user.password,
      name: user.name,
      email: user.email,
      home_address: user.home_address,
      work_address: user.work_address,
      type: user.type,
      emergency_number: user.emergency_number,
      note: user.note
    }
  end
end
