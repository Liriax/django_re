import { PropTypes } from "prop-types";
import {
  Box,
  Card,
  CardActionArea,
  CardActions,
  CardHeader,
  Typography,
  Chip,
  IconButton,
  Tooltip,
} from "@mui/material";
import { Verified, HighlightOff } from "@mui/icons-material";

export default function RecommendationCard(props) {
  const { /*id,*/ headline, status, /*date,*/ score, onClick } = props;

  const handleClickRecommendation = (event) => {
    onClick(event, props);
  };

  const handleClickImplement = (event) => {
    alert("TODO: implement");
  };

  const handleClickUnapplicable = (event) => {
    alert("TODO: unapplicable");
  };

  const style = () => {
    return {
      card: {
        height: "10em",
        border: 0.5,
        borderBottom: 3,
        marginTop: 1,
        borderColor: "text.secondary",
        borderBottomColor:
          status === "implemented"
            ? "success.main"
            : status === "unapplicable"
            ? "error.main"
            : "primary.main",
      },
    };
  };

  return (
    <Card raised sx={style().card}>
      <CardActionArea
        sx={{ height: "65%" }}
        onClick={handleClickRecommendation}
      >
        <CardHeader
          component={() => (
            <>
              <Typography align="left" sx={{ padding: 1.5 }} variant="body1">
                {headline}
              </Typography>
            </>
          )}
        />
      </CardActionArea>
      <CardActions>
        <Box sx={{ mx: "auto" }}>
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
          <Tooltip title="Score">
            <IconButton>
              <Chip label={`${score} %`} variant="outlined" size="small" />
            </IconButton>
          </Tooltip>
        </Box>
      </CardActions>
    </Card>
  );
}

RecommendationCard.propTypes = {
  id: PropTypes.number,
  headline: PropTypes.string,
  status: PropTypes.string,
  date: PropTypes.string,
  score: PropTypes.number,
};
