import { PropTypes } from "prop-types";
import "./recommendationCard.scss";

export default function RecommendationCard(props) {
  const { /*id,*/ headline, status, /*date,*/ score, onClick, width } = props;

  const handleClickRecommendation = (event) => {
    onClick && onClick(event, props);
  };

  const style = () => {
    return {
      borderBottomColor:
        status === "implemented"
          ? "#0be881"
          : status === "unapplicable"
          ? "#ffa801"
          : "#3c40c6",
    };
  };

  return (
    <div
      className="recommendationCard"
      onClick={handleClickRecommendation}
      style={{ width: width }}
    >
      <div className="recommendationContent" style={style()}>
        <div className="text">{headline}</div>
        <div className="weights">
          <div className="first weight">{score} %</div>
        </div>
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
  width: PropTypes.string,
};
