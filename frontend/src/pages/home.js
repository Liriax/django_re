import { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom"
import { Bar, RecommendationDetails, RecommendationList, Overlay } from "../components"
import * as API from "../api"

export default function Home() {
    const navigate = useNavigate()
    const { id } = useParams()
	const [recommendations, setRecommendations] = useState(null)
    const [recommendation, setRecommendation] = useState(null)

    useEffect(() => {
		fetchRecommendations()
	}, [])

    useEffect(() => {
        if(id) {
            fetchRecommendation()
        } else {
            setRecommendation(null)
        }
    }, [id])

    const fetchRecommendations = async () => {
		try {
			const result = await API.recommendations.team(1)
			setRecommendations(result.data)
		} catch (error) {
			console.log(error)
		}
	}

    const fetchRecommendation = async () => {
		try {
			const result = await API.recommendations.recommendation(id)
            console.log(result.data)
			setRecommendation(result.data)
		} catch (error) {
			console.log(error)
		}
	}
    
    const handleClickRecommendation = (event, recommendation) => {
        navigate(`./recommendation/${recommendation.id}`)
    }

    return (
        <>
            <Bar />
            {recommendations ? 
                <>
                    <RecommendationList recommendations={recommendations} onClick={{recommendation: handleClickRecommendation}} />
                    {recommendation && 
                        <Overlay>
                            <RecommendationDetails recommendation={recommendation} />
                        </Overlay>
                    }
                </>
            : "Loading"}
        </>
    )
}