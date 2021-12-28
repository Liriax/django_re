import { PropTypes } from "prop-types"
import { Card, CardActionArea, CardActions, CardHeader, Typography, Chip, IconButton, Tooltip } from "@mui/material"
import { Verified, HighlightOff } from "@mui/icons-material"
//TODO: import * as API from "../api"

export default function Recommendation(props) {
    const handleClickImplement = (event) => {
        alert("implement")
        //TODO: API.recommendations.implement(props.id)
    }

    const handleClickUnapplicable = (event) => {
        alert("unapplicable")
        //TODO: API.recommendations.unapplicable(props.id)
    }

    const style = () => {
        return {
            card: {
                height: "10em",
                border: 0.5,
                borderBottom: 3,
                marginTop: 1,
                borderColor: "text.secondary",
                borderBottomColor: props.status === "implemented" ? "success.main" : props.status === "unapplicable" ? "error.main" : "primary.main",
            }
        }
    }

    return (
        <Card raised sx={style().card}>
            <CardActionArea sx={{height: "65%"}}>
                <CardHeader subheader={props.date} component={() =>
                    <Typography align="left" sx={{padding: 1.5}} variant="body1">{props.headline}</Typography>
                } />
            </CardActionArea>
            <CardActions>
                <Tooltip title="Implement">
                    <IconButton color="success" onClick={handleClickImplement}>
                        <Verified />
                    </IconButton>
                </Tooltip>
                <Tooltip title="Not Applicable">
                    <IconButton color="warning" onClick={handleClickUnapplicable}>
                        <HighlightOff />
                    </IconButton>
                </Tooltip>
                <Tooltip title="Weight">
                    <IconButton>
                        <Chip label={`${props.weight} %`} />
                    </IconButton>
                </Tooltip>
            </CardActions>
        </Card>
    )
}

Recommendation.propTypes = {
    id: PropTypes.number,
    headline: PropTypes.string,
    status: PropTypes.string,
    date: PropTypes.string,
    weight: PropTypes.number
}