import { Link } from "react-router-dom";

export default function NotFound() {
    return (
        <section className="card">
            <h1>404</h1>
            <p>That page doesn’t exist.</p>
            <Link to="/" className="btn linklike">
                Go home
            </Link>
        </section>
    );
}
