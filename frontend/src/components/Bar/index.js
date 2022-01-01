// import { NavLink } from "react-router-dom";
import "./bar.scss";

const Navigation = (props) => {
  return (
    <div className="navigation">
      <ul className="items">
        <li className="logo">
          <img alt="logo" src="./logo.png"></img>
        </li>
        {/* <NavLink className="link" to={`/`} activeClassName="active">
                    <li className="item">
                        <img alt={"title"} className="icon" src={`./icons/`}></img>
                        <span className="title">Title</span>
                    </li>
                </NavLink> */}
      </ul>
    </div>
  );
};

export default Navigation;
