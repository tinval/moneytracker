import { render, screen } from "@testing-library/react";
import { expect, test } from "vitest";
import { MemoryRouter } from "react-router-dom";
import App from "./App";

test("App renders and redirects to the index route", () => {
  render(
    <MemoryRouter initialEntries={["/"]}>
      <App />
    </MemoryRouter>,
  );
  const navElement = screen.getByText(/Accounts/i);
  expect(navElement).toBeInTheDocument();
});
