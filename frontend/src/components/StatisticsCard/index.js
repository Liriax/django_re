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
        status === "IMPLEMENTED"
          ? "#0be881"
          : status === "REJECTED"
          ? "#ffa801"
          : "#3c40c6",
    };
  };

  return (
    <div className="statisticsCard" onClick={handleClickRecommendation}>
      <div className="statisticsContent" style={style()}>
        <div className="headline">{headline}</div>
        <div className="statisticsContainer">
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(6, 1fr)",
              gridGap: "1em",
              padding: "1em",
            }}
          >
            <div />
            <div className="statHeading">Date</div>
            <div className="statHeading">Change Failure Rate</div>
            <div className="statHeading">Deployment Frequency</div>
            <div className="statHeading">Lead Time for Changes</div>
            <div className="statHeading">Time to Restore Services</div>
            <div className="rowHeading">Received:</div>
            <div className="statItem">1</div>
            <div className="statItem">1</div>
            <div className="statItem">2</div>
            <div className="statItem">3</div>
            <div className="statItem">3</div>
            <div className="rowHeading">Implemented:</div>
            <div className="statItem">1</div>
            <div className="statItem">1</div>
            <div className="statItem">2</div>
            <div className="statItem">3</div>
            <div className="statItem">3</div>
          </div>
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
