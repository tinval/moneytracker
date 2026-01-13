type Tx = {
    id: number;
    date: string;
    description: string;
    amount: number;
    currency_code: string;
};

const mockTxs: Tx[] = [
    { id: 101, date: "2026-01-10", description: "Groceries", amount: -82.5, currency_code: "CHF" },
    { id: 102, date: "2026-01-11", description: "Salary", amount: 4200, currency_code: "CHF" },
];

function formatMoney(amount: number, currency: string) {
    const sign = amount < 0 ? "-" : "";
    const abs = Math.abs(amount);
    return `${sign}${abs.toFixed(2)} ${currency}`;
}

export default function Transactions() {
    return (
        <section className="card">
            <div className="row space-between">
                <h1>Transactions</h1>
                <button className="btn">Import</button>
            </div>

            <div className="table">
                <div className="tr th">
                    <div>Date</div>
                    <div>Description</div>
                    <div className="right">Amount</div>
                </div>

                {mockTxs.map((t) => (
                    <div className="tr" key={t.id}>
                        <div>{t.date}</div>
                        <div>{t.description}</div>
                        <div className={`right ${t.amount < 0 ? "neg" : "pos"}`}>
                            {formatMoney(t.amount, t.currency_code)}
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
}
