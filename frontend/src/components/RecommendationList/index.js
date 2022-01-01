import { PropTypes } from "prop-types";
import { RecommendationCard } from "../";
import "./recommendationList.scss";

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
    <div className="recommendationList">
      <RecommendationListCategory
        title="Current"
        recommendations={sortedRecommendations?.current}
        onClick={onClick}
      />
      <hr />
      <RecommendationListCategory
        title="Implemented"
        recommendations={sortedRecommendations?.implemented}
        onClick={onClick}
      />
      <hr />
      <RecommendationListCategory
        title="Not applicable"
        recommendations={sortedRecommendations?.unapplicable}
        onClick={onClick}
      />
    </div>
  );
}

function RecommendationListCategory(props) {
  const { title, recommendations, onClick } = props;

  const available = () => {
    return recommendations?.length >= 1;
  };

  const count = () => {
    if (recommendations?.length === 1) {
      return `${recommendations.length} Recommendation`;
    } else {
      return `${recommendations?.length || 0} Recommendations`;
    }
  };

  return (
    <div className="recommendationCategory">
      <div className="title">
        <h2 className="name">{title}</h2>
        <h3 className="count"> - {count()}</h3>
      </div>
      <div className="content">
        {available() ? (
          recommendations.map((recommendation) => {
            const { id, recommendation_headline, status, createdAt } =
              recommendation;
            return (
              <RecommendationCard
                key={id}
                id={id}
                headline={recommendation_headline}
                status={status}
                date={createdAt}
                score={parseInt(Math.random() * 100)}
                onClick={onClick?.recommendation}
              />
            );
          })
        ) : (
          <h6>No recommendations found</h6>
        )}
      </div>
    </div>
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
