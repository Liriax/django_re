import { useEffect, useState } from "react"
import { Box, Typography, Divider, Grid } from "@mui/material"
import { Recommendation } from "./"
import * as API from "../api"

export default function RecommendationList() {
	const [recommendations, setRecommendations] = useState([])

	useEffect(() => {
        console.log("fetch")
		fetchRecommendations()
	}, [])

    const fetchRecommendations = async () => {
		try {
			const result = await API.recommendations.team(1)
			setRecommendations(result.data)
		} catch (error) {
			console.log(error)
		}
	}

    const filterRecommendationsByStatus = (status) => {
        return recommendations.filter(recommendation => recommendation.status === status)
    }

    const renderRecommendationsByStatus = (status) => {
        //TODO: Implement weight & date
        const filteredRecommendations = filterRecommendationsByStatus(status)
        if(filteredRecommendations.length >= 1) {
            const lengthTerm = filteredRecommendations.length >= 2 ? "Recommendations" : "Recommendation"
            return (
                <>
                    <Typography gutterBottom variant="subtitle1" sx={{display: "inline"}}> - {filteredRecommendations.length} {lengthTerm}</Typography>
                    <Grid container spacing={2}>
                        {filteredRecommendations.map(recommendation => {
                            const { id, recommendation_headline, status, createdAt } = recommendation
                            return (
                                <Grid key={recommendation.id} item xl={2} lg={2} md={3} sm={6} xs={12}>
                                    <Recommendation id={id} headline={recommendation_headline} status={status} date={createdAt} weight={parseInt(Math.random() * 100)} />
                                </Grid>    
                            )
                        })}
                    </Grid>
                </>
            )
        } else {
            return (
                <>
                    <Typography gutterBottom variant="subtitle1" sx={{display: "inline"}}> - 0 Recommendations</Typography>
                    <Typography variant="h6">No recommendations found</Typography>
                </>
            )
        }
    }

	return (
        <>
            <Box sx={{width: "100%", padding: 2}}>
                <Typography gutterBottom variant="h5" sx={{display: "inline"}}>Current</Typography>
                {recommendations ?
                    renderRecommendationsByStatus("current")
                : 
                    <Typography variant="h6">Loading recommendations</Typography>
                }
            </Box>
            <Divider />
            <Box sx={{width: "100%", padding: 2}}>
                <Typography gutterBottom variant="h5" sx={{display: "inline"}}>Implemented</Typography>
                {recommendations ?
                    renderRecommendationsByStatus("implemented")
                : 
                    <Typography variant="h6">Loading recommendations</Typography>
                }
            </Box>
            <Divider />
            <Box sx={{width: "100%", padding: 2}}>
                <Typography gutterBottom variant="h5" sx={{display: "inline"}}>Not applicable</Typography>
                {recommendations ?
                    renderRecommendationsByStatus("unapplicable")
                : 
                    <Typography variant="h6">Loading recommendations</Typography>
                }
            </Box>
        </>
	)
}
