type Account = {
  id: number;
  name: string;
  type: string;
  currency_code: string;
};

const mockAccounts: Account[] = [
  { id: 1, name: "UBS Checking", type: "Checking", currency_code: "CHF" },
  { id: 2, name: "Brokerage", type: "Investment", currency_code: "USD" },
];

export default function Accounts() {
  return (
    <section className="card">
      <div className="row space-between">
        <h1>Accounts</h1>
        <button className="btn">Add account</button>
      </div>

      <div className="table">
        <div className="tr th">
          <div>Name</div>
          <div>Type</div>
          <div>Currency</div>
        </div>

        {mockAccounts.map((a) => (
          <div className="tr" key={a.id}>
            <div>{a.name}</div>
            <div>{a.type}</div>
            <div>{a.currency_code}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
