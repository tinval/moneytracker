type User = {
  id: number;
  email: string;
  name?: string | null;
};

const mockUser: User = { id: 1, email: "user@example.com", name: "Alex" };

export default function User() {
  return (
    <section className="card">
      <h1>User</h1>

      <div className="kv">
        <div className="k">Name</div>
        <div className="v">{mockUser.name ?? "—"}</div>

        <div className="k">Email</div>
        <div className="v">{mockUser.email}</div>

        <div className="k">User ID</div>
        <div className="v">{mockUser.id}</div>
      </div>

      <div className="row">
        <button className="btn">Edit profile</button>
        <button className="btn secondary">Log out</button>
      </div>
    </section>
  );
}
