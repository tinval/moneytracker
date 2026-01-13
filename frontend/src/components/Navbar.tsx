import { NavLink } from "react-router-dom";

const linkClass = ({ isActive }: { isActive: boolean }) =>
    `nav-link ${isActive ? "active" : ""}`;

export default function Navbar() {
    return (
        <header className="navbar">
            <div className="container nav-inner">
                <div className="brand">
                    <span className="brand-dot" />
                    <span>Finance</span>
                </div>

                <nav className="nav-links">
                    <NavLink to="/" end className={linkClass}>
                        Main
                    </NavLink>
                    <NavLink to="/accounts" className={linkClass}>
                        Accounts
                    </NavLink>
                    <NavLink to="/transactions" className={linkClass}>
                        Transactions
                    </NavLink>
                    <NavLink to="/user" className={linkClass}>
                        User
                    </NavLink>
                </nav>
            </div>
        </header>
    );
}
