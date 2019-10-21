defmodule KPortalWeb.Router do
  use KPortalWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  pipeline :auth do
    plug Guardian.Plug.VerifySession
    plug Guardian.Plug.VerifyHeader, realm: "Bearer"
    plug Guardian.Plug.LoadResource
  end

  pipeline :authed_access do
    plug(Guardian.Plug.EnsureAuthenticated, %{"type" => "access", handler: KPortalWeb.HttpErrorHandler})
  end

  scope "/", KPortalWeb do
    pipe_through [:api, :auth]

    get "/login", LoginController, :new
    post "/login", LoginController, :create
    delete "/login", LoginController, :delete
  end

  scope "/", KPortalWeb do
    pipe_through([:api, :auth, :authed_access])

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
