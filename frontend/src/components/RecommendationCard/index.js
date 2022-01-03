import { PropTypes } from "prop-types";
import "./recommendationCard.scss";

export default function RecommendationCard(props) {
  const { /*id,*/ headline, status, /*date,*/ score, onClick } = props;

  const handleClickRecommendation = (event) => {
    onClick && onClick(event, props);
  };

  const generateClassNames = () => {
    const className = ["recommendationCard"];
    className.push(status);
    return className.join(" ");
  };

  return (
    <div className={generateClassNames()} onClick={handleClickRecommendation}>
      <div className="text">{headline}</div>
      <div className="weights">
        <div className="weight">{score} %</div>
      </div>
    </div>
  );
}

RecommendationCard.propTypes = {
  id: PropTypes.number,
  headline: PropTypes.string,
  status: PropTypes.string,
  date: PropTypes.string,
  score: PropTypes.number,
  onClick: PropTypes.func,
};
