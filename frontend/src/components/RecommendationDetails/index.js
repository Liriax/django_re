import { RecommendationCard } from "../";
import "./recommendationDetails.scss";

export default function RecommendationDetails(props) {
  const { recommendation, onClick } = props;
  const { /*id,*/ recommendation_headline, status, createdAt } = recommendation;
  const {
    implement: onClickImplement,
    unapliccable: onClickUnapplicable,
    close: onClickClose,
  } = onClick;

  return (
    <div className="recommendationDetails">
      <div className="close" onClick={onClickClose}>
        Go back
      </div>
      <div className="recommendation">
        <RecommendationCard
          headline={recommendation_headline}
          status={status}
          date={createdAt}
          score={parseInt(Math.random() * 100)}
        />
        <div className="actions">
          <div onClick={onClickImplement} className="implement">
            Implement
          </div>
          <div onClick={onClickUnapplicable} className="unapplicable">
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
          minim. Consectetur esse elit reprehenderit consectetur pariatur culpa.
          Qui ex sunt id elit.
        </div>
        <div className="title">Minim veniam aute est.</div>
        <div className="text">
          Cillum adipisicing officia nulla in. Voluptate incididunt occaecat
          amet Lorem ut enim esse aute mollit aliquip. Nostrud exercitation
          consectetur id eu ipsum fugiat quis. Deserunt tempor Lorem consequat
          cupidatat mollit. Et reprehenderit qui laborum nulla laboris dolor
          minim. Consectetur esse elit reprehenderit consectetur pariatur culpa.
          Qui ex sunt id elit.
        </div>
        <div className="title">Dolore culpa Lorem aliqua .</div>
        <div className="text">
          Cillum adipisicing officia nulla in. Voluptate incididunt occaecat
          amet Lorem ut enim esse aute mollit aliquip. Nostrud exercitation
          consectetur id eu ipsum fugiat quis. Deserunt tempor Lorem consequat
          cupidatat mollit. Et reprehenderit qui laborum nulla laboris dolor
          minim. Consectetur esse elit reprehenderit consectetur pariatur culpa.
          Qui ex sunt id elit.
        </div>
      </div>
    </div>
  );
}
