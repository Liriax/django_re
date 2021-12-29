import { PropTypes } from "prop-types";
import { Box, Typography, Divider, Grid } from "@mui/material";
import { RecommendationCard } from "./";

export default function RecommendationList(props) {
  const { recommendations, onClick } = props;

  const sortRecommendationsByStatus = () => {
    //Sort recommendations by status in object (sortedRecommendations.current, ...implemented, ...unapplicable)
    return recommendations.reduce((sortedRecommendations, recommendation) => {
      const recommendationStatus = sortedRecommendations[recommendation.status];
      return {
        ...sortedRecommendations,
        [recommendation.status]: [
          ...(Array.isArray(recommendationStatus) ? recommendationStatus : []),
          recommendation,
        ],
      };
    }, {});
  };
  const sortedRecommendations = sortRecommendationsByStatus();

  return (
    <>
      <RecommendationListCategory
        title="Current"
        recommendations={sortedRecommendations?.current}
        onClick={onClick}
      />
      <Divider />
      <RecommendationListCategory
        title="Implemented"
        recommendations={sortedRecommendations?.implemented}
        onClick={onClick}
      />
      <Divider />
      <RecommendationListCategory
        title="Not applicable"
        recommendations={sortedRecommendations?.unapplicable}
        onClick={onClick}
      />
    </>
  );
}

function RecommendationListCategory(props) {
  const { title, recommendations, onClick } = props;

  const available = () => {
    return recommendations.length >= 1;
  };

  const count = () => {
    if (recommendations.length === 1) {
      return `${recommendations.length} Recommendation`;
    } else {
      return `${recommendations.length || 0} Recommendations`;
    }
  };

  return (
    <Box sx={{ width: "100%", padding: 2 }}>
      <Typography gutterBottom variant="h5" sx={{ display: "inline" }}>
        {title}
      </Typography>
      <Typography gutterBottom variant="subtitle1" sx={{ display: "inline" }}>
        {" "}
        - {count()}
      </Typography>
      {available() ? (
        <Grid container spacing={2}>
          {recommendations.map((recommendation) => {
            const { id, recommendation_headline, status, createdAt } =
              recommendation;
            return (
              <Grid key={id} item xl={2} lg={2} md={3} sm={6} xs={12}>
                <RecommendationCard
                  id={id}
                  headline={recommendation_headline}
                  status={status}
                  date={createdAt}
                  score={parseInt(Math.random() * 100)}
                  onClick={onClick?.recommendation}
                />
              </Grid>
            );
          })}
        </Grid>
      ) : (
        <Typography variant="h6">No recommendations found</Typography>
      )}
    </Box>
  );
}

RecommendationList.propTypes = {
  recommendations: PropTypes.array,
  onClick: PropTypes.object,
};

RecommendationListCategory.propTypes = {
  title: PropTypes.string,
  recommendations: PropTypes.array,
  onClick: PropTypes.object,
};
