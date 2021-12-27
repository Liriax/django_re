import React from "react"
import ReactDOM from "react-dom"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { ThemeProvider } from "@mui/material/styles"
import { CssBaseline } from "@mui/material"
import { theme } from "./config"
// import { Home } from "./routes"
import "./index.css"
import Home from "./components/Home";
import "bootstrap/dist/css/bootstrap.min.css";

ReactDOM.render(
    <React.StrictMode>
        <BrowserRouter>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                    <Routes>
                        <Route path="/" element={<Home />} />
                    </Routes>
            </ThemeProvider>
        </BrowserRouter>
    </React.StrictMode>
, document.getElementById("root"))