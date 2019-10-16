defmodule KPortalWeb.Router do
  use KPortalWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", KPortalWeb do
    pipe_through :api

    get  "/part", PartController, :index
    post "/part", PartController, :create
    get  "/part/:id", PartController, :show
    get  "/type", TypeController, :index
    post "/type", TypeController, :create
    get  "/type/:id", TypeController, :show
    get  "/user", UserController, :index
    post "/user", UserController, :create
    get  "/user/:id", UserController, :show
  end
end
