import { Title } from "../";
import "./bar.scss";

const Bar = () => {
  return (
    <div className="bar">
      <div className="items">
        <div className="item logo">
          <img alt="logo" src="./logo.png"></img>
        </div>
        <div className="item text">
          <Title color="light" size="small">
            Team 1
          </Title>
        </div>
      </div>
    </div>
  );
};

export default Bar;
