import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { Title } from "../components";

test("title renders text as uppercase", () => {
  render(<Title uppercase>Hello</Title>);
  const linkElement = screen.getByText("HELLO");
  expect(linkElement).toBeInTheDocument();
});
