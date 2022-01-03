import { PropTypes } from "prop-types";
import { Button, RecommendationCard, /*StatisticsCard,*/ Title } from "../";
import "./recommendationDetails.scss";

export default function RecommendationDetails(props) {
  const { recommendation, onClick } = props;
  const { id, recommendation_headline, status, createdAt } = recommendation;
  const {
    implement: onClickImplement,
    unapliccable: onClickReject,
    close: onClickClose,
  } = onClick;

  const handleClickImplement = () => {
    onClickImplement(id);
  };

  const handleClickReject = () => {
    onClickReject(id);
  };

  return (
    <div className="recommendationDetails">
      <Button className="close" color="light" onClick={onClickClose}>
        Go back
      </Button>
      <div className="content">
        <div className="recommendation">
          <RecommendationCard
            headline={recommendation_headline}
            status={status}
            date={createdAt}
            score={parseInt(Math.random() * 100)}
          />
          <div className="actions">
            <Button inline onClick={handleClickImplement} color="success">
              Implement
            </Button>
            <Button inline onClick={handleClickReject} color="warning">
              Reject
            </Button>
          </div>
          {/* <StatisticsCard headline="Statistics" /> */}
        </div>
        <hr />
        <div className="description">
          <Title color="light" size="medium">
            Sunt irure fugiat pariatur minim.
          </Title>
          <div className="text">
            Cillum adipisicing officia nulla in. Voluptate incididunt occaecat
            amet Lorem ut enim esse aute mollit aliquip. Nostrud exercitation
            consectetur id eu ipsum fugiat quis. Deserunt tempor Lorem consequat
            cupidatat mollit. Et reprehenderit qui laborum nulla laboris dolor
            minim. Consectetur esse elit reprehenderit consectetur pariatur
            culpa. Qui ex sunt id elit.
          </div>
          <Title color="light" size="medium">
            Minim veniam aute est.
          </Title>
          <div className="text">
            Cillum adipisicing officia nulla in. Voluptate incididunt occaecat
            amet Lorem ut enim esse aute mollit aliquip. Nostrud exercitation
            consectetur id eu ipsum fugiat quis. Deserunt tempor Lorem consequat
            cupidatat mollit. Et reprehenderit qui laborum nulla laboris dolor
            minim. Consectetur esse elit reprehenderit consectetur pariatur
            culpa. Qui ex sunt id elit.
          </div>
        </div>
      </div>
    </div>
  );
}

RecommendationDetails.propTypes = {
  recommendation: PropTypes.object,
  onClick: PropTypes.object,
};
