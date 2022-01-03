import { PropTypes } from "prop-types";
import { common } from "../../config";
import "./title.scss";

export default function Title(props) {
  const { className, inline, uppercase, children, color, size } = props;

  const generateClassNames = () => {
    const classes = ["title", className];
    if (common.style.colors.includes(color)) {
      classes.push(color);
    } else {
      classes.push("primary");
    }
    if (common.style.sizes.includes(size)) {
      classes.push(size);
    } else {
      classes.push("medium");
    }
    if (inline) {
      classes.push("inline");
    }
    return classes.join(" ");
  };

  return (
    <div className={generateClassNames()}>
      {uppercase ? children?.toUpperCase() : children}
    </div>
  );
}

Title.propTypes = {
  className: PropTypes.string,
  inline: PropTypes.bool,
  uppercase: PropTypes.bool,
  children: PropTypes.string,
  color: PropTypes.string,
  size: PropTypes.string,
};
