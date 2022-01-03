import { RecommendationCard, StatisticsCard } from "../";
import "./recommendationDetails.scss";

export default function RecommendationDetails(props) {
  const { recommendation, onClick } = props;
  const { id, recommendation_headline, status, createdAt } = recommendation;
  const {
    implement: onClickImplement,
    unapliccable: onClickUnapplicable,
    close: onClickClose,
  } = onClick;

  const handleClickImplement = () => {
    onClickImplement(id)
  }

  const handleClickUnapplicable = () => {
    onClickUnapplicable(id)
  }

  return (
    <div className="recommendationDetails">
      <div className="close" onClick={onClickClose}>
        Go back
      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "center",
          marginTop: "2em",
        }}
      >
        <div className="recommendation">
          <RecommendationCard
            headline={recommendation_headline}
            status={status}
            date={createdAt}
            score={parseInt(Math.random() * 100)}
            width="auto"
          />
          <div className="actions">
            <div onClick={handleClickImplement} className="implement">
              Implement
            </div>
            <div onClick={handleClickUnapplicable} className="unapplicable">
              Not applicable
            </div>
          </div>
        </div>
        <div className="description">
          <div className="title">Sunt irure fugiat pariatur minim.</div>
          <div className="text">
            Cillum adipisicing officia nulla in. Voluptate incididunt occaecat
            amet Lorem ut enim esse aute mollit aliquip. Nostrud exercitation
            consectetur id eu ipsum fugiat quis. Deserunt tempor Lorem consequat
            cupidatat mollit. Et reprehenderit qui laborum nulla laboris dolor
            minim. Consectetur esse elit reprehenderit consectetur pariatur
            culpa. Qui ex sunt id elit.
          </div>
          <div className="title">Minim veniam aute est.</div>
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
      <StatisticsCard headline="Statistics" />
    </div>
  );
}
