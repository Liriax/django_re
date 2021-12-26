import { useEffect, useState } from "react"
import { Bar } from "../components"
import * as API from "../api"

export default function App() {
    const [recommendations, setRecommendations] = useState(null)

    useEffect(() => {
        fetchData()
    }, [])

    const fetchData = async () => {
        try {
            const response = await API.recommendations.team(1)
            setRecommendations(await response.json())
        } catch(error) {
            console.log(error)
        }
    }

    return (
        <>
            <Bar />
            {JSON.stringify(recommendations)}
        </>
    )
}