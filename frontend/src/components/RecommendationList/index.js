import { PropTypes } from "prop-types";
import { RecommendationCard, Title } from "../";
import "./recommendationList.scss";

export default function RecommendationList(props) {
  const { recommendations, onClick } = props;

  const sortRecommendationCategories = () => {
    //Sort recommendations by status in object (sortedRecommendations.suggested, ...implemented, ...rejected)
    return recommendations.reduce((categories, recommendation) => {
      const category = categories[recommendation.status];
      return {
        ...categories,
        [recommendation.status]: [
          ...(Array.isArray(category) ? category : []),
          recommendation,
        ],
      };
    }, {});
  };
  const recommendationCategories = sortRecommendationCategories();

  return (
    <div className="recommendationList">
      <RecommendationListCategory
        title="Suggested"
        recommendations={recommendationCategories?.suggested}
        onClick={onClick}
      />
      <hr />
      <RecommendationListCategory
        title="Implemented"
        recommendations={recommendationCategories?.implemented}
        onClick={onClick}
      />
      <hr />
      <RecommendationListCategory
        title="Rejected"
        recommendations={recommendationCategories?.rejected}
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
        <Title inline className="name" color="dark">
          {title}
        </Title>
        <Title inline className="count" color="dark" size="small">
          {count()}
        </Title>
      </div>
      {available() ? (
        <div className="list">
          {recommendations.map((recommendation) => {
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
          })}
        </div>
      ) : (
        <Title className="empty" color="dark" size="small">
          No recommendations found
        </Title>
      )}
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
