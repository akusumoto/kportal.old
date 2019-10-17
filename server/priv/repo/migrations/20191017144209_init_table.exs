defmodule KPortal.Repo.Migrations.InitTable do
  use Ecto.Migration

  alias KPortal.Accounts.{Part, Type}
  import Ecto.Repo

  def change do
    KPortal.Repo.insert %Part{name: "Vn1"}
    KPortal.Repo.insert %Part{name: "Vn2"}
    KPortal.Repo.insert %Part{name: "Va"}
    KPortal.Repo.insert %Part{name: "Vc"}
    KPortal.Repo.insert %Part{name: "Cb"}
    KPortal.Repo.insert %Part{name: "Fl"}
    KPortal.Repo.insert %Part{name: "Cl"}
    KPortal.Repo.insert %Part{name: "Sax"}
    KPortal.Repo.insert %Part{name: "Fg"}
    KPortal.Repo.insert %Part{name: "Ob"}
    KPortal.Repo.insert %Part{name: "Hr"}
    KPortal.Repo.insert %Part{name: "Tp"}
    KPortal.Repo.insert %Part{name: "Tb"}
    KPortal.Repo.insert %Part{name: "Tu"}
    KPortal.Repo.insert %Part{name: "Perc"}
    KPortal.Repo.insert %Part{name: "Gt"}
    KPortal.Repo.insert %Part{name: "Syn"}
    KPortal.Repo.insert %Part{name: "Bs"}
    KPortal.Repo.insert %Part{name: "Pf"}
    KPortal.Repo.insert %Part{name: "Cho Sp"}
    KPortal.Repo.insert %Part{name: "Cho Al"}
    KPortal.Repo.insert %Part{name: "Cho Tn"}
    KPortal.Repo.insert %Part{name: "Cho Bs"}
    KPortal.Repo.insert %Part{name: "Cond"}
    KPortal.Repo.insert %Part{name: "Staff"}

    KPortal.Repo.insert %Type{name: "社会人"}
    KPortal.Repo.insert %Type{name: "学生"}
  end
end
