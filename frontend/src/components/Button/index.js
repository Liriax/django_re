import { PropTypes } from "prop-types";
import { common } from "../../config";
import "./button.scss";

export default function Button(props) {
  const { className, onClick, inline, children, color } = props;

  const handleClick = () => {
    onClick && onClick();
  };

  const generateClassNames = () => {
    const classes = ["button", className];
    if (common.style.colors.includes(color)) {
      classes.push(color);
    } else {
      classes.push("primary");
    }
    if (inline) {
      classes.push("inline");
    }
    return classes.join(" ");
  };

  return (
    <div onClick={handleClick} className={generateClassNames()}>
      {children}
    </div>
  );
}

Button.propTypes = {
  className: PropTypes.string,
  onClick: PropTypes.func,
  inline: PropTypes.bool,
  children: PropTypes.string,
  color: PropTypes.oneOf(common.style.colors),
};
