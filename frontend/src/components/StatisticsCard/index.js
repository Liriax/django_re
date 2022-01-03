import { PropTypes } from "prop-types";
import "./statisticsCard.scss";

export default function StatisticsCard(props) {
  const { /*id,*/ headline, status, /*date,*/ score, onClick } = props;

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
    <div className="statisticsCard" onClick={handleClickRecommendation}>
      <div className="statisticsContent" style={style()}>
        <div className="text">{headline}</div>
        <div className="statisticsContainer">
          <div className="statisticsRow">
            <div>Received: </div>
            <div>1</div>
            <div>2</div>
            <div>3</div>
          </div>
          <div className="statisticsRow">implemented</div>
        </div>
      </div>
    </div>
  );
}

StatisticsCard.propTypes = {
  id: PropTypes.number,
  headline: PropTypes.string,
  status: PropTypes.string,
  date: PropTypes.string,
  score: PropTypes.number,
  onClick: PropTypes.func,
};
