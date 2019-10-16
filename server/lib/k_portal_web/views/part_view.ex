defmodule KPortalWeb.PartView do
  use KPortalWeb, :view
  alias KPortalWeb.PartView

  def render("index.json", %{parts: parts}) do
    render_many(parts, PartView, "part.json")
  end

  def render("show.json", %{part: part}) do
    render_one(part, PartView, "part.json")
  end

  def render("part.json", %{part: part}) do
    %{id: part.id,
      name: part.name}
  end
end
