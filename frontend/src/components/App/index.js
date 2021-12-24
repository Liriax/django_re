import { useEffect, useState } from "react"
import { Container, Divider } from "@mui/material"
import { Title } from "../"
import "./style.css"

function App() {
    const [data, setData] = useState(null)

    useEffect(async () => {
        const result = await fetch("http://localhost:8080/recommend/api")
        setData(result)
    }, [])

    return (
        <Container>
            <Title uppercase>{JSON.stringify(data)}</Title>
            <Divider />
        </Container>
    )
}

export default App